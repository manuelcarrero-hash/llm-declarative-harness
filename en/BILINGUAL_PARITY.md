# Bilingual Parity Matrix

Spanish is the canonical source. The English version must preserve the same obligations, states, activation criteria, boundaries and evidence requirements. It does not need to be a word-for-word translation.

| Spanish area | English area | Status in 0.9.0 |
| --- | --- | --- |
| `../INTERNO_PARA_LLM.md` | `LLM_INTERNALS.md` | Semantic parity reviewed |
| `../EMPEZAR_AQUI.md` | `START_HERE.md` | Equivalent universal instruction and five-block expectation |
| `../01_nucleo/` | `01_core/` | Semantic parity reviewed, including guided start, specification gate and pre-delivery review |
| `../02_modulos/` | `02_modules/` | Parity reviewed, including prior Reviewer contract, artifact QA, calibration and scaffolding reassessment |
| `../03_plantillas/` | `03_templates/` | Equivalent fields, including Reviewer calibration, contract, flows, thresholds and evidence |
| `../04_adaptadores/` | `04_adapters/` | Equivalent schema 1.1 and authority fields |
| `../05_ejemplos/` | `05_examples/` | Equivalent software, non-code, guided-start and non-technical comprehension scenarios |
| `../06_validacion/` | `06_validation/` | Equivalent `REVIEW_01`, new `CALIBRATION_01`, schema 1.8 and R18–R20 |

## Update rule

Every functional change to canonical content must update its English counterpart in the same change. Before release, compare manifests, control IDs, paths, startup modes, allowed states, capability and authority labels and activation criteria.
