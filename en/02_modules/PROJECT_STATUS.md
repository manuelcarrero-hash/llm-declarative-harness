# Module: Project Status

Maintain one authoritative snapshot that answers: what was done, where are we, what comes next and where are we going? This module also governs continuity, checkpoints, handoffs and resumption when work crosses agents, sessions, compaction, failures or phases.

## Modes

- `REPORT`: inspect and report without writing.
- `SYNC`: create or update only with explicit authorization.

## Minimum content

Project identity, timestamp and anchors; validated work; current position; risks and decisions; next action; gates; destination and success criteria. Separate confirmed facts of the current assignment, background from memory or prior projects, reusable materials, style references and proposals not yet accepted. When a work map is active, link it and record its resumption frontier without duplicating its detail. Resolve contradictions using the newest and most direct evidence without erasing intentional decisions.

Do not elevate an interpretation, topic, case, datum or preference chosen by the agent into confirmed fact. Use the factual taxonomy in `../01_core/OPERATING_CONTRACT.md`. Before persisting an `INFERRED` or `PLANNED` item that materially changes future work, obtain confirmation or preserve it explicitly as pending. A later correction must also repair contaminated state and leave a brief trace of the change.

## Resumption frontier

A frontier may preserve already verified outcomes only when their evidence remains current, their dependencies are known and no later change affects their validity. Record what is preserved, what is invalidated, the exact resumption point and supporting evidence.

The map is a derived view, not a second source of truth. When dependencies are absent, ambiguous, divergent or unverifiable, invalidate conservatively and repeat the applicable validation.

## Operational pulse

When it helps resumption or decision-making, lead with the compact view in `../03_templates/OPERATIONAL_PULSE.template.md`. It is a view of authoritative status, not a second source of truth.

Include optional telemetry only when a current source exposes it directly. Classify each signal with the Operating Contract factual taxonomy, source and freshness. Use `UNAVAILABLE` only when the capability is `UNSUPPORTED`. Do not turn message count, elapsed time, output volume or intuition into exact percentages, costs or limits.

## Checkpoints and artifacts

Use percentages only with real telemetry and known total capacity. Default policy: preventive checkpoint at a measured 30% and rotation at a measured 40%; without telemetry, use qualitative signals and keep percentage `UNKNOWN`.

At every relevant checkpoint, update or link the operational pulse. When durable writing exists, each agent preserves material output at source and returns a reference, status, evidence, gaps and uncertainties. The recipient reads the authoritative artifact when synthesis may lose precision; a broken or unverifiable reference does not complete a handoff.

## Failure, resumption and rotation

Apply the Operating Contract retry taxonomy and budget. Before restarting costly work, preserve the last safe checkpoint, observable cause, attempts and next alternative. With an active map, traverse only supported dependencies and revalidate affected descendants; do not restart from zero unless corruption, incompatibility or demonstrated absence of a safe point requires it.

To rotate: reach a safe atomic boundary, write and verify the handoff, synchronize authorized state, start the successor with minimum context and require a handshake before editing. Do not claim persistence, resumption, stopping or session creation that the platform cannot demonstrate.
