# Bilingual Parity Matrix

Spanish is the canonical source. The English version must preserve the same obligations, states, activation criteria, boundaries and evidence requirements. It does not need to be a word-for-word translation.

| Spanish area | English area | Status in 0.3.0 |
| --- | --- | --- |
| `../00_LEEME_PRIMERO.md` | `00_READ_ME_FIRST.md` | Semantic parity reviewed |
| `../01_nucleo/` | `01_core/` | Semantic parity reviewed, including guided start |
| `../02_modulos/` | `02_modules/` | Semantic parity reviewed, including Council and onboarding evaluation |
| `../03_plantillas/` | `03_templates/` | Equivalent fields, including startup summary, capabilities, Council and operational pulse |
| `../04_adaptadores/` | `04_adapters/` | Equivalent schema 1.1 and authority fields |
| `../05_ejemplos/` | `05_examples/` | Equivalent software, non-code and guided-start scenarios |
| `../06_validacion/` | `06_validation/` | Equivalent `ONBOARDING_01`, `AUTHORITY_01` and negative cases |

## Update rule

Every functional change to canonical content must update its English counterpart in the same change. Before release, compare manifests, control IDs, paths, startup modes, allowed states, capability and authority labels and activation criteria.
