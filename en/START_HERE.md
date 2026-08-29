# Start here

This is the only file you need to use. You do not need to open, choose, or configure the other files in this folder.

## Universal instruction

Copy and send this text to an assistant that can access the harness folder and your project files:

> I want to work on this project using the harness. First read the manifest, tell me which version you found and cite the file; if you cannot, stop and explain the smallest manual action required. Then ask only the necessary questions and decide whether to start a new project, continue an existing one, or verify whether it is truly finished. Consult the required instructions yourself; do not ask me to choose modules, edit technical files, or describe your tools. After my answers and before modifying anything or taking material action, show me in plain language: what you understood, what result will prove completion, where project state is or should be kept, what you can actually do, what you could not verify, which authorization you will need, which boundaries remain open, and the first step.

Then answer the assistant's questions in ordinary language.

## What you should receive before work begins

A brief load receipt with no more than five blocks:

1. **Mode:** new, continue, or verify.
2. **Goal and state:** the intended result, how completion will be known and where progress will be preserved.
3. **Real capabilities:** what the assistant can do, its evidence, and what remains unverified.
4. **Minimum plan:** internally selected modules and first step, without jargon.
5. **Your control:** actions that will require your authorization and open boundaries or risks.

If the assistant cannot identify the harness version, asks you to configure files, or modifies anything before presenting this receipt, startup has not completed correctly.

## Important

The harness organizes and makes LLM work auditable; it does not add tools or guarantee compliance. The remaining files are technical internals for the assistant, not documentation you need to learn.

Español: usa [`../EMPEZAR_AQUI.md`](../EMPEZAR_AQUI.md).

**Provider-neutral declarative harness for LLMs, created by Manuel Carrero Rojo.**
