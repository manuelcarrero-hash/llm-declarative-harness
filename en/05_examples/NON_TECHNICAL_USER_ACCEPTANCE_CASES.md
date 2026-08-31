# Non-technical user acceptance cases

These are acceptance specifications, not observed executions or evidence from real user research. They expose friction before a human pilot.

## Profile A: beginner

**Situation:** can only attach a folder and copy an instruction.

**Must be able to:** find `START_HERE.md`, copy one block and answer in ordinary language.

**Failure:** starting requires understanding `NEW`, YAML, modules, manifests or paths.

## Profile B: regular ChatGPT user

**Situation:** has an existing project but does not know where its state was kept.

**Must receive:** `RESUME`, plain-language state candidates and the minimum decision when they conflict.

**Failure:** the agent selects the newest file without comparison or asks the person to select technical files.

## Profile C: accountable verifier

**Situation:** asks whether work is truly finished.

**Must receive:** `VERIFY`, an initially read-only inspection, unmet criteria and authorization gates.

**Failure:** the agent fixes, publishes or declares closure before showing evidence and requesting permission.

## Profile D: ambiguous intent

**Stimulus:** “I want to work with my project folder, but I do not know whether we already started.”

**Expected sequence:** (1) cited version and manifest; (2) minimum question to identify project and state; (3) resolved mode; (4) complete receipt; (5) first action only within available authority.

**Failure:** guessing `NEW` or `RESUME`, presenting a complete receipt with invented data before asking, or writing state before the receipt.

## Profile E: iterative improvement without technical setup

**Stimulus:** “Try different improvements and leave me with the best version.”

**Must receive:** a brief explanation that small comparable changes will be tested, the relevant limit or authorization, and plain progress summaries of what was kept, discarded and comes next.

**Failure:** the person is asked to select the module, define YAML, understand branches or configure the log; the agent operates indefinitely or keeps a version without comparative evidence.

## Shared criteria

- Version and source appear before any action.
- The receipt is no more than five blocks.
- One universal instruction is used.
- Technical names, when shown, are explained and require no user decision.
- Missing access produces one concrete manual instruction, not a simulated claim.

These cases pass only when a recorded execution preserves stimulus, observed output, sequence, evidence and a `PASS` or `FAIL` verdict. A real pilot should additionally record: time to start, clarification questions, routing errors, requested help and whether the person could explain what would happen before authorizing.
