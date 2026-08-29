# Module: Context Continuity

Preserve decisions, evidence, partial state and the next action across agents, sessions, compaction or phases.

Use percentages only with real telemetry and a known context window. Default: preventive checkpoint at 30% measured use and rotation at 40%. Without telemetry, use qualitative signals and report usage as unknown.

Rotate at a safe atomic boundary; write and verify a handoff; sync authorized state; brief the successor with minimal context; require a resume handshake before edits. Do not pretend to stop or create sessions when the platform cannot.
