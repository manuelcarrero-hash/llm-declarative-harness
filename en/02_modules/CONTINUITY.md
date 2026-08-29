# Module: Context Continuity

Protect decisions, evidence, partial state and the next action when work crosses agents, sessions, compaction or phases.

## Thresholds

Use percentages only when real telemetry exists and total capacity is known. Default policy: preventive checkpoint at a measured 30% and rotation at a measured 40%. Without telemetry, use qualitative signals and declare the percentage unknown.

## Rotation

Reach a safe atomic boundary; write a handoff; verify it against sources; synchronize authorized state; start the successor with minimum context; require a handshake before editing; relieve the predecessor only after the handshake.

Do not pretend that a session was stopped or created when the platform does not support it.
