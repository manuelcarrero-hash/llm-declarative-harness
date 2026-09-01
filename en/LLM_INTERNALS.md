# LLM internals — Provider-Neutral Declarative Harness

Version: 0.8.0
Author and maintainer: Manuel Carrero Rojo

## Startup instruction

If you are a person, use only `START_HERE.md`; the rest is the harness technical interior. This file is the technical entrypoint that `HARNESS_MANIFEST.yaml` directs the agent to read after the manifest itself. If you are an agentic LLM, confirm the observed version, apply `01_core/GUIDED_START.md`, present the load receipt and activate only compatible and necessary modules.

This package defines a declarative harness: rules, contracts, states, handoffs and evaluations. It does not contain its own runtime, control the provider's inference loop or guarantee autonomous execution. A model or platform must interpret the files and provide tools, memory, agents, permissions and telemetry.

## What it is for

This harness gives an agentic LLM a consistent, verifiable and transferable way to work on complex projects. It turns coordination practices into files that any compatible model can consult without depending on a previous conversation or a specific provider.

It helps to:

- transform a broad request into an objective with scope and completion criteria;
- establish durable rules for agents working on a project;
- coordinate a lead, workers and reviewers only when independent workstreams justify the cost;
- scale effort, delegate in waves and preserve artifacts without loss through repeated summaries;
- represent dependencies among complex outcomes, localize review impact and resume only from a frontier backed by evidence;
- preserve real project state outside the context window;
- transfer work between agents or sessions through verifiable handoffs;
- prevent closure based only on model claims;
- test small reversible changes and keep only those that pass a predefined comparison;
- evaluate with evidence whether the agentic process works reliably;
- consult independent perspectives and synthesize decisions without confusing consensus with evidence;
- adapt the same framework to different models and platforms.
- close material ambiguities with the person, verify premises that could invalidate the outcome, and review the deliverable before preserving it as state.

## When to use it

Use it when work has one or more of these characteristics:

- it will span phases, sessions or context windows;
- it includes material changes to code, documents, data or architecture;
- it requires coordination among agents or roles with separated responsibilities;
- it needs operating, safety, review or completion rules;
- it must be resumable without relying on conversation memory;
- it needs traceability for decisions, tests, deployments or human validation;
- there is meaningful cost if the model declares incomplete work finished;
- you want to compare reliability across models or platforms;
- you want a repeatable process for multiple projects or users.

It can also be applied partially: for example, use only goal and status for a long project, or governance and review for a software repository.

## When not to use it

Do not use the full process when:

- the request is simple, one-turn and has no future continuity;
- explanation, summarization, translation or a short draft is enough;
- the work is a small, local, reversible and low-risk change;
- no project, durable state or coordination need exists;
- a simple task list solves the need better;
- it is expected to replace permissions, sandboxes, authentication, backups or real technical controls;
- it is expected to create autonomy, memory, agents or telemetry the platform does not provide;
- it is intended to remove human oversight from sensitive legal, financial, medical, security or production decisions;
- maintaining the artifacts would cost more than the work's risk or complexity.

Do not activate it by inertia. Use only modules that reduce a concrete risk or materially improve continuity, coordination or verifiability.

## Objective

Enable an LLM capable of acting on projects to:

1. convert intent into a verifiable objective;
2. discover rules applicable to the workplace;
3. divide and scale work without losing ownership, fidelity or authority;
4. maintain durable state outside the conversation;
5. transfer work to a clean session or agent;
6. close only with evidence;
7. evaluate process reliability across real runs.

## Reading order

1. `HARNESS_MANIFEST.yaml`
2. `LLM_INTERNALS.md` (this file)
3. `01_core/OPERATING_CONTRACT.md`
4. `01_core/AUTHORITY_AND_SAFETY.md`
5. `01_core/GUIDED_START.md`
6. Modules activated by the manifest for the task
7. Corresponding templates
8. `06_validation/CONFORMANCE_TEST.md` before claiming compatibility

## Honesty rule

Use one of these labels for every capability: `SUPPORTED`, `PARTIAL`, `UNSUPPORTED` or `UNKNOWN`. Reading an instruction does not prove it was followed; executing a task does not prove it was validated.

## Quick start for a project

1. Read the universal request in `START_HERE.md`, confirm the version and resolve whether the person wants to start, resume or verify a project.
2. Ask in plain language what they want to achieve and where state exists or should be preserved.
3. Evaluate real capabilities yourself; do not ask the user to configure technical files.
4. Select only necessary modules and present the load receipt in no more than five blocks.
5. Close material decisions, validate critical premises and request authority before creating or updating state or executing the first checkpoint.
6. Before delivery or persistence, apply the operating-contract pre-delivery review; self-review does not replace an independent Reviewer when one is required.
7. If rotation occurs, create a handoff and require a resumption handshake.
8. Evaluate the run when it is part of a pilot or audit.

## Distribution

This package is distributed under the MIT License. It may be used, copied, modified and redistributed, including commercially, provided that the copyright notice and license text in `../LICENSE` are preserved.

Credit: **Provider-Neutral Declarative Harness for LLMs, created by Manuel Carrero Rojo.**
