# Provider-Neutral Declarative Harness for LLMs

[English](README.md) | [Español](README.es.md)

Created by **Manuel Carrero Rojo** · MIT License · Experimental version 0.10.0

**No technical background required:** open only [`EMPEZAR_AQUI.md`](EMPEZAR_AQUI.md) for Spanish or [`en/START_HERE.md`](en/START_HERE.md) for English. The remaining folders are internals for the LLM.

This is a beginner-friendly, bilingual and provider-neutral harness for starting, resuming and verifying substantial LLM projects without asking the user to configure technical files. It preserves durable state, makes capabilities and permissions visible, closes material ambiguities before production, checks critical premises and reviews each deliverable before it becomes trusted state.

For material work, an available independent Reviewer checks the validation contract before execution and exercises critical flows on the real artifact. Human corrections calibrate future review only after another relevant run confirms the adjustment; these mechanics remain internal to preserve a simple experience.

## What problem does it solve?

Use it when an AI forgets prior decisions, loses project state between chats, says work is finished without enough proof, or when several agents need clear ownership and continuity.

It is useful for software, research, books, courses and other multi-stage projects. It is unnecessary for short questions, simple writing or low-risk one-turn tasks.

## Start here

- Non-technical users: open only [`en/START_HERE.md`](en/START_HERE.md).
- Agentic LLMs: read [`en/HARNESS_MANIFEST.yaml`](en/HARNESS_MANIFEST.yaml), then its declared entrypoint, [`en/LLM_INTERNALS.md`](en/LLM_INTERNALS.md).
- Common protocol to start, resume or verify: [`en/01_core/GUIDED_START.md`](en/01_core/GUIDED_START.md).
- Spanish version: read [`EMPEZAR_AQUI.md`](EMPEZAR_AQUI.md).
- Non-code example: read [`en/05_examples/NON_CODE_BOOTSTRAP.md`](en/05_examples/NON_CODE_BOOTSTRAP.md).
- Guided-start scenarios: read [`en/05_examples/GUIDED_START_SCENARIOS.md`](en/05_examples/GUIDED_START_SCENARIOS.md).
- Evaluation controls: read [`en/06_validation/CONTROL_CATALOG.md`](en/06_validation/CONTROL_CATALOG.md) and the [`regression suite`](en/06_validation/REGRESSION_SUITE.md).
- Translation policy: see [`en/BILINGUAL_PARITY.md`](en/BILINGUAL_PARITY.md).
- Release history: see [`CHANGELOG.md`](CHANGELOG.md).

This repository defines a declarative operating protocol, not an autonomous runtime. It does not give a model tools, memory, subagents, permissions or context telemetry that its platform does not provide.

Guided start asks in plain language what the person wants to achieve and where state should be preserved. The LLM verifies its capabilities, selects only necessary modules, explains limits and authorizations and begins with the smallest authorized checkpoint; the person does not configure technical files, roles or agents.

When genuinely independent workstreams exist, Team internally scales effort as single, focused or broad, delegates in waves and preserves results in verifiable artifacts. It avoids unnecessary agents for small tasks. When several outcomes depend on one another, it may internally create a small map to identify what a finding affects, what requires renewed review and which verified work may be preserved. The person receives only a plain explanation and does not configure graphs or relationships. Internal files: [`en/02_modules/TEAM.md`](en/02_modules/TEAM.md), [`en/03_templates/AGENT_ASSIGNMENT.template.md`](en/03_templates/AGENT_ASSIGNMENT.template.md) and [`en/03_templates/ORCHESTRATION_TRACE.template.md`](en/03_templates/ORCHESTRATION_TRACE.template.md).

For material software changes, the optional Code Intelligence module reconstructs only the affected surface, classifies relationship certainty and defines which tests must be repeated. It may use indexes, LSP or graphs such as Codebase Memory MCP when already available, but retains a direct-reading path and installs no service without authorization. File: [`en/02_modules/CODE_INTELLIGENCE.md`](en/02_modules/CODE_INTELLIGENCE.md).

For difficult decisions, the optional Council module collects independent perspectives, cross-reviews anonymized proposals and produces a reasoned synthesis. It does not treat voting as proof or grant authority to act.

When work benefits from several comparable attempts, the optional Iteration module establishes a baseline, tests reversible changes, and records what is kept or discarded. The person does not configure the loop and receives only a plain summary of what was tried, the outcome and the next step. Files: [`en/02_modules/ITERATION.md`](en/02_modules/ITERATION.md) and [`en/03_templates/ITERATION_LOG.template.md`](en/03_templates/ITERATION_LOG.template.md).

Council files: [`en/02_modules/COUNCIL.md`](en/02_modules/COUNCIL.md) and [`en/03_templates/COUNCIL_BRIEF.template.md`](en/03_templates/COUNCIL_BRIEF.template.md).

The operational pulse provides a short view of what is implemented, checked or pending and the exact next action. It may show telemetry only when the platform exposes it; unavailable data remains explicitly unknown. Template: [`en/03_templates/OPERATIONAL_PULSE.template.md`](en/03_templates/OPERATIONAL_PULSE.template.md).

## Inspiration and acknowledgements

The harness was developed independently, while recognizing public ideas that influenced skills and modules later incorporated into this protocol: [`garrytan/gstack`](https://github.com/garrytan/gstack), [`mvanhorn/last30days-skill`](https://github.com/mvanhorn/last30days-skill), [`karpathy/llm-council`](https://github.com/karpathy/llm-council), [`karpathy/autoresearch`](https://github.com/karpathy/autoresearch), [`DeusData/codebase-memory-mcp`](https://github.com/DeusData/codebase-memory-mcp), Anthropic's [`How we built our multi-agent research system`](https://www.anthropic.com/engineering/multi-agent-research-system) and [`Harness design for long-running application development`](https://www.anthropic.com/engineering/harness-design-long-running-apps), the survey [`Graph Engineering in the Era of LLM Agents`](https://arxiv.org/abs/2608.21156), and LangChain's [`3 Years of Graph Engineering with LangGraph`](https://www.langchain.com/blog/3-years-of-graph-engineering-with-langgraph). See [`ACKNOWLEDGEMENTS.md`](ACKNOWLEDGEMENTS.md) for the precise scope of each influence and licensing notes.

No affiliation, sponsorship or endorsement by their authors or maintainers is implied.

Copyright (c) 2026 Manuel Carrero Rojo.
