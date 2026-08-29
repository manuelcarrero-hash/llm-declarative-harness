# Provider-Neutral Declarative Harness for LLMs

[English](README.md) | [Español](README.es.md)

Created by **Manuel Carrero Rojo** · MIT License · Experimental version 0.1.0

This is a beginner-friendly, provider-neutral set of instructions and templates that helps agentic LLMs manage substantial projects with clearer goals, durable state, safe handoffs, independent review and evidence-based completion.

## What problem does it solve?

Use it when an AI forgets prior decisions, loses project state between chats, says work is finished without enough proof, or when several agents need clear ownership and continuity.

It is useful for software, research, books, courses and other multi-stage projects. It is unnecessary for short questions, simple writing or low-risk one-turn tasks.

## Start here

- Non-technical users: read [`en/START_HERE_NO_TECHNICAL_KNOWLEDGE.md`](en/START_HERE_NO_TECHNICAL_KNOWLEDGE.md).
- Agentic LLMs: read [`en/00_READ_ME_FIRST.md`](en/00_READ_ME_FIRST.md), then [`en/HARNESS_MANIFEST.yaml`](en/HARNESS_MANIFEST.yaml).
- Spanish version: read [`EMPIEZA_AQUI_SIN_CONOCIMIENTOS_TECNICOS.md`](EMPIEZA_AQUI_SIN_CONOCIMIENTOS_TECNICOS.md).

This repository defines a declarative operating protocol, not an autonomous runtime. It does not give a model tools, memory, subagents, permissions or context telemetry that its platform does not provide.

## Quick prompt

> I want to use this harness for a project. Read `en/00_READ_ME_FIRST.md` and `en/HARNESS_MANIFEST.yaml`. Explain in plain language which capabilities your platform actually supports. Do not assume unavailable capabilities. Then help me configure the project without overwriting existing files or taking unauthorized actions.

Copyright (c) 2026 Manuel Carrero Rojo.
