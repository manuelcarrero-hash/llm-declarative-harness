# Advisory compatibility matrix

This reference helps identify which capabilities must be checked on each platform. It does not grant capabilities or replace `CAPABILITY_PROFILE.template.yaml`. Current execution evidence always prevails over this matrix; the completed profile comes next, then this dated reference, and general assumptions last.

## Maintenance rule

Use only `SUPPORTED`, `PARTIAL`, `UNSUPPORTED` or `UNKNOWN`. Every claim other than `UNKNOWN` must state the exact platform and interface, scope, verifiable source and date. A stale, ambiguous or contradicted mark returns to `UNKNOWN` until rechecked. Do not infer parity among applications, plans, versions or configurations from the same provider.

## Initial reference

Cells deliberately remain `UNKNOWN` until evidence is recorded in a real run. The agent consults this table to plan checks; it does not ask the user to complete it.

| Platform / interface | Durable files | Hierarchical instructions | Tools | Separate agents | Independent review | Context telemetry | Session rotation | Approval pause | Tracing | Resumable state | Source / date / scope |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Current platform | `UNKNOWN` | `UNKNOWN` | `UNKNOWN` | `UNKNOWN` | `UNKNOWN` | `UNKNOWN` | `UNKNOWN` | `UNKNOWN` | `UNKNOWN` | `UNKNOWN` | Verify during guided start |

## Evidence record

When a recurring orientation adds value, add a row with:

- exact provider, product and interface name;
- relevant version, plan or configuration;
- capability and label;
- observed test or primary documentation;
- check date;
- limitations and conditions.

A contradiction in the current run corrects that run's profile and flags the advisory entry for review; work is never forced to match the table.
