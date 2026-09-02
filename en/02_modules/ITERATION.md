# Module: Verifiable Iteration

Activate when the outcome benefits from several reversible attempts that can be compared against stable validation. Do not activate for brief tasks, obvious fixes, irreversible actions, or work where experimentation materially increases risk.

The user does not configure this module or need to learn its mechanics. The agent decides whether it applies, explains it as “testing small changes and keeping only those that demonstrate improvement,” and asks only for material decisions or authorization.

## Entry conditions

Before the first attempt, establish:

- an observed baseline or an explicit reason why none can be obtained;
- a concrete gap and testable hypothesis;
- validation and an acceptance criterion defined before the change;
- a bounded mutable area and evaluation protected from opportunistic alteration;
- a safe way to restore the best validated state;
- a budget or stopping condition compatible with granted authority.

If a material condition is missing, use `BLOCKED`, `DECISION_REQUIRED` or `AUTHORITY_REQUIRED`; do not pretend the attempts are comparable.

## Loop

1. Confirm the best validated state and its evidence.
2. Select one hypothesis or a minimum inseparable set.
3. Predeclare the change, validation, criterion, risks and restoration method.
4. Apply the smallest authorized reversible change.
5. Run validation without weakening it to favor the attempt.
6. Compare against the baseline, every mandatory criterion and possible regressions.
7. Issue a verdict:
   - `KEEP`: sufficient improvement with no unacceptable regression; it becomes the best validated state.
   - `REVISE`: promising but insufficient evidence; it is not yet validated.
   - `DISCARD`: no improvement, disproportionate complexity or a regression; restore.
   - `CRASH`: the attempt could not run because of an internal failure; restore.
   - `BLOCKED`: an external dependency prevents evaluation.
   - `ESCALATE`: continuation requires a new decision or authority.
8. Record evidence, learning, final state and next route.
9. Continue automatically only within the authorized scope, risk and budget.

A failed attempt may produce learning, but must not contaminate the best validated state. Never erase the record to present an artificially clean sequence.

## Review

When an independent Reviewer exists, inspect the actual change and also verify comparability, validation integrity, regressions, complexity cost and restoration. A Builder's own claim does not constitute approval.

When a work map is active, every material finding must identify the direct outcome, failed or missing evidence, and potentially affected dependents. A `KEEP` does not automatically preserve descendant outcomes: revalidate them when dependency or impact requires it.

Apply the degraded compatibility in `../01_core/OPERATING_CONTRACT.md` when the platform cannot provide independence. Deterministic self-tests do not become independent review.

## Simplicity and stopping

For equivalent outcomes, prefer the simpler and more maintainable option. A marginal improvement does not justify disproportionate complexity, cost or risk.

Stop on goal achievement, exhausted budget, diminishing returns, lost comparability, new risk, material contradiction, new authority requirement or user intervention. Autonomy is not permission to operate indefinitely.
