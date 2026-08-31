# Bilingual Parity Matrix

Spanish is the canonical source. The English version must preserve the same obligations, states, activation criteria, boundaries and evidence requirements. It does not need to be a word-for-word translation.

| Spanish area | English area | Status in 0.7.0 |
| --- | --- | --- |
| `../INTERNO_PARA_LLM.md` | `LLM_INTERNALS.md` | Semantic parity reviewed |
| `../EMPEZAR_AQUI.md` | `START_HERE.md` | Equivalent universal instruction and five-block expectation |
| `../01_nucleo/` | `01_core/` | Semantic parity reviewed, including guided start |
| `../02_modulos/` | `02_modules/` | Semantic parity reviewed, including Council, Iteration, level-based orchestration, work maps and onboarding evaluation |
| `../03_plantillas/` | `03_templates/` | Equivalent fields, including load receipt, startup summary, capabilities, Council, Iteration, assignment, work map, trace and operational pulse |
| `../04_adaptadores/` | `04_adapters/` | Equivalent schema 1.1 and authority fields |
| `../05_ejemplos/` | `05_examples/` | Equivalent software, non-code, guided-start and non-technical comprehension scenarios |
| `../06_validacion/` | `06_validation/` | Equivalent `LOAD_01`, `ONBOARDING_01`, `AUTHORITY_01`, `EXECUTION_01`, `EXPERIENCE_01`, `ITERATION_01`, `ORCHESTRATION_01`, `DEPENDENCY_01`, regression suite, exploratory runs and negative cases |

## Update rule

Every functional change to canonical content must update its English counterpart in the same change. Before release, compare manifests, control IDs, paths, startup modes, allowed states, capability and authority labels and activation criteria.
