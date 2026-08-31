# Module: Context Continuity

Protect decisions, evidence, partial state, artifacts and the next action when work crosses agents, sessions, compaction, failures or phases.

## Thresholds

Use percentages only when real telemetry and total capacity are known. Default policy: preventive checkpoint at a measured 30% and rotation at a measured 40%. Without telemetry, use qualitative signals and report the percentage as unknown.

At every relevant checkpoint, update or link the operational pulse: phase, delivery states, latest check, risk, continuity state and next action. Label the source and freshness of every runtime signal. `UNKNOWN` is not a failure; invented precision is.

## Artifacts across agents

When the platform supports it, each agent stores its material output directly in the durable workspace and gives the successor or Lead a reference, status, evidence, gaps and uncertainties. Do not route full artifacts through repeated summaries when they can be preserved at source.

The recipient must read the authoritative artifact when a summary could lose precision. A broken reference or unverifiable artifact is not a complete handoff.

## Failure and resumption

Apply the retry taxonomy and budget in `../01_core/OPERATING_CONTRACT.md`. Before restarting costly work, preserve the last safe checkpoint, observable cause, attempts made and next alternative. Resume from the checkpoint; do not start over unless evidence shows corruption or incompatibility.

## Rotation

Reach a safe atomic boundary; write a handoff; verify it against sources; synchronize authorized state; start a successor with minimum context; require a handshake before editing; release the prior agent only after the handshake.

Do not pretend to stop, persist, resume or create a session when the platform cannot do so.
