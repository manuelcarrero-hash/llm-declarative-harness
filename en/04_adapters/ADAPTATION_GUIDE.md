# Guide for Adapting a Model or Platform

## 1. Capability inventory

Complete `CAPABILITY_PROFILE.template.yaml` with evidence. Do not infer tools from provider marketing.

## 2. Minimum mapping

| Harness capability | Acceptable substitute |
| --- | --- |
| Durable files | Drive, repository, workspace or equivalent storage |
| Separate agents | Subagents, separate processes or independent sessions |
| Independent review | Another agent that is not given the builder's preferred verdict |
| Hierarchical rules | Root file plus subdirectory rules with documented precedence |
| Measured context | Real token and window telemetry; otherwise qualitative signals |
| Approvals | Verifiable human pause before the action |
| Traces | Event, tool, handoff and outcome log |

## 3. Bootstrap

Instruct the agent to read `00_READ_ME_FIRST.md`, the manifest, the core and activated modules. Copy templates into the project only when they do not compete with existing sources. Record paths instead of pasting complete rules into every prompt.

## 4. Honest degradation

- Without subagents: use adversarial review and disclose that it is not independent.
- Without write access: operate in `REPORT` and deliver proposed content.
- Without telemetry: do not use context percentages.
- Without session creation: generate a handoff and ask the user to open a clean session.
- Without verifiable tools: mark evidence as `REPORTED` or `UNKNOWN`.

## 5. Conformance

Run `../06_validation/CONFORMANCE_TEST.md`. A platform may be partially compatible; it must publish the exceptions.
