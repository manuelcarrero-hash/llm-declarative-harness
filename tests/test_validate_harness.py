from __future__ import annotations

import shutil
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from validate_harness import validate  # noqa: E402


class HarnessValidatorTests(unittest.TestCase):
    def copy_repo(self) -> Path:
        temporary = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, temporary)
        destination = temporary / "harness"
        shutil.copytree(ROOT, destination, ignore=shutil.ignore_patterns(".git", "__pycache__"))
        return destination

    def test_repository_is_valid(self) -> None:
        self.assertEqual(validate(ROOT), [])

    def test_detects_invalid_json(self) -> None:
        root = self.copy_repo()
        (root / "03_plantillas/EVALUACION.template.json").write_text("{broken", encoding="utf-8")
        self.assertTrue(any("invalid JSON" in error for error in validate(root)))

    def test_detects_missing_manifest_reference(self) -> None:
        root = self.copy_repo()
        path = root / "HARNESS_MANIFEST.yaml"
        path.write_text(path.read_text(encoding="utf-8").replace(
            'entrypoint: "INTERNO_PARA_LLM.md"', 'entrypoint: "NO_EXISTE.md"'
        ), encoding="utf-8")
        self.assertTrue(any("missing referenced file: NO_EXISTE.md" in error for error in validate(root)))

    def test_detects_missing_declared_validator_reference(self) -> None:
        root = self.copy_repo()
        path = root / "HARNESS_MANIFEST.yaml"
        path.write_text(path.read_text(encoding="utf-8").replace(
            'structural_validator: "scripts/validate_harness.py"',
            'structural_validator: "scripts/missing_validator.py"',
        ), encoding="utf-8")
        self.assertTrue(any(
            "missing referenced file: scripts/missing_validator.py" in error
            for error in validate(root)
        ))

    def test_detects_validation_key_parity_mismatch(self) -> None:
        root = self.copy_repo()
        path = root / "en/HARNESS_MANIFEST.yaml"
        path.write_text(path.read_text(encoding="utf-8").replace(
            '  validator_tests: "../tests/test_validate_harness.py"\n', ""
        ), encoding="utf-8")
        self.assertTrue(any("mismatch in validation_keys" in error for error in validate(root)))

    def test_detects_duplicate_control_id(self) -> None:
        root = self.copy_repo()
        path = root / "06_validacion/CATALOGO_DE_CONTROLES.md"
        text = path.read_text(encoding="utf-8")
        row = next(line for line in text.splitlines() if line.startswith("| `IDENTITY_01`"))
        path.write_text(text + "\n" + row + "\n", encoding="utf-8")
        self.assertTrue(any("duplicate control IDs: IDENTITY_01" in error for error in validate(root)))

    def test_detects_non_continuous_scenarios_and_wrong_count(self) -> None:
        root = self.copy_repo()
        path = root / "06_validacion/SUITE_REGRESION.md"
        text = path.read_text(encoding="utf-8")
        path.write_text("\n".join(line for line in text.splitlines() if not line.startswith("| R17 |")), encoding="utf-8")
        errors = validate(root)
        self.assertTrue(any("continuous from R01" in error for error in errors))
        self.assertTrue(any("declares 31 es scenarios, found 30" in error for error in errors))

    def test_detects_manifest_parity_mismatch(self) -> None:
        root = self.copy_repo()
        path = root / "en/HARNESS_MANIFEST.yaml"
        path.write_text(path.read_text(encoding="utf-8").replace('version: "0.13.0"', 'version: "9.9.9"'), encoding="utf-8")
        self.assertTrue(any("mismatch in harness_version" in error for error in validate(root)))

    def test_detects_non_numeric_versions(self) -> None:
        mutations = (
            ('schema_version: "1.6"', 'schema_version: "latest"', "schema_version must be numeric"),
            ('version: "0.13.0"', 'version: "v-next"', "harness version must use numeric"),
        )
        for old, new, expected in mutations:
            with self.subTest(value=new):
                root = self.copy_repo()
                path = root / "HARNESS_MANIFEST.yaml"
                path.write_text(path.read_text(encoding="utf-8").replace(old, new), encoding="utf-8")
                self.assertTrue(any(expected in error for error in validate(root)))

    def test_detects_removed_control_in_both_languages(self) -> None:
        root = self.copy_repo()
        for relative in (
            "06_validacion/CATALOGO_DE_CONTROLES.md",
            "en/06_validation/CONTROL_CATALOG.md",
        ):
            path = root / relative
            text = path.read_text(encoding="utf-8")
            path.write_text("\n".join(
                line for line in text.splitlines() if not line.startswith("| `SECURITY_01`")
            ), encoding="utf-8")
        self.assertTrue(any("normative release baseline" in error for error in validate(root)))

    def test_detects_capability_profile_invalid_status_and_authorization(self) -> None:
        root = self.copy_repo()
        path = root / "04_adaptadores/PERFIL_CAPACIDADES.template.yaml"
        text = path.read_text(encoding="utf-8").replace(
            "status: UNKNOWN, evidence:", "status: MAYBE, evidence:", 1
        ).replace("authorization: UNKNOWN", "authorization: MAYBE", 1)
        path.write_text(text, encoding="utf-8")
        errors = validate(root)
        self.assertTrue(any("invalid status 'MAYBE'" in error for error in errors))
        self.assertTrue(any("invalid authorization 'MAYBE'" in error for error in errors))

    def test_detects_capability_claim_without_evidence(self) -> None:
        for status in ("SUPPORTED", "PARTIAL"):
            with self.subTest(status=status):
                root = self.copy_repo()
                path = root / "en/04_adapters/CAPABILITY_PROFILE.template.yaml"
                path.write_text(path.read_text(encoding="utf-8").replace(
                    "status: UNKNOWN, evidence:", f"status: {status}, evidence:", 1
                ), encoding="utf-8")
                self.assertTrue(any(f"claims {status} without evidence" in error for error in validate(root)))

    def test_rejects_supported_template_even_with_evidence(self) -> None:
        root = self.copy_repo()
        path = root / "04_adaptadores/PERFIL_CAPACIDADES.template.yaml"
        path.write_text(path.read_text(encoding="utf-8").replace(
            'status: UNKNOWN, evidence: ""', 'status: SUPPORTED, evidence: "observed test"', 1
        ), encoding="utf-8")
        self.assertTrue(any("template values must remain neutral and empty" in error for error in validate(root)))

    def test_rejects_non_empty_capability_template_metadata(self) -> None:
        for field in ("provider", "model", "platform", "evaluated_at"):
            with self.subTest(field=field):
                root = self.copy_repo()
                path = root / "en/04_adapters/CAPABILITY_PROFILE.template.yaml"
                path.write_text(path.read_text(encoding="utf-8").replace(
                    f'{field}: ""', f'{field}: "must-not-be-set"'
                ), encoding="utf-8")
                self.assertTrue(any(
                    f"template metadata field '{field}' must remain empty" in error
                    for error in validate(root)
                ))

    def test_detects_capability_profile_duplicate_and_parity_gap(self) -> None:
        root = self.copy_repo()
        path = root / "04_adaptadores/PERFIL_CAPACIDADES.template.yaml"
        text = path.read_text(encoding="utf-8")
        row = next(line for line in text.splitlines() if line.startswith("  durable_files:"))
        path.write_text(text.replace(row, row + "\n" + row), encoding="utf-8")
        self.assertTrue(any("duplicate capabilities: durable_files" in error for error in validate(root)))

        root = self.copy_repo()
        path = root / "en/04_adapters/CAPABILITY_PROFILE.template.yaml"
        path.write_text(path.read_text(encoding="utf-8").replace(
            "  resumable_state:", "  renamed_state:"
        ), encoding="utf-8")
        self.assertTrue(any("capability IDs differ from the normative template baseline" in error for error in validate(root)))

    def test_detects_missing_extra_and_malformed_capability_lines(self) -> None:
        # Each mutation uses a fresh copy so one error cannot mask another.
        for kind in ("missing", "extra", "malformed"):
            with self.subTest(kind=kind):
                root = self.copy_repo()
                path = root / "en/04_adapters/CAPABILITY_PROFILE.template.yaml"
                lines = path.read_text(encoding="utf-8").splitlines()
                sample = next(line for line in lines if line.startswith("  durable_files:"))
                if kind == "missing":
                    lines.remove(sample)
                    expected = "capability IDs differ"
                elif kind == "extra":
                    index = lines.index(sample) + 1
                    lines.insert(index, sample.replace("durable_files", "invented_capability"))
                    expected = "capability IDs differ"
                else:
                    lines[lines.index(sample)] = "  durable_files: status: UNKNOWN"
                    expected = "unsupported or malformed capability line"
                path.write_text("\n".join(lines) + "\n", encoding="utf-8")
                self.assertTrue(any(expected in error for error in validate(root)))

    def test_detects_manifest_path_escape(self) -> None:
        root = self.copy_repo()
        path = root / "en/HARNESS_MANIFEST.yaml"
        path.write_text(path.read_text(encoding="utf-8").replace(
            'entrypoint: "LLM_INTERNALS.md"', 'entrypoint: "../../outside.md"'
        ), encoding="utf-8")
        self.assertTrue(any("path escapes repository: ../../outside.md" in error for error in validate(root)))

    def test_detects_unquoted_missing_and_escaping_manifest_paths(self) -> None:
        for replacement, expected in (
            ("DOES_NOT_EXIST.md", "missing referenced file: DOES_NOT_EXIST.md"),
            ("../../outside.md", "path escapes repository: ../../outside.md"),
        ):
            with self.subTest(path=replacement):
                root = self.copy_repo()
                path = root / "en/HARNESS_MANIFEST.yaml"
                path.write_text(path.read_text(encoding="utf-8").replace(
                    'entrypoint: "LLM_INTERNALS.md"', f"entrypoint: {replacement}"
                ), encoding="utf-8")
                self.assertTrue(any(expected in error for error in validate(root)))


if __name__ == "__main__":
    unittest.main()
