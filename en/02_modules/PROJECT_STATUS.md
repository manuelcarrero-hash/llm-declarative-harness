# Module: Project Status

Maintain one authoritative snapshot that answers: what was done, where are we, what comes next and where are we going?

## Modes

- `REPORT`: inspect and report without writing.
- `SYNC`: create or update only with explicit authorization.

## Minimum content

Project identity, timestamp and anchors; validated work; current position; risks and decisions; next action; gates; destination and success criteria. When a work map is active, link it and record its resumption frontier without duplicating its detail. Resolve contradictions using the newest and most direct evidence without erasing intentional decisions.

## Resumption frontier

A frontier may preserve already verified outcomes only when their evidence remains current, their dependencies are known and no later change affects their validity. Record what is preserved, what is invalidated, the exact resumption point and supporting evidence.

The map is a derived view, not a second source of truth. When dependencies are absent, ambiguous, divergent or unverifiable, invalidate conservatively and repeat the applicable validation.

## Operational pulse

When it helps resumption or decision-making, lead with the compact view in `../03_templates/OPERATIONAL_PULSE.template.md`. It is a view of authoritative status, not a second source of truth.

Include optional telemetry only when a current source exposes it directly. Label each signal `OBSERVED`, `REPORTED`, `INFERRED`, `PLANNED` or `UNKNOWN`, with its source and freshness. Use `UNAVAILABLE` only when the capability is `UNSUPPORTED`. Do not turn message count, elapsed time, output volume or intuition into exact percentages, costs or limits.
