# Module: Context Continuity

Protect decisions, evidence, partial state and the next action when work crosses agents, sessions, compaction or phases.

## Thresholds

Use percentages only when real telemetry exists and total capacity is known. Default policy: preventive checkpoint at a measured 30% and rotation at a measured 40%. Without telemetry, use qualitative signals and declare the percentage unknown.

At each relevant checkpoint, update or link the operational pulse: phase, delivery states, latest check, risk, continuity state and next action. Label the source and freshness of every runtime signal. `UNKNOWN` is not a failure; invented precision is.

## Rotation

Reach a safe atomic boundary; write a handoff; verify it against sources; synchronize authorized state; start the successor with minimum context; require a handshake before editing; relieve the predecessor only after the handshake.

Do not pretend that a session was stopped or created when the platform does not support it.
