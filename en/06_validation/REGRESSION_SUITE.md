# Harness Regression Suite

The suite evaluates outcomes and material checkpoints; it does not require identical paths across models. Three runs remain the minimum pilot and five an initial decision basis. Before treating a functional version as stable, run 12–20 representative cases, including at least the following 13.

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

Add up to seven release-risk cases: current facts, insufficient sources, context loss, wrong tool, agent duplication, exhausted budget, partial integration and deployment failure.

## Evidence per case

Record stimulus, version, provider/model/platform, capabilities, artifacts, applicable controls, observed output, human intervention and verdict. Combine rule-based evaluation with human review of a sample. Agent self-classification does not prove the outcome.

## Comparison

Compare with the prior version by control and scenario. A correction is promising after one pass and established only after another relevant run without weakening the test.
