# Module: Agent Team

Use real roles when the platform supports separate agents and independence improves correctness.

## Minimum roles

- **Lead:** contract, authority, integration and closure.
- **Builder:** bounded implementation and tests.
- **Reviewer:** independent inspection of the actual change; verdict `APPROVED` or `CHANGES_REQUIRED`.

Add QA, security, design or research only when a useful boundary exists. One agent performing several personas does not prove independence.

Avoid concurrent writes to the same file. Each assignment must include directory, applicable rules, boundaries, deliverable and completion evidence.
