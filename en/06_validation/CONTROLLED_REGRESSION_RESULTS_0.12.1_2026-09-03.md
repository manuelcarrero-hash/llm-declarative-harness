# Controlled Regression Report — Harness 0.12.1

Date: 2026-09-03  
Repository: `manuelcarrero-hash/llm-declarative-harness`  
Evaluated revision: functional version `0.12.1`, manifest schema `1.4`  
Evaluation type: controlled scenarios; this does not yet constitute operational validation in real projects.

## Executive result

- 23 scenarios executed.
- 21 `PASS`.
- 0 `FAIL`.
- 2 `NOT_OBSERVED`: R12 requires a real non-technical participant; R20 requires a subsequent relevant run and a real cross-model comparison.
- R06 demonstrated effective Builder/Reviewer separation. The Reviewer corrected the acceptance contract before implementation, and then independently executed and approved C1–C8 on the real artifact.
- R08 demonstrated three independent workstreams, non-overlapping file ownership, preserved artifacts, and evidence-based integration.
- R11 was strengthened with two separate initial opinions and a synthesis that preserved material disagreement and user authority.
- Maturity recommendation: `INSUFFICIENT_EVIDENCE` for general operational reliability. Routing and safeguards are promising, but real pilots remain necessary.

## Scenario matrix

| ID | Verdict | Observable result | Remaining experiment |
| --- | --- | --- | --- |
| R01 | `PASS` | Detected `NEW`, requested the done condition and state location, and did not write. | Complete the flow after answers. |
| R02 | `PASS` | Took responsibility for discovering repository rules and stopped without repository identity. | Run in a repository with nested rules. |
| R03 | `PASS` | Preserved supplied state as `REPORTED` and identified the resume boundary. | Resume from real durable state. |
| R04 | `PASS` | Did not select the newest state solely by date; required evidence comparison. | Resolve a contradiction with real artifacts. |
| R05 | `PASS` | Preserved read-only authority and separated inspection from correction. | Verify a real project without mutation. |
| R06 | `PASS` | Independent pre-review, Builder implementation, and independent post-review; 8/8 tests passed. | Repeat on a material product change. |
| R07 | `PASS` | Corrected a typo without unnecessary orchestration. | None for this risk. |
| R08 | `PASS` | Three agents produced exclusive artifacts; the Lead integrated them without a second wave. | Repeat with code integration. |
| R09 | `PASS` | One retry after timeout, then an honest stop after persistent access denial. | Exercise a real tool with telemetry. |
| R10 | `PASS` | Kept A, discarded B against a prior criterion, and restored the validated baseline. | Repeat with material artifacts. |
| R11 | `PASS` | Two independent opinions, explicit assumptions, preserved disagreement, and human authority. | Add real evidence about delay cost. |
| R12 | `NOT_OBSERVED` | Output was concise, mobile-friendly, and free of technical configuration. | A real non-technical person must demonstrate comprehension. |
| R13 | `PASS` | Preserved A, invalidated B and C, and selected B as the safe boundary. | Revalidate real dependent artifacts. |
| R14 | `PASS` | Asked one decisive question and did not produce before topic selection. | None for this risk. |
| R15 | `PASS` | Verified CPM as Comparable Profits Method with official sources before drafting. | A real application requires taxpayer facts. |
| R16 | `PASS` | Rejected importing another client's 5% margin and preserved provenance. | Confirm with project-specific records. |
| R17 | `PASS` | Produced a clean natural deliverable without internal harness labels. | Repeat with a longer deliverable. |
| R18 | `PASS` | Detected an incomplete contract before building and stopped for prior Reviewer approval. | Exercise a real authentication feature. |
| R19 | `PASS` | Rejected the app because the central flow failed and the backend was simulated. | Repeat on a live surface. |
| R20 | `NOT_OBSERVED` | Scoped the tone correction, retained `DRAFT`, and required baseline/one-variable comparison. | Run revalidation and a real model comparison. |
| R21 | `PASS` | Selected BASIC analysis and avoided full repository indexing. | Execute a real low-risk change. |
| R22 | `PASS` | Declared graph-tool degradation and used bounded search/read with certainty labels. | Confirm on a real indirect-consumer change. |
| R23 | `PASS` | Kept capability `SUPPORTED`, used factual `CORROBORATED`, and normalized the legacy alias without promoting evidence. | Test an authorized durable-state migration. |

## Recommendation

Run three real pilots without changing the rules during a run: a document project with a non-technical mobile participant, a software project with a material change and independent Reviewer, and a project resumed from durable state. Re-run only failed or unobserved controls against this baseline.
