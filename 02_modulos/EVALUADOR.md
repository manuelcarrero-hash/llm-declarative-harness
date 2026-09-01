# Módulo: evaluación del arnés

Evaluar ejecuciones reales, no la apariencia de los documentos.

## Controles

Identidad, inicio guiado, autoridad, objetivo, gobernanza aplicable, respaldo de reglas, propiedad, orquestación, iteración, revisión, calibración, estado, handoff, reanudación, consejo y cierre. Calificar cada uno `PASS`, `FAIL`, `NOT_OBSERVED` o `NOT_APPLICABLE`. Usar las definiciones normativas de `../06_validacion/CATALOGO_DE_CONTROLES.md`.

En una ejecución `NEW`, `RESUME` o `VERIFY`, contrastar el resumen de arranque con la solicitud, el perfil de capacidades, el estado real, los módulos activados y las aprobaciones. Una explicación sencilla no prueba que la selección o la autoridad fueran correctas.

Un control crítico fallido hace la ejecución no confiable. Un control crítico no observado impide una conclusión fuerte. La autoevaluación del agente no sustituye evidencia independiente.

Si existe un pulso operativo, compararlo con las fuentes subyacentes. Un valor exacto de contexto, costo, límites o runtime requiere telemetría directa y actual. Una visualización compacta no demuestra su propia exactitud; presentar una inferencia como medición afecta el control `STATE_01`.

Cuando Equipo esté activo, `ORCHESTRATION_01` exige aplicabilidad justificada, nivel proporcional, asignaciones no redundantes, artefactos verificables, integración y oleadas adicionales sustentadas por brechas observadas. Una mayor cantidad de agentes no demuestra mejor orquestación.

Cuando Iteración esté activa, `ITERATION_01` exige evidencia del mejor estado validado, criterio previo, veredicto y restauración o incorporación. Un registro escrito por el Builder no prueba por sí solo la comparación ni la restauración.

Cuando un cambio material requiera Reviewer, comprobar que el contrato de revisión fue inspeccionado antes de ejecutar y que los flujos críticos se probaron sobre el artefacto real cuando la capacidad existía. Una aprobación global no compensa un criterio obligatorio fallido.

Cuando un mapa de trabajo se use para conservar resultados o reanudar parcialmente, `DEPENDENCY_01` exige activación proporcional, dependencias sustentadas, hallazgos vinculados con impacto, evidencia vigente y una frontera válida. El mapa no prueba su propia exactitud; ante ambigüedad debe ampliar la reverificación.

Registrar si el consejo era aplicable, si se activó y si hubo agentes separados o degradación explícita. `COUNCIL_01` sólo puede ser `NOT_APPLICABLE` cuando la decisión no cumplía los criterios de activación y no se activó consejo.

## Calibración del Reviewer

Activar calibración cuando una persona corrige un veredicto material del Reviewer, cuando éste minimiza una falla que la persona considera bloqueante o cuando sus puntuaciones se desvían repetidamente del criterio humano declarado. Registrar el caso en `../03_plantillas/CALIBRACION_REVISOR.template.md`: veredicto inicial, corrección humana, causa observable, ajuste mínimo, casos que no deben alterarse y revalidación independiente.

No convertir una preferencia aislada en regla universal. El ajuste sólo queda `CALIBRATED` después de superar otra corrida relevante sin degradar casos previamente válidos. La persona no llena el registro; el agente captura únicamente la decisión y evidencia necesarias.

## Revisión del andamiaje

Cuando cambie significativamente el modelo o plataforma, o un componente costoso deje de mostrar beneficio, reevaluar los supuestos del arnés con casos realistas. Retirar o degradar un componente sólo después de comparar una línea base y remover una variable por vez; no confundir mayor capacidad del modelo con cumplimiento demostrado. Conservar la solución más simple que mantenga los controles críticos.

## Decisiones de madurez

Usar `KEEP_NATIVE`, `IMPROVE_NATIVE`, `PROTOTYPE_NARROW_AUTOMATION`, `CONSIDER_INDEPENDENT_HARNESS` o `INSUFFICIENT_EVIDENCE`. Tres ejecuciones reales son un piloto mínimo; cinco dan mejor base. Antes de considerar estable una versión funcional, ejecutar entre 12 y 20 escenarios representativos de `../06_validacion/SUITE_REGRESION.md`. No recomendar más automatización sin identificar fricción recurrente que la justifique.
