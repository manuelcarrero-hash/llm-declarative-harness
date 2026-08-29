# Normative Control Catalog

This file defines the IDs used by `EVALUATION.template.json`. An agent must not infer or redefine their meaning.

| ID | Area | Critical | Observable question | Typical evidence |
| --- | --- | --- | --- | --- |
| `IDENTITY_01` | Identity | Yes | Did every participant operate on the intended project, repository, branch and objective? | Remote, branch, commit, workspace and agent acknowledgement |
| `GOAL_01` | Goal | Yes | Were outcome, scope, boundaries, completion evidence and terminal state explicit and stable? | Goal contract and checkpoint |
| `GOVERNANCE_01` | Governance | Yes | Were effective instructions resolved for the actual working directories? | Instruction chain, target paths and audit |
| `GOVERNANCE_02` | Governance | No | Were material commands and rules supported by current project evidence? | Manifests, CI, command results and audit |
| `OWNERSHIP_01` | Team | No | Did each workstream have bounded ownership without conflicting writes? | Assignments, diffs, workspace state and integration record |
| `REVIEW_01` | Review | Yes when material change occurred | Did an independent reviewer inspect the actual change and issue a supported verdict before closure? | Diff, findings, rerun evidence and verdict |
| `STATE_01` | State | Yes | Did authoritative status distinguish implemented, committed, pushed, reviewed, deployed and user-validated? | Snapshot compared with repository and deployment |
| `HANDOFF_01` | Continuity | Yes when rotation occurred | Did the handoff contain verified progress, partial state, risks, rules, exact next action and stopping condition? | Handoff and cited evidence |
| `RESUME_01` | Continuity | Yes when rotation occurred | Did the successor identify the project, checkpoint, remaining gap and first action before editing? | Handshake and first subsequent action |
| `CLOSURE_01` | Closure | Yes | Was closure supported by every required test, review, deployment and acceptance gate? | Terminal report and evidence for each gate |

## Allowed statuses

- `PASS`: inspected evidence shows that the behavior occurred.
- `FAIL`: evidence shows contrary behavior.
- `NOT_OBSERVED`: the run did not produce enough evidence to judge.
- `NOT_APPLICABLE`: the control was genuinely outside the run.

## Decision rules

- A critical control marked `FAIL` makes the run unreliable.
- A critical control marked `NOT_OBSERVED` prevents a high-confidence conclusion.
- If a material change occurred, `REVIEW_01` cannot be `NOT_APPLICABLE` merely because no reviewer was assigned.
- If no rotation occurred, `HANDOFF_01` and `RESUME_01` may be `NOT_APPLICABLE`.
- An agent-authored summary is not independent evidence of its own compliance.
