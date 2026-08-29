# Provider-Neutral Declarative Harness for LLMs

[English](README.md) | [Español](README.es.md)

Created by **Manuel Carrero Rojo** · MIT License · Experimental version 0.2.2

This is a beginner-friendly, provider-neutral set of instructions and templates that helps agentic LLMs manage substantial projects with clearer goals, durable state, safe handoffs, independent review and evidence-based completion.

## What problem does it solve?

Use it when an AI forgets prior decisions, loses project state between chats, says work is finished without enough proof, or when several agents need clear ownership and continuity.

It is useful for software, research, books, courses and other multi-stage projects. It is unnecessary for short questions, simple writing or low-risk one-turn tasks.

## Start here

- Non-technical users: read [`en/START_HERE_NO_TECHNICAL_KNOWLEDGE.md`](en/START_HERE_NO_TECHNICAL_KNOWLEDGE.md).
- Agentic LLMs: read [`en/00_READ_ME_FIRST.md`](en/00_READ_ME_FIRST.md), then [`en/HARNESS_MANIFEST.yaml`](en/HARNESS_MANIFEST.yaml).
- Common protocol to start, resume or verify: [`en/01_core/GUIDED_START.md`](en/01_core/GUIDED_START.md).
- Spanish version: read [`EMPIEZA_AQUI_SIN_CONOCIMIENTOS_TECNICOS.md`](EMPIEZA_AQUI_SIN_CONOCIMIENTOS_TECNICOS.md).
- Non-code example: read [`en/05_examples/NON_CODE_BOOTSTRAP.md`](en/05_examples/NON_CODE_BOOTSTRAP.md).
- Evaluation controls: read [`en/06_validation/CONTROL_CATALOG.md`](en/06_validation/CONTROL_CATALOG.md).
- Translation policy: see [`en/BILINGUAL_PARITY.md`](en/BILINGUAL_PARITY.md).
- Release history: see [`CHANGELOG.md`](CHANGELOG.md).

This repository defines a declarative operating protocol, not an autonomous runtime. It does not give a model tools, memory, subagents, permissions or context telemetry that its platform does not provide.

Guided start asks in plain language what the person wants to achieve and where state should be preserved. The LLM must verify its own capabilities, select only necessary modules, explain limits and authorizations and begin with the smallest authorized checkpoint; the person does not configure technical files.

For difficult decisions, the optional Council module collects independent perspectives, cross-reviews anonymized proposals and produces a reasoned synthesis. It does not treat voting as proof or grant authority to act.

Council files: [`en/02_modules/COUNCIL.md`](en/02_modules/COUNCIL.md) and [`en/03_templates/COUNCIL_BRIEF.template.md`](en/03_templates/COUNCIL_BRIEF.template.md).

The operational pulse provides a short view of what is implemented, checked or pending and the exact next action. It may show telemetry only when the platform exposes it; unavailable data remains explicitly unknown. Template: [`en/03_templates/OPERATIONAL_PULSE.template.md`](en/03_templates/OPERATIONAL_PULSE.template.md).

Copyright (c) 2026 Manuel Carrero Rojo.
