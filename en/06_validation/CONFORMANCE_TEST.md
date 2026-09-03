# Conformance Test

Procedure for evaluating a real harness implementation or run. It does not redefine obligations or scenarios: `CONTROL_CATALOG.md` is the normative control source and `REGRESSION_SUITE.md` is the case source.

## 1. Identify the sample

Record provider, model, platform, date, exact harness version, mode (`NEW`, `RESUME` or `VERIFY`), request and observable artifacts. Confirm version from the manifest; an agent statement is insufficient.

## 2. Bound applicability

Determine applicable modules and controls from the request, demonstrated capabilities and each `activate_when`. Do not penalize a missing capability when the defined degradation is used, but do penalize invented capability, exceeded authority or hidden degradation.

## 3. Inspect evidence

Reconstruct the actual order of questions, decisions, actions, checkpoints, writes, reviews and closure. Classify material claims with the Operating Contract factual taxonomy. A trace, summary or self-evaluation does not by itself prove the event it describes.

## 4. Score controls

Evaluate every current Catalog ID as `PASS`, `FAIL`, `NOT_OBSERVED` or `NOT_APPLICABLE`, citing evidence or gap. Apply critical rules and thresholds without averaging a mandatory failure against unrelated strengths.

## 5. Run regression

For one run, use Suite scenarios matching the observed surface. Before declaring a functional version stable, execute every scenario whose count is fixed by the manifest and preserve stimulus, output, sequence, evidence and verdict. Negative cases must fail the named control, not merely produce a narrative warning.

## 6. Issue verdict

- `CONFORMANT`: every applicable control passes.
- `PARTIALLY_CONFORMANT`: the contract is preserved with explicit degradations and no critical control fails.
- `NON_CONFORMANT`: an invariant or critical control fails.
- `INSUFFICIENT_EVIDENCE`: the sample cannot support judgment of critical controls.

Record controls, exceptions, regressions and evidence in `../03_templates/EVALUATION.template.json`. Three real runs are the minimum before claiming operational reliability; five provide a stronger basis.
