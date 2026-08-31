# Module: Harness Evaluation

Evaluate real runs, not the appearance of the documents.

## Controls

Evaluate identity, guided start, authority, objective, applicable governance, evidence supporting rules, ownership, orchestration, iteration, review, state, handoff, resumption, council and closure. Score each control as `PASS`, `FAIL`, `NOT_OBSERVED` or `NOT_APPLICABLE`. Use the normative definitions in `../06_validation/CONTROL_CATALOG.md`.

For a `NEW`, `RESUME` or `VERIFY` run, compare the startup summary with the request, capability profile, real state, activated modules and approvals. A plain explanation does not prove that selection or authority was correct.

A failed critical control makes the run unreliable. An unobserved critical control prevents a strong conclusion. Agent self-evaluation does not replace independent evidence.

If an operational pulse exists, compare it with the underlying sources. An exact context, cost, limit or runtime value requires direct current telemetry. A compact display does not prove its own accuracy; presenting inference as measurement affects control `STATE_01`.

When Team is active, `ORCHESTRATION_01` requires justified applicability, proportional level, non-redundant assignments, verifiable artifacts, integration and additional waves supported by observed gaps. More agents do not demonstrate better orchestration.

When Iteration is active, `ITERATION_01` requires evidence of the best validated state, prior criterion, verdict, and restoration or incorporation. A Builder-authored log does not by itself prove comparison or restoration.

When a work map is used to preserve outcomes or resume partially, `DEPENDENCY_01` requires proportional activation, supported dependencies, findings linked to impact, current evidence and a valid frontier. The map does not prove its own accuracy; ambiguity must widen reverification.

Record whether council was applicable, activated, and backed by separate agents or explicit degradation. `COUNCIL_01` may be `NOT_APPLICABLE` only when the decision did not meet activation criteria and no council was activated.

## Maturity decisions

Use `KEEP_NATIVE`, `IMPROVE_NATIVE`, `PROTOTYPE_NARROW_AUTOMATION`, `CONSIDER_INDEPENDENT_HARNESS` or `INSUFFICIENT_EVIDENCE`. Three real runs are a minimum pilot; five provide a stronger basis. Before treating a functional version as stable, run 12–20 representative scenarios from `../06_validation/REGRESSION_SUITE.md`. Do not recommend more automation without identifying recurring friction that justifies it.
