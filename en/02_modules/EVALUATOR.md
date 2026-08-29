# Module: Harness Evaluation

Evaluate real runs, not the appearance of the documents.

## Controls

Evaluate identity, objective, applicable governance, evidence supporting rules, ownership, review, state, handoff, resumption and closure. Score each control as `PASS`, `FAIL`, `NOT_OBSERVED` or `NOT_APPLICABLE`. Use the normative definitions in `../06_validation/CONTROL_CATALOG.md`.

A failed critical control makes the run unreliable. An unobserved critical control prevents a strong conclusion. Agent self-evaluation does not replace independent evidence.

If an operational pulse exists, compare it with the underlying sources. An exact context, cost, limit or runtime value requires direct current telemetry. A compact display does not prove its own accuracy; presenting inference as measurement affects control `STATE_01`.

## Maturity decisions

Use `KEEP_NATIVE`, `IMPROVE_NATIVE`, `PROTOTYPE_NARROW_AUTOMATION`, `CONSIDER_INDEPENDENT_HARNESS` or `INSUFFICIENT_EVIDENCE`. Three real runs are a minimum pilot; five provide a stronger basis. Do not recommend more automation without identifying recurring friction that justifies it.
