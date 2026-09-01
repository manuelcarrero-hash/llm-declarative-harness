# Module: Agent Team

Use real roles only when the platform supports separate agents and division materially improves correctness, coverage, speed or independence. The person does not select roles, levels or agents; the Lead resolves the setup and explains it in plain language.

## Applicability test

Activate Team when at least two materially independent workstreams exist, each can produce its own evidence, and one or more of the following also applies:

- information reasonably exceeds one agent's context;
- distinct tools, sources or specialties are needed;
- parallel exploration removes material delay;
- independent review reduces meaningful risk;
- expected value justifies added cost and coordination.

Do not activate for small, highly sequential work, inseparable context, concurrent writes to the same artifact or workstreams that would only duplicate the same search. Separating Builder and Reviewer may still be required even when execution remains `SINGLE`.

## Internal effort levels

- `SINGLE`: one executor or sequential flow; small or tightly dependent work.
- `FOCUSED`: normally two to four independent workstreams with bounded deliverables.
- `BROAD`: extensive research or verification across many sources, tools or contexts; requires a budget and stronger traceability.

Start with the smallest sufficient level. Ranges are heuristics, not quotas. More agents require a concrete gap; availability does not prove need.

## Minimum roles

- **Lead:** contract, authority, strategy, budget, integration and closure.
- **Builder / Worker:** bounded execution, evidence and own artifact.
- **Reviewer:** independent inspection of the contract and actual change; verdict `APPROVED` or `CHANGES_REQUIRED`. When Iteration is active, also verify baseline, comparability, validation integrity, regressions, complexity cost and restoration.

Add QA, security, design, research or evidence review only when a useful boundary exists. One agent performing several personas does not prove independence.

## Pre-execution review contract

When a material change requires an independent Reviewer, that Reviewer must inspect before execution: expected outcome, confirmed material decisions, observable behaviors, evidence, critical flows, rejection thresholds and unauthorized actions. The Builder proposes how to demonstrate `Done`; the Reviewer identifies insufficient coverage, untestable criteria or incentives to approve incomplete work. The Lead resolves disagreement without expanding scope or replacing a decision reserved to the user.

Do not require this negotiation for small tasks or when the platform cannot provide independence. In that case, apply proportional pre-delivery review and disclose the degradation. The technical agreement stays internal unless it exposes a material decision for the person.

## QA on the real artifact

When an executable or interactive artifact exists and tools are available, the Reviewer must exercise critical flows through the same surface the person would use and verify observable effects across relevant layers. Reading the diff, inspecting a static screenshot, confirming that a function exists or accepting the Builder's report is insufficient. Record flow, action, expected result, observed result and evidence.

When the real surface is unavailable, declare `PARTIAL` and run the best substitute without presenting it as end-to-end proof. Every mandatory criterion has its own rejection threshold: visual, technical or narrative strength does not compensate for failure of a core function.

## Delegation in waves

1. Bound non-redundant workstreams and assign the minimum first wave.
2. Use `../03_templates/AGENT_ASSIGNMENT.template.md` for every material workstream.
3. Avoid concurrent writes to the same file and declare exclusions among agents.
4. Receive status, evidence, artifact, gaps and uncertainties.
5. Integrate and check coverage before opening another wave.
6. Create a second wave only for an observed gap, never by inertia.

Each assignment must include objective, exact question, boundary, included and excluded scope, preferred sources or tools, unauthorized actions, format, evidence, artifact, completion condition, stop condition and budget.

## Dependencies among outcomes

When at least three material outcomes exist, an observable dependency connects them and changing one may affect another's validity, internally generate `../03_templates/WORK_MAP.template.md`. The Lead maintains outcomes, dependencies, artifacts and evidence; the person does not draw the map or configure relationships.

The map is derived and disposable: it does not replace artifacts or authoritative state. Record only supported dependencies. When a relationship is ambiguous or unverifiable, do not use the map to preserve work without renewed validation.

## Artifacts and fidelity

When compatible durable writing exists, the specialist agent preserves its result directly and returns a lightweight reference to the Lead. The Lead integrates by reference and does not unnecessarily rewrite source content. Without durable writing, disclose the degradation and preserve structured output in the available medium.

For material teams, audits or incidents, use `../03_templates/ORCHESTRATION_TRACE.template.md`. Record operating facts, never chain of thought.
