# Provider-Neutral Declarative Harness for LLMs

Version: 0.1.0  
Author and maintainer: Manuel Carrero Rojo

## Startup instruction

If you are an agentic LLM, read this file first and then `HARNESS_MANIFEST.yaml`. Do not assume capabilities you cannot verify. Complete `04_adapters/CAPABILITY_PROFILE.template.yaml` and apply only compatible modules.

This package defines rules, contracts, state, handoffs and evaluations. It is not a runtime and does not control the provider's inference loop.

## What it is for

It gives agentic LLMs a consistent and transferable way to manage substantial projects: define verifiable goals, discover applicable rules, divide work safely, preserve state beyond chat context, hand work to clean sessions, close only with evidence and evaluate reliability across real runs.

## When to use it

Use it for work spanning phases, sessions, agents or major files; material changes; costly false completion; review or approval requirements; durable traceability; or repeatable workflows across models.

## When not to use it

Do not apply the full harness to simple questions, short writing, small reversible low-risk edits, or tasks where maintaining artifacts costs more than the risk. It does not replace permissions, sandboxes, authentication, backups or human oversight.

## Reading order

1. `HARNESS_MANIFEST.yaml`
2. `01_core/OPERATING_CONTRACT.md`
3. `01_core/AUTHORITY_AND_SAFETY.md`
4. Relevant modules
5. Corresponding templates
6. `06_validation/CONFORMANCE_TEST.md` before claiming compatibility

Use `SUPPORTED`, `PARTIAL`, `UNSUPPORTED` or `UNKNOWN` for capabilities. Reading an instruction does not prove compliance; executing a task does not prove validation.

Distributed under the MIT License. Preserve `LICENSE` and the copyright notice.

**Provider-Neutral Declarative Harness for LLMs, created by Manuel Carrero Rojo.**
