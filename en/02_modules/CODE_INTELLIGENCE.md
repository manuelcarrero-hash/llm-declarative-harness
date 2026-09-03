# Module: Code Intelligence

## Purpose

Reduce isolated changes and regressions caused by treating a repository as a collection of files. Before a material technical change, the agent builds a sufficient, supported view of the affected surface: entry points, symbols, calls, data, dependencies, tests and service boundaries. Depth must be proportional to risk; this module does not require indexing the whole repository.

The person describes the change in plain language. The agent selects tools internally and communicates only what may be affected, what was verified, what remains uncertain and how the change will be tested.

## Activation

Activate when:

- code or architecture changes and impact may extend beyond the target file;
- the repository is unfamiliar, medium-sized or large;
- connected routes, services, data or repositories exist;
- a previous fix caused regressions or component relationships are uncertain;
- the Reviewer needs to verify indirect impact.

Do not activate as ceremony for a local, reversible, low-risk edit with an evident boundary. Do not claim complete understanding after inspecting only part of the system.

## Proportional levels

- **BASIC:** direct search and reading of relevant files; suitable for local changes with evident dependencies.
- **STRUCTURAL:** bounded map of entry points, modules, symbols, tests and dependencies; default for material changes.
- **DEEP:** call graph, data flow, cross-service or cross-repository links and tool-assisted impact analysis; use only when complexity and available capability justify it.

The level describes required evidence, not a specific tool.

## Protocol

### 1. Identity and rules

Confirm repository, branch, commit or workspace state and applicable rules. Separate confirmed code, documentation, tool results and inference.

### 2. Bound the question

Define the behavior to change and the initial surface. Do not explore the entire repository by inertia.

### 3. Reconstruct the affected surface

Identify as relevant:

- entry points and routes;
- modified symbols and their callers or consumers;
- contracts, types, schemas and persistence;
- side effects, asynchronous work and integrations;
- existing tests and related user surfaces;
- boundaries among packages, services or repositories.

Record only supported relationships. A text match does not prove a dependency, and a tool does not prove exhaustiveness.

### 4. Classify certainty

Classify every material relationship with the Operating Contract factual taxonomy. Existing dependencies normally use `CONFIRMED`, `CORROBORATED`, `INFERRED` or `UNKNOWN`; `REPORTED` and `PLANNED` do not demonstrate a current dependency. An `INFERRED` or `UNKNOWN` relationship capable of invalidating the change must be resolved, bounded or escalated before execution.

### 5. Analyze impact

Produce an internal short note containing:

- direct surface;
- potential dependents;
- tests and flows to repeat;
- uncertainties and exclusions;
- applied level, tools and evidence freshness.

When Team's work map exists, link only affected outcomes without confusing code dependencies with management dependencies.

### 6. Implement and verify

Change only within the authorized boundary. Afterwards:

- inspect the diff and affected symbols;
- run relevant tests and, when a real surface exists, exercise critical flows;
- check for broken dependencies, orphaned routes or out-of-scope changes;
- update durable status only with useful conclusions and evidence, not a graph dump.

## Optional structural tools

When the platform provides code intelligence, semantic search, LSP, indexes or graphs —for example Codebase Memory MCP— use them as accelerators for architecture, calls and impact. Verify availability and freshness. Apply the authority and sensitive-data limits in `../01_core/AUTHORITY_AND_SAFETY.md`; tool availability does not authorize installation, configuration, persistent services or external code transfer.

When unavailable, apply the possible level through search, reading, manifests, tests and local tools. Disclose the degradation. The harness remains functional and never depends on a particular provider, MCP server or product.

## Boundaries

- An index does not replace PROJECT_STATUS, Git, tests or human review.
- Static analysis may miss reflection, generated code, dynamic configuration and runtime effects.
- Do not present vendor metrics, declared coverage or token savings as observed results.
- Do not preserve secrets, complete code or bulky output in project status.

## Minimum observable output

To credit the module, evidence must include: applied level, identity of inspected code, direct surface, relevant dependents, certainty of material relationships, selected tests or flows, uncertainties and post-change evidence. Naming a tool or claiming the repository was analyzed is insufficient.
