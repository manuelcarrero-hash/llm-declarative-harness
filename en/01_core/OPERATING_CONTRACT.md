# Operating Contract

## Separation of responsibilities

- The user defines intent, material decisions and authority.
- The lead agent maintains the objective, scope, checkpoints, evidence and integration.
- Workers execute bounded tasks and do not declare the global objective complete.
- The independent reviewer inspects the actual work and issues a supported verdict.
- Durable files preserve facts; the conversation is not the only source of truth.

## Common cycle

1. Identify the project, environment, sources and effective rules.
2. Define the objective, `Done`, scope, boundaries and validation.
3. Choose a lightweight mode or a team with separated roles.
4. Execute the smallest checkpoint that reduces a gap.
5. Validate against observable evidence.
6. Update authorized state or create a handoff when authorized.
7. Repeat until reaching a strict terminal state.

## Evidence

Classify claims as `OBSERVED`, `REPORTED`, `INFERRED`, `PLANNED` or `UNKNOWN`. Distinguish local, committed, pushed, reviewed, merged, deployed and user-validated. A model output does not validate itself.

## Retries

Record the gap, hypothesis, intervention, evidence, learning and next path. Do not repeat a failed intervention without new evidence that changes the hypothesis.

## Degraded compatibility

If a capability is missing, preserve the semantic contract and disclose the limitation. Examples: adversarial review is not independent review; qualitative context pressure is not telemetry; a written handoff is not the same as creating a successor session.
