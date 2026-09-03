# Guided start

This protocol turns a simple request into a verifiable startup. It is declarative: a compatible platform interprets it, but the harness does not itself provide tools, memory, permissions or automation.

## Entry modes

- `NEW`: start a project and create durable state when authorized.
- `RESUME`: locate, reconcile and resume the existing authoritative state.
- `VERIFY`: check in read-only mode whether the outcome truly satisfies its completion criteria.

Copy-ready instructions and a guided interface are equivalent entries into the same protocol. They must not produce different rules, modules or completion criteria.

The universal instruction in `START_HERE.md` is the preferred human entry. The three specific instructions remain alternatives and examples, not decisions the user must understand.

## Load gate

Before asking questions, the agent must read the manifest, report the exact observed version, and cite the file from which it obtained that value. It may then ask the minimum necessary questions. Before any material action it must present the complete receipt in `03_templates/LOAD_RECEIPT.template.md` using no more than five blocks.

If it cannot access the harness, cannot find the manifest, or cannot confirm the version, it must stop. It may not replace reading with prior knowledge, infer a version from a folder name, or claim it applied modules it did not read. It must explain the smallest manual action required to grant access.

## Three pillars

1. Ask in plain language what the person wants to achieve and what observable result would prove completion.
2. Ask whether project state already exists and where it is. If it does not exist or the person does not know where to store it, recommend only locations the platform can actually use.
3. Evaluate environment capabilities with evidence. This assessment belongs to the agent, not the user. Ask only when a capability remains `UNKNOWN`, more than one source may be authoritative or authorization is required.

Do not ask the user to complete YAML, Markdown, manifests, technical paths or manual module selection. The agent translates the answers into the harness contract.

## Normative sequence

1. Satisfy the load gate and resolve `NEW`, `RESUME` or `VERIFY` from the universal request; ask only when intent is ambiguous.
2. Identify the project, environment and sources already available without probing outside scope.
3. Resolve the objective and observable completion criteria. If the person names alternatives, examples or broad references that would materially change the outcome, ask one decisive question or recommend an option and wait for confirmation; do not choose silently. In `RESUME`, preserve the existing objective unless evidence shows that it is missing, changed or contradictory.
4. Locate authoritative state. If several candidates exist, compare identity, scope, source, freshness and evidence; do not choose only by date or merge them automatically.
5. Declare capabilities with the corresponding profile. Separate status, evidence, authorization and freshness for every capability.
6. Select only modules whose `activate_when` condition is met and record the reason. Omitting a module can be the correct decision.
7. Present the startup receipt in plain language with the objective, state, relevant capabilities, modules, limits, pending authorization and first action, within five visible blocks.
8. Operate in `REPORT` until authority to create or update state is available. Group reversible, low-risk approvals when scope is clear; request separate authority to publish, deploy, merge, delete, send communications, change permissions, spend money or use secrets.
9. Before the first checkpoint, identify and close material premises that could invalidate the outcome according to `OPERATING_CONTRACT.md`.
10. Execute the smallest authorized first checkpoint, apply pre-delivery review and preserve evidence.

## Interaction and evidence discipline

- Use `COMPACT` by default: each visible receipt or checkpoint should normally fit within 250 words and show only decisions, critical evidence, uncertainty, pending authority and the next action. Use `AUDITABLE` only when the person requests it or an audit requires expanded traceability.
- Continue automatically between already authorized checkpoints. Stop only for a decision that materially changes scope, an unresolved contradiction, a new risk or an action requiring additional authority. Do not ask for “continue” or “go ahead” without a real decision.
- Do not claim a module was applied merely because it was named or read. Each activated module must produce minimum observable evidence: Goal, outcome and `Done`; Status, location, durability, current decisions, continuity and next action; research, sources and material exclusions; evidence, fact, source, inference and confidence; voice, concrete patterns derived from references; Team, applicability, level, workstreams and artifacts; Council, brief, perspectives and synthesis; Iteration, baseline, predeclared criterion, verdicts and restoration.
- Do not declare a capability by inference. Demonstrate it with a current verifiable action or mark it `UNKNOWN`, `PARTIAL` or `UNSUPPORTED`.
- For work dependent on current facts, do not draft the deliverable until source selection and evidence sufficiency are closed. The load receipt does not close research.
- Always distinguish prior project state, reusable materials and style or format references. One does not imply the others.
- Treat memory and previous projects as provenance-bearing background, not facts of the current assignment. Confirm before reusing topics, cases, style, decisions or data that materially change the outcome.
- Keep module names, restrictions and internal architecture internal unless the person requests an auditable view. The final deliverable must use the natural format of the work, not render harness instructions as content.
- On mobile interfaces avoid wide tables. Present matrices as cards or compact lists unless the person requests tabular format.

## Minimum selection by mode

| Mode | Base modules | Additional activation |
| --- | --- | --- |
| `NEW` | Goal and Status | Governance when rules exist; Team only when independent workstreams exist and benefit justifies coordination; the agent selects the level |
| `RESUME` | Status | Goal when missing or inconsistent; Governance when resumption changes a governed workspace |
| `VERIFY` | Goal and Status | Evaluator when the run or maturity is evaluated; Team only when material verification contains independent workstreams, benefits from separated roles and required capabilities are available |

Council remains conditional on an ambiguous, costly or subjective decision. Starting, resuming or verifying does not activate it by itself.

## State rules

- Software project: prefer the authoritative repository or workspace when compatible durable writing exists.
- Document project: prefer the authoritative Drive folder or equivalent storage.
- No durable writing: provide an exportable proposal, declare `PARTIAL` and explain the minimum manual action.
- Missing state: propose reconstruction from current sources; write only in authorized `SYNC` mode.
- Contradictory state: preserve sources, present the conflict and request the minimum decision when evidence cannot resolve it.

The startup receipt is a view. It does not replace or compete with `PROJECT_STATUS.md` or its equivalent as the authoritative source.

`REPORT` and `SYNC` classify only inspection or writing of project state. They do not grant or revoke authority to modify other artifacts or perform external actions; those actions are governed by their authorized scope and `AUTHORITY_AND_SAFETY.md`.

## Startup completion

Startup is ready only when mode, objective, state source, relevant capabilities, activated modules, limits, pending authority and first action are known. If any remains materially ambiguous, use `DECISION_REQUIRED`, `AUTHORITY_REQUIRED` or `BLOCKED_EXTERNAL`; do not pretend the project started.
