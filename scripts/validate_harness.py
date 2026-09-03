#!/usr/bin/env python3
"""Deterministic, dependency-free structural validator for the harness."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path


MANIFESTS = ("HARNESS_MANIFEST.yaml", "en/HARNESS_MANIFEST.yaml")
CONTROL_FILES = (
    "06_validacion/CATALOGO_DE_CONTROLES.md",
    "en/06_validation/CONTROL_CATALOG.md",
)
SUITE_FILES = (
    "06_validacion/SUITE_REGRESION.md",
    "en/06_validation/REGRESSION_SUITE.md",
)
CAPABILITY_PROFILE_FILES = (
    "04_adaptadores/PERFIL_CAPACIDADES.template.yaml",
    "en/04_adapters/CAPABILITY_PROFILE.template.yaml",
)
# The catalog itself is normative, but a bilingual deletion would otherwise look
# like parity. This release baseline makes removal an explicit code review event.
EXPECTED_CONTROL_IDS = (
    "IDENTITY_01", "LOAD_01", "ONBOARDING_01", "AUTHORITY_01", "SECURITY_01",
    "GOAL_01", "GOVERNANCE_01", "GOVERNANCE_02", "OWNERSHIP_01",
    "ORCHESTRATION_01", "ITERATION_01", "REVIEW_01", "CALIBRATION_01",
    "LEARNING_01", "DEPENDENCY_01", "STATE_01", "HANDOFF_01", "RESUME_01",
    "COUNCIL_01", "CODE_INTELLIGENCE_01", "EXECUTION_01", "EXPERIENCE_01",
    "CLOSURE_01",
)
EXPECTED_CAPABILITY_IDS = (
    "durable_files", "hierarchical_instructions", "tool_use", "separate_agents",
    "independent_review", "context_telemetry", "session_creation_or_rotation",
    "human_approval_pause", "event_tracing", "resumable_state",
)
PATH_KEYS = {
    "es_entrypoint", "en_entrypoint", "parity_matrix", "human_entrypoint", "entrypoint",
    "path", "capability_profile", "universal_prompt", "load_receipt", "operating_contract",
    "authority_and_safety", "guided_start", "controlled_improvement", "compatibility_path",
    "startup_summary", "goal", "governance", "agent_assignment", "orchestration_trace",
    "work_map", "iteration_log", "status", "operational_pulse", "handoff", "evaluation",
    "reviewer_calibration", "improvement_candidate", "capabilities", "council_brief",
    "conformance", "control_catalog", "regression_suite", "software", "non_code",
    "structural_validator", "validator_tests", "non_technical_user_acceptance_cases",
    "compatibility_matrix",
}
EXPECTED_SCENARIO_START = 1
VERSION_PATTERN = re.compile(r"^[0-9]+\.[0-9]+(?:\.[0-9]+)?$")


@dataclass(frozen=True)
class Manifest:
    path: Path
    schema_version: str
    harness_version: str
    languages: tuple[str, ...]
    modules: tuple[str, ...]
    template_keys: tuple[str, ...]
    core_protocol_keys: tuple[str, ...]
    capability_labels: tuple[str, ...]
    authorization_labels: tuple[str, ...]
    factual_labels: tuple[str, ...]
    terminal_states: tuple[str, ...]
    validation_keys: tuple[str, ...]
    release_counts: dict[str, int]
    referenced_paths: tuple[str, ...]


@dataclass(frozen=True)
class CapabilityProfile:
    path: Path
    schema_version: str
    top_keys: tuple[str, ...]
    provider: str
    model: str
    platform: str
    evaluated_at: str
    capabilities: dict[str, dict[str, str]]


class ValidationError(ValueError):
    pass


def _section(text: str, name: str) -> str:
    lines = text.splitlines()
    try:
        start = lines.index(f"{name}:") + 1
    except ValueError:
        raise ValidationError(f"missing section {name!r}")
    body: list[str] = []
    for line in lines[start:]:
        if line and not line.startswith(" "):
            break
        body.append(line)
    return "\n".join(body) + "\n"


def _scalar(text: str, key: str) -> str:
    match = re.search(rf'(?m)^{re.escape(key)}:\s*["\']?([^"\'\n]+?)["\']?\s*$', text)
    if not match:
        raise ValidationError(f"missing scalar {key!r}")
    return match.group(1).strip()


def _nested_scalar(section: str, key: str) -> str:
    match = re.search(rf'(?m)^  {re.escape(key)}:\s*["\']?([^"\'\n]+?)["\']?\s*$', section)
    if not match:
        raise ValidationError(f"missing nested scalar {key!r}")
    return match.group(1).strip()


def _inline_list(text: str, key: str) -> tuple[str, ...]:
    match = re.search(rf"(?m)^{re.escape(key)}:\s*\[([^\]]*)\]\s*$", text)
    if not match:
        raise ValidationError(f"missing inline list {key!r}")
    values = [item.strip().strip('"\'') for item in match.group(1).split(",")]
    if not values or any(not item for item in values):
        raise ValidationError(f"empty or malformed inline list {key!r}")
    return tuple(values)


def _mapping_keys(text: str, section_name: str) -> tuple[str, ...]:
    body = _section(text, section_name)
    return tuple(re.findall(r"(?m)^  ([a-z][a-z0-9_]*):", body))


def _basic_yaml_checks(text: str) -> None:
    if "\t" in text:
        raise ValidationError("tabs are not allowed in YAML indentation")
    for number, line in enumerate(text.splitlines(), 1):
        stripped = line.lstrip(" ")
        if not stripped or stripped.startswith("#") or stripped.startswith("-"):
            continue
        if ":" not in stripped:
            raise ValidationError(f"line {number} is not a supported YAML mapping/list entry")
    for opener, closer in (("[", "]"), ("{", "}")):
        if text.count(opener) != text.count(closer):
            raise ValidationError(f"unbalanced {opener}{closer}")


def _split_inline_mapping(value: str) -> list[str]:
    items: list[str] = []
    current: list[str] = []
    quote: str | None = None
    for character in value:
        if character in "\"'":
            if quote == character:
                quote = None
            elif quote is None:
                quote = character
        if character == "," and quote is None:
            items.append("".join(current).strip())
            current = []
        else:
            current.append(character)
    if quote is not None:
        raise ValidationError("unterminated quote in inline mapping")
    items.append("".join(current).strip())
    return items


def _parse_inline_mapping(value: str) -> dict[str, str]:
    if not value.startswith("{") or not value.endswith("}"):
        raise ValidationError("capability must use a supported inline mapping")
    result: dict[str, str] = {}
    for item in _split_inline_mapping(value[1:-1]):
        if ":" not in item:
            raise ValidationError("malformed capability field")
        key, raw = item.split(":", 1)
        key, raw = key.strip(), raw.strip()
        if key in result:
            raise ValidationError(f"duplicate capability field {key!r}")
        result[key] = raw[1:-1] if len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in "\"'" else raw
    return result


def parse_capability_profile(path: Path) -> CapabilityProfile:
    text = path.read_text(encoding="utf-8")
    _basic_yaml_checks(text)
    top_keys = tuple(re.findall(r"(?m)^([a-z][a-z0-9_]*):", text))
    if duplicates := _duplicates(top_keys):
        raise ValidationError(f"duplicate top-level keys: {', '.join(duplicates)}")
    required_top = ("schema_version", "provider", "model", "platform", "evaluated_at", "capabilities", "exceptions")
    if top_keys != required_top:
        raise ValidationError("top-level fields or order differ from the capability profile contract")
    schema_version = _scalar(text, "schema_version")
    if not VERSION_PATTERN.fullmatch(schema_version):
        raise ValidationError("schema_version must be numeric dotted notation")
    metadata: dict[str, str] = {}
    for key in ("provider", "model", "platform", "evaluated_at"):
        match = re.search(rf'(?m)^{key}:\s*(["\'])(.*?)\1\s*$', text)
        if not match:
            raise ValidationError(f"template metadata field {key!r} must be a quoted string")
        metadata[key] = match.group(2)
        if metadata[key]:
            raise ValidationError(f"template metadata field {key!r} must remain empty")

    body = _section(text, "capabilities")
    material_lines = [line for line in body.splitlines() if line.strip() and not line.lstrip().startswith("#")]
    row_pattern = re.compile(r"^  ([a-z][a-z0-9_]*):\s*(\{.*\})\s*$")
    parsed_rows = [row_pattern.fullmatch(line) for line in material_lines]
    if any(match is None for match in parsed_rows):
        bad_line = material_lines[parsed_rows.index(None)]
        raise ValidationError(f"unsupported or malformed capability line: {bad_line.strip()!r}")
    rows = [(match.group(1), match.group(2)) for match in parsed_rows if match is not None]
    names = tuple(name for name, _ in rows)
    if not names:
        raise ValidationError("capabilities section is empty or malformed")
    if duplicates := _duplicates(names):
        raise ValidationError(f"duplicate capabilities: {', '.join(duplicates)}")
    if names != EXPECTED_CAPABILITY_IDS:
        raise ValidationError("capability IDs differ from the normative template baseline")
    capabilities = {name: _parse_inline_mapping(value) for name, value in rows}
    required_fields = ("status", "evidence", "authorization", "checked_at", "authorization_scope")
    for name, fields in capabilities.items():
        if tuple(fields) != required_fields:
            raise ValidationError(f"capability {name!r} fields or order differ from the contract")
    if not re.search(r"(?m)^exceptions:\s*\[\]\s*$", text):
        raise ValidationError("template exceptions must be an empty inline list")
    return CapabilityProfile(path, schema_version, top_keys, capabilities=capabilities, **metadata)


def parse_manifest(path: Path) -> Manifest:
    text = path.read_text(encoding="utf-8")
    _basic_yaml_checks(text)
    harness = _section(text, "harness")
    validation = _section(text, "validation")
    modules = tuple(re.findall(r"(?m)^  - id:\s*([a-z][a-z0-9_]*)\s*$", _section(text, "modules")))
    if not modules:
        raise ValidationError("modules section contains no supported module entries")
    counts = {
        key: int(value)
        for key, value in re.findall(r"(?m)^    (es|en):\s*([0-9]+)\s*$", validation)
    }
    if set(counts) != {"es", "en"}:
        raise ValidationError("release_regression_cases must declare es and en")

    schema_version = _scalar(text, "schema_version")
    harness_version = _nested_scalar(harness, "version")
    if not VERSION_PATTERN.fullmatch(schema_version):
        raise ValidationError("schema_version must be numeric dotted notation")
    if not VERSION_PATTERN.fullmatch(harness_version) or harness_version.count(".") != 2:
        raise ValidationError("harness version must use numeric major.minor.patch notation")

    paths: list[str] = []
    path_line = re.compile(r"^\s*([a-z][a-z0-9_]*):\s*(.*?)\s*$")
    for number, line in enumerate(text.splitlines(), 1):
        match = path_line.fullmatch(line)
        if not match or match.group(1) not in PATH_KEYS:
            continue
        raw = match.group(2)
        if not raw and match.group(1) == "guided_start":  # top-level section, not core_protocols field
            continue
        if len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in "\"'":
            value = raw[1:-1]
        elif raw and not any(character.isspace() for character in raw) and not raw.startswith(("[", "{")):
            value = raw
        else:
            raise ValidationError(f"line {number} has a malformed path field {match.group(1)!r}")
        if not value:
            raise ValidationError(f"line {number} has an empty path field {match.group(1)!r}")
        paths.append(value)
    return Manifest(
        path=path,
        schema_version=schema_version,
        harness_version=harness_version,
        languages=_inline_list(harness, "  languages"),
        modules=modules,
        template_keys=_mapping_keys(text, "templates"),
        core_protocol_keys=_mapping_keys(text, "core_protocols"),
        capability_labels=_inline_list(text, "capability_labels"),
        authorization_labels=_inline_list(text, "authorization_labels"),
        factual_labels=_inline_list(text, "factual_labels"),
        terminal_states=_inline_list(text, "terminal_states"),
        validation_keys=_mapping_keys(text, "validation"),
        release_counts=counts,
        referenced_paths=tuple(paths),
    )


def control_ids(path: Path) -> tuple[str, ...]:
    text = path.read_text(encoding="utf-8")
    return tuple(re.findall(r"(?m)^\| `([A-Z][A-Z0-9_]+)` \|", text))


def scenario_ids(path: Path) -> tuple[str, ...]:
    text = path.read_text(encoding="utf-8")
    return tuple(re.findall(r"(?m)^\| (R[0-9]{2}) \|", text))


def _duplicates(values: tuple[str, ...]) -> list[str]:
    return sorted({value for value in values if values.count(value) > 1})


def validate(root: Path) -> list[str]:
    errors: list[str] = []

    manifests: list[Manifest] = []
    for relative in MANIFESTS:
        try:
            manifests.append(parse_manifest(root / relative))
        except (OSError, UnicodeError, ValidationError, ValueError) as exc:
            errors.append(f"{relative}: {exc}")

    for path in sorted(root.rglob("*.json")):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError) as exc:
            errors.append(f"{path.relative_to(root)}: invalid JSON: {exc}")

    for manifest in manifests:
        base = manifest.path.parent
        for relative in manifest.referenced_paths:
            candidate = (base / relative).resolve()
            try:
                candidate.relative_to(root.resolve())
            except ValueError:
                errors.append(f"{manifest.path.relative_to(root)}: path escapes repository: {relative}")
                continue
            if not candidate.is_file():
                errors.append(f"{manifest.path.relative_to(root)}: missing referenced file: {relative}")
        for label, values in (
            ("modules", manifest.modules),
            ("template keys", manifest.template_keys),
            ("core protocol keys", manifest.core_protocol_keys),
        ):
            if duplicates := _duplicates(values):
                errors.append(f"{manifest.path.relative_to(root)}: duplicate {label}: {', '.join(duplicates)}")

    profiles: list[CapabilityProfile] = []
    for relative in CAPABILITY_PROFILE_FILES:
        try:
            profile = parse_capability_profile(root / relative)
            profiles.append(profile)
            if manifests:
                allowed_statuses = set(manifests[0].capability_labels)
                allowed_authorizations = set(manifests[0].authorization_labels)
                for name, fields in profile.capabilities.items():
                    if fields["status"] not in allowed_statuses:
                        errors.append(f"{relative}: capability {name!r} has invalid status {fields['status']!r}")
                    if fields["authorization"] not in allowed_authorizations:
                        errors.append(f"{relative}: capability {name!r} has invalid authorization {fields['authorization']!r}")
                    if fields["status"] != "UNKNOWN" and not fields["evidence"].strip():
                        errors.append(f"{relative}: capability {name!r} claims {fields['status']} without evidence")
                    expected_defaults = {
                        "status": "UNKNOWN", "evidence": "", "authorization": "UNKNOWN",
                        "checked_at": "", "authorization_scope": "",
                    }
                    if fields != expected_defaults:
                        errors.append(f"{relative}: capability {name!r} template values must remain neutral and empty")
        except (OSError, UnicodeError, ValidationError, ValueError) as exc:
            errors.append(f"{relative}: {exc}")

    if len(profiles) == 2:
        es_profile, en_profile = profiles
        if es_profile.schema_version != en_profile.schema_version:
            errors.append("capability profiles: ES/EN schema versions differ")
        if es_profile.top_keys != en_profile.top_keys:
            errors.append("capability profiles: ES/EN top-level fields differ")
        if tuple(es_profile.capabilities) != tuple(en_profile.capabilities):
            errors.append("capability profiles: ES/EN capability names or order differ")
        else:
            for name in es_profile.capabilities:
                if tuple(es_profile.capabilities[name]) != tuple(en_profile.capabilities[name]):
                    errors.append(f"capability profiles: ES/EN fields differ for {name!r}")

    controls: list[tuple[str, ...]] = []
    for relative in CONTROL_FILES:
        ids = control_ids(root / relative)
        controls.append(ids)
        if not ids:
            errors.append(f"{relative}: no control IDs found")
        if duplicates := _duplicates(ids):
            errors.append(f"{relative}: duplicate control IDs: {', '.join(duplicates)}")
        if ids != EXPECTED_CONTROL_IDS:
            errors.append(f"{relative}: control IDs differ from the normative release baseline")

    scenarios: list[tuple[str, ...]] = []
    for relative in SUITE_FILES:
        ids = scenario_ids(root / relative)
        scenarios.append(ids)
        if duplicates := _duplicates(ids):
            errors.append(f"{relative}: duplicate scenario IDs: {', '.join(duplicates)}")
        expected = tuple(f"R{number:02d}" for number in range(EXPECTED_SCENARIO_START, len(ids) + 1))
        if ids != expected:
            errors.append(f"{relative}: scenarios must be unique, ordered and continuous from R01")

    if len(manifests) == 2:
        es, en = manifests
        comparable = (
            "schema_version", "harness_version", "languages", "modules", "template_keys",
            "core_protocol_keys", "capability_labels", "authorization_labels", "factual_labels",
            "terminal_states", "validation_keys", "release_counts",
        )
        for field in comparable:
            if getattr(es, field) != getattr(en, field):
                errors.append(f"manifests: ES/EN structural mismatch in {field}")
        for lang, count in es.release_counts.items():
            actual = len(scenarios[0 if lang == "es" else 1]) if len(scenarios) == 2 else -1
            if count != actual:
                errors.append(f"manifest declares {count} {lang} scenarios, found {actual}")

    if len(controls) == 2 and controls[0] != controls[1]:
        errors.append("control catalogs: ES/EN control IDs or order differ")
    if len(scenarios) == 2 and scenarios[0] != scenarios[1]:
        errors.append("regression suites: ES/EN scenario IDs or order differ")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args(argv)
    errors = validate(args.root.resolve())
    if errors:
        print(f"FAIL: {len(errors)} structural error(s)", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("PASS: harness structure, references, JSON, regression suites and ES/EN parity")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
