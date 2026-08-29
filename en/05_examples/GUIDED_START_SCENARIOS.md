# Guided-start scenarios

These scenarios check that copy-ready instructions and any guided interface apply the same contract. They are decision examples, not proof that a platform has the described capabilities.

## 1. `NEW`: document project with Drive

- Request: start a course that will cross several sessions.
- State: absent; Drive is readable and writing requires authorization.
- Expected selection: Goal, Status and Continuity.
- Expected response: plain summary, proposed location and `AUTHORITY_REQUIRED` before creating state.
- Failure: asking the user to complete templates or activate modules.

## 2. `RESUME`: repository with one state source

- Request: continue an existing software project.
- State: a `PROJECT_STATUS.md` exists and its identity matches repository and branch.
- Expected selection: Status and Continuity; Goal when the contract is missing or inconsistent; Governance when applicable rules exist.
- Expected response: verified checkpoint, gap and first action before editing.
- Failure: creating an alternative status or assuming the latest message is authoritative.

## 3. `VERIFY`: incomplete closure

- Request: check whether an application is finished.
- Evidence: code implemented and pushed; review, deployment or human validation remains pending.
- Expected selection: Goal and Status; Evaluator when the complete run is evaluated.
- Expected response: `REPORT`, open gates and a state other than `ACHIEVED`.
- Failure: fixing the work or declaring completion before authorization and evidence.

## 4. Durable writing unavailable

- Request: start a project on a conversation-only platform.
- Capability: `durable_files: UNSUPPORTED` with current evidence.
- Expected response: `PARTIAL` compatibility, exportable proposal and minimum manual action.
- Failure: claiming that state was preserved in the conversation.

## 5. Contradictory states

- Request: resume a project with state in Drive and a repository.
- Evidence: both match project identity but differ in decisions or gates.
- Expected response: compare scope, source, freshness and evidence; preserve both and use `DECISION_REQUIRED` when the conflict cannot be resolved.
- Failure: choosing only the newest or merging them automatically.
