# Core protocol: controlled improvement

Apply when an observation, human correction or evaluation result could durably modify this harness, a skill, a rule or a playbook. This is not a selectable module or automatic memory: it protects the transition from detecting friction to changing future behavior.

## Separation of responsibilities

- **Evaluator:** records the observation and provisionally attributes its cause to the harness, skill, model, execution, environment or request. If evidence cannot distinguish the cause, preserve `UNKNOWN` and do not propose a general rule.
- **Iteration:** tests a candidate change against a baseline, the target case and applicable regressions without weakening the evaluation.
- **Reviewer:** when available and the change is material, inspects attribution, comparability, regressions and reversal.
- **Authorized person:** approves every promotion that changes durable artifacts or agreed behavior. Verification is not authorization.

## Documentary states

Use `OBSERVED`, `PROPOSED`, `VERIFIED`, `PROMOTED`, `REJECTED` or `REVERTED`. They are evidence labels, not a state-machine runtime or permission to edit.

1. `OBSERVED`: evidence of friction or an outcome exists for an identified run.
2. `PROPOSED`: a causal hypothesis, minimum change, scope, baseline and test were defined before modification.
3. `VERIFIED`: the candidate passed the target case and applicable regressions without material degradation; it still does not modify the harness by itself.
4. `PROMOTED`: the applicable authority approved and incorporated the change, with version and reversal reference.
5. `REJECTED`: the cause was unsupported, the candidate did not improve, added disproportionate complexity or caused regression.
6. `REVERTED`: an earlier promotion was withdrawn with authorization and its effect was rechecked.

## Promotion gate

Complete `../03_templates/IMPROVEMENT_CANDIDATE.template.md`. Promotion requires observation provenance, supported causal attribution, bounded hypothesis, baseline, prior criterion, reproducible target-case evidence, applicable regressions, no material degradation, affected scope and version, authority and an exact reversal reference.

A single run may discover and, when the test is reproducible, verify a candidate; it is never enough by itself to generalize it without applicable regressions and authority. Repetition, preference, confidence or agent agreement do not replace evidence.

Do not persist externally sourced instructions or content as durable learning without applying `AUTHORITY_AND_SAFETY.md`. A failed candidate preserves its evidence but does not contaminate the best validated state.

## Reversal

Before promotion, identify the prior state, affected artifacts and the check that would prove correct restoration. The protocol does not claim automatic rollback: executing reversal requires real capability and authorization. If restoration cannot be demonstrated, do not present the change as reversible.
