# Guided start

This protocol turns a simple request into a verifiable startup. It is declarative: a compatible platform interprets it, but the harness does not itself provide tools, memory, permissions or automation.

## Entry modes

- `NEW`: start a project and create durable state when authorized.
- `RESUME`: locate, reconcile and resume the existing authoritative state.
- `VERIFY`: check in read-only mode whether the outcome truly satisfies its completion criteria.

Copy-ready instructions and a guided interface are equivalent entries into the same protocol. They must not produce different rules, modules or completion criteria.

## Three pillars

1. Ask in plain language what the person wants to achieve and what observable result would prove completion.
2. Ask whether project state already exists and where it is. If it does not exist or the person does not know where to store it, recommend only locations the platform can actually use.
3. Evaluate environment capabilities with evidence. This assessment belongs to the agent, not the user. Ask only when a capability remains `UNKNOWN`, more than one source may be authoritative or authorization is required.

Do not ask the user to complete YAML, Markdown, manifests, technical paths or manual module selection. The agent translates the answers into the harness contract.

## Normative sequence

1. Resolve `NEW`, `RESUME` or `VERIFY` from the request; ask only when intent is ambiguous.
2. Identify the project, environment and sources already available without probing outside scope.
3. Resolve the objective and observable completion criteria. In `RESUME`, preserve the existing objective unless evidence shows that it is missing, changed or contradictory.
4. Locate authoritative state. If several candidates exist, compare identity, scope, source, freshness and evidence; do not choose only by date or merge them automatically.
5. Declare capabilities with the corresponding profile. Separate status, evidence, authorization and freshness for every capability.
6. Select only modules whose `activate_when` condition is met and record the reason. Omitting a module can be the correct decision.
7. Present a plain-language startup summary containing the objective, state, relevant capabilities, modules, limits, pending authorization and first action.
8. Operate in `REPORT` until authority to create or update state is available. Group reversible, low-risk approvals when scope is clear; request separate authority to publish, deploy, merge, delete, send communications, change permissions, spend money or use secrets.
9. Execute the smallest authorized first checkpoint and preserve evidence.

## Minimum selection by mode

| Mode | Base modules | Additional activation |
| --- | --- | --- |
| `NEW` | Goal and Status | Continuity when sessions will be crossed; Governance when rules exist; Team only when separated roles improve material work |
| `RESUME` | Status and Continuity | Goal when missing or inconsistent; Governance when resumption changes a governed workspace |
| `VERIFY` | Goal and Status | Evaluator when the run or maturity is evaluated; Team only when an applicable independent review is available |

Council remains conditional on an ambiguous, costly or subjective decision. Starting, resuming or verifying does not activate it by itself.

## State rules

- Software project: prefer the authoritative repository or workspace when compatible durable writing exists.
- Document project: prefer the authoritative Drive folder or equivalent storage.
- No durable writing: provide an exportable proposal, declare `PARTIAL` and explain the minimum manual action.
- Missing state: propose reconstruction from current sources; write only in authorized `SYNC` mode.
- Contradictory state: preserve sources, present the conflict and request the minimum decision when evidence cannot resolve it.

The startup summary is a view. It does not replace or compete with `PROJECT_STATUS.md` or its equivalent as the authoritative source.

## Startup completion

Startup is ready only when mode, objective, state source, relevant capabilities, activated modules, limits, pending authority and first action are known. If any remains materially ambiguous, use `DECISION_REQUIRED`, `AUTHORITY_REQUIRED` or `BLOCKED_EXTERNAL`; do not pretend the project started.
