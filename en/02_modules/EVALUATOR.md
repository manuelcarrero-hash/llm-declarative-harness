# Module: Harness Evaluation

Evaluate real runs, not the appearance of the documents.

## Controls

Evaluate identity, guided start, authority, objective, applicable governance, evidence supporting rules, ownership, orchestration, iteration, review, calibration, state, handoff, resumption, council and closure. Score each control as `PASS`, `FAIL`, `NOT_OBSERVED` or `NOT_APPLICABLE`. Use the normative definitions in `../06_validation/CONTROL_CATALOG.md`.

For a `NEW`, `RESUME` or `VERIFY` run, compare the startup summary with the request, capability profile, real state, activated modules and approvals. A plain explanation does not prove that selection or authority was correct.

A failed critical control makes the run unreliable. An unobserved critical control prevents a strong conclusion. Agent self-evaluation does not replace independent evidence.

If an operational pulse exists, compare it with the underlying sources. An exact context, cost, limit or runtime value requires direct current telemetry. A compact display does not prove its own accuracy; presenting inference as measurement affects control `STATE_01`.

When Team is active, `ORCHESTRATION_01` requires justified applicability, proportional level, non-redundant assignments, verifiable artifacts, integration and additional waves supported by observed gaps. More agents do not demonstrate better orchestration.

When Iteration is active, `ITERATION_01` requires evidence of the best validated state, prior criterion, verdict, and restoration or incorporation. A Builder-authored log does not by itself prove comparison or restoration.

When a material change requires a Reviewer, verify that the review contract was inspected before execution and that critical flows were exercised on the real artifact when capability existed. A global approval cannot compensate for a failed mandatory criterion.

When a work map is used to preserve outcomes or resume partially, `DEPENDENCY_01` requires proportional activation, supported dependencies, findings linked to impact, current evidence and a valid frontier. The map does not prove its own accuracy; ambiguity must widen reverification.

Record whether council was applicable, activated, and backed by separate agents or explicit degradation. `COUNCIL_01` may be `NOT_APPLICABLE` only when the decision did not meet activation criteria and no council was activated.

## Reviewer calibration

Activate calibration when a person corrects a material Reviewer verdict, when the Reviewer minimizes a failure the person considers blocking, or when its scores repeatedly diverge from declared human judgment. Record the case in `../03_templates/REVIEWER_CALIBRATION.template.md`: initial verdict, human correction, observable cause, minimum adjustment, cases that must not change and independent revalidation.

Do not turn one isolated preference into a universal rule. The adjustment becomes `CALIBRATED` only after another relevant run passes without degrading previously valid cases. The person does not fill in the record; the agent captures only the necessary decision and evidence.

## Harness reassessment

When the model or platform changes significantly, or an expensive component stops showing benefit, reassess harness assumptions on realistic cases. Remove or degrade a component only after comparing a baseline and changing one variable at a time; do not confuse greater model capability with demonstrated compliance. Preserve the simplest solution that maintains critical controls.

## Maturity decisions

Use `KEEP_NATIVE`, `IMPROVE_NATIVE`, `PROTOTYPE_NARROW_AUTOMATION`, `CONSIDER_INDEPENDENT_HARNESS` or `INSUFFICIENT_EVIDENCE`. Three real runs are a minimum pilot; five provide a stronger basis. Before treating a functional version as stable, run 12–20 representative scenarios from `../06_validation/REGRESSION_SUITE.md`. Do not recommend more automation without identifying recurring friction that justifies it.
