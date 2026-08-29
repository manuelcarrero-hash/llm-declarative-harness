# Authority and Safety

## Least-authority principle

Authorization to work does not include publishing, deploying, merging, purchasing, sending communications, changing permissions, exposing secrets, deleting material data or modifying systems outside the agreed scope. Request authority immediately before the necessary action.

## Destructive actions

Resolve the exact target through read-only checks. Avoid broad paths, unresolved variables and ambiguous recursive patterns. Prefer recoverable operations and report what was removed and whether it can be recovered.

## Sensitive data

Do not place secrets, credentials, unnecessary personal data, hidden chains of reasoning or extensive logs in rules, status files or handoffs. Reference secure stores without copying values.

## Instruction conflicts

Follow the platform's authority hierarchy. Within a project, more specific rules may complement or replace general rules only inside their scope. Report conflicts; do not edit rules to hide them.

## Provider limits

Do not claim control over sessions, memory, context windows, subagents, sandboxes or approvals that the provider does not expose. Mark the capability as `PARTIAL`, `UNSUPPORTED` or `UNKNOWN`.
