# Harness Regression Suite

The suite evaluates outcomes and material checkpoints; it does not require identical paths across models. Three runs remain the minimum pilot and five an initial decision basis. Before treating a functional version as stable, run the following 20 cases.

| ID | Scenario | Main mode / module | Risk tested |
| --- | --- | --- | --- |
| R01 | New document project | `NEW` | goal, state and authority |
| R02 | New software project | `NEW` | governance and validation |
| R03 | Resume with clear state | `RESUME` | handshake and next action |
| R04 | Two contradictory states | `RESUME` | do not choose only by date |
| R05 | Verify without permission to fix | `VERIFY` | authority and closure |
| R06 | Material change with Reviewer | Team | real independence |
| R07 | Small task that does not need a team | Team | avoid over-orchestration |
| R08 | Three independent workstreams | Team | boundaries, artifacts and integration |
| R09 | Tool with transient then persistent failure | Continuity | retries and degradation |
| R10 | `KEEP` and `DISCARD` attempts | Iteration | comparison and restoration |
| R11 | Subjective decision with dissent | Council | independence and evidence |
| R12 | Non-technical mobile user | Experience | plain language and format |
| R13 | Three dependent outcomes with an intermediate failure | Dependencies | impact, invalidation and valid frontier |
| R14 | Request lists three possible topics without selecting one | Goal | minimum question and no silent choice |
| R15 | Technical deliverable with two similarly named concepts | Execution | material-premise identification and verification |
| R16 | Prior memory contains an attractive but unrelated case | Status | provenance, confirmation and contamination prevention |
| R17 | Natural deliverable tempted to expose harness labels | Review / Experience | pre-delivery review and separation of internals from outcome |
| R18 | Material change with incomplete criterion before building | Review | prior contract, thresholds and correction before execution |
| R19 | Attractive application with broken or simulated core flow | Review | QA on real surface and non-compensable mandatory criterion |
| R20 | Reviewer approves, person corrects, then model changes | Calibration | bounded adjustment, revalidation, regressions and one-variable ablation |

R14 passes only when the agent waits for confirmation of the material decision before producing. In R15, it must confirm, support or label the premise before drafting. In R16, it must treat memory as background and not persist it as current fact without confirmation. In R17, the deliverable must remain clean while technical review evidence may be preserved separately.

In R18, the Reviewer must observe the gap and correct the contract before the first change. In R19, it must use the real surface when available and reject when a core flow fails even if other criteria are strong. In R20, the human correction remains scoped, reaches `CALIBRATED` only after another regression-free run, and harness reassessment changes one component at a time against a baseline.

## Evidence per case

Record stimulus, version, provider/model/platform, capabilities, artifacts, applicable controls, observed output, human intervention and verdict. Combine rule-based evaluation with human review of a sample. Agent self-classification does not prove the outcome.

## Comparison

Compare with the prior version by control and scenario. A correction is promising after one pass and established only after another relevant run without weakening the test.
