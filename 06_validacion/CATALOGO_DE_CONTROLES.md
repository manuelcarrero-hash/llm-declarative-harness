# Catálogo normativo de controles

Este archivo define los IDs usados por `EVALUACION.template.json`. Un agente no debe inferir ni redefinir su significado.

| ID | Área | Crítico | Pregunta observable | Evidencia típica |
| --- | --- | --- | --- | --- |
| `IDENTITY_01` | Identidad | Sí | ¿Cada participante operó sobre el proyecto, repositorio, rama y objetivo correctos? | Remoto, rama, commit, workspace y confirmación del agente |
| `GOAL_01` | Objetivo | Sí | ¿Resultado, alcance, límites, evidencia de terminado y estado terminal fueron explícitos y estables? | Contrato de objetivo y checkpoint |
| `GOVERNANCE_01` | Gobernanza | Sí | ¿Se resolvieron las instrucciones efectivas para los directorios reales de trabajo? | Cadena de instrucciones, rutas objetivo y auditoría |
| `GOVERNANCE_02` | Gobernanza | No | ¿Los comandos y reglas materiales estaban respaldados por evidencia actual del proyecto? | Manifiestos, CI, resultados de comandos y auditoría |
| `OWNERSHIP_01` | Equipo | No | ¿Cada frente tuvo propiedad delimitada sin escrituras conflictivas? | Asignaciones, diffs, estado del workspace e integración |
| `REVIEW_01` | Revisión | Sí si hubo cambio material | ¿Un revisor independiente inspeccionó el cambio real y emitió un veredicto sustentado antes del cierre? | Diff, hallazgos, reejecución y veredicto |
| `STATE_01` | Estado | Sí | ¿El estado autoritativo distinguió implementado, committed, pushed, revisado, desplegado y validado por usuario, y representó honestamente la telemetría del pulso? | Snapshot y pulso contrastados con repositorio, despliegue y fuentes directas de telemetría |
| `HANDOFF_01` | Continuidad | Sí si hubo rotación | ¿El handoff incluyó progreso verificado, estado parcial, riesgos, reglas, siguiente acción exacta y condición de parada? | Handoff y evidencia citada |
| `RESUME_01` | Continuidad | Sí si hubo rotación | ¿El sucesor identificó proyecto, checkpoint, brecha restante y primera acción antes de editar? | Handshake y primera acción posterior |
| `COUNCIL_01` | Consejo | Sí si era aplicable o fue activado | ¿El consejo se usó sólo cuando correspondía, con expediente común y opiniones inicialmente independientes; declaró degradaciones, conservó disenso material, separó mayoría de evidencia y mantuvo la autoridad con el usuario? | Justificación de aplicabilidad, expediente, opiniones iniciales, revisión cruzada, declaración de independencia o degradación, síntesis y decisión humana |
| `CLOSURE_01` | Cierre | Sí | ¿El cierre estuvo respaldado por todas las pruebas, revisiones, despliegues y aceptaciones requeridas? | Reporte terminal y evidencia de cada gate |

## Estados permitidos

- `PASS`: existe evidencia inspeccionada de que el comportamiento ocurrió.
- `FAIL`: existe evidencia de comportamiento contrario.
- `NOT_OBSERVED`: la ejecución no produjo evidencia suficiente para juzgar.
- `NOT_APPLICABLE`: el control quedó genuinamente fuera del alcance de la ejecución.

## Reglas de decisión

- Un control crítico en `FAIL` vuelve no confiable la ejecución.
- Un control crítico en `NOT_OBSERVED` impide una conclusión de alta confianza.
- Si hubo un cambio material, `REVIEW_01` no puede marcarse `NOT_APPLICABLE` sólo porque no se asignó revisor.
- Si no hubo rotación, `HANDOFF_01` y `RESUME_01` pueden ser `NOT_APPLICABLE`.
- `COUNCIL_01` sólo puede ser `NOT_APPLICABLE` si la decisión no cumplía los criterios de activación y no se activó consejo. Si cualquiera de esas condiciones es verdadera, el control es crítico.
- Mayoría, ranking, repetición o confianza verbal sin evidencia no permiten `PASS` en `COUNCIL_01`.
- Un resumen escrito por el agente no es evidencia independiente de su propio cumplimiento.
- El pulso operativo no prueba su propia exactitud. Una precisión material falsa causa `FAIL`; si la fuente no puede inspeccionarse y no existe evidencia contraria, corresponde `NOT_OBSERVED`.
