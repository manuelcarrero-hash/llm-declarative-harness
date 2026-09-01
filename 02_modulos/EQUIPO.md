# Módulo: equipo agéntico

Usar roles reales sólo cuando la plataforma permita agentes separados y la división mejore materialmente corrección, cobertura, velocidad o independencia. La persona no selecciona roles, niveles ni agentes; el Lead resuelve la configuración y la explica en lenguaje sencillo.

## Prueba de aplicabilidad

Activar Equipo cuando existan al menos dos frentes materialmente independientes, cada uno pueda producir evidencia propia y además concurra una o más de estas condiciones:

- la información excede razonablemente el contexto de un agente;
- se necesitan herramientas, fuentes o especialidades distintas;
- la exploración en paralelo reduce una demora material;
- una revisión independiente disminuye un riesgo relevante;
- el valor esperado justifica el costo y coordinación adicionales.

No activarlo para trabajo pequeño, altamente secuencial, con contexto inseparable, escrituras sobre el mismo artefacto o frentes que sólo repetirían la misma búsqueda. Separar Builder y Reviewer puede seguir siendo necesario aunque la ejecución permanezca en nivel `SINGLE`.

## Niveles internos de esfuerzo

- `SINGLE`: un ejecutor o flujo secuencial; tarea pequeña o estrechamente dependiente.
- `FOCUSED`: normalmente dos a cuatro frentes independientes con entregables delimitados.
- `BROAD`: investigación o verificación extensa con muchas fuentes, herramientas o contextos; exige presupuesto y trazabilidad reforzada.

Comenzar con el menor nivel suficiente. Los rangos son heurísticos, no cuotas. Usar más agentes requiere una brecha concreta; disponibilidad no equivale a necesidad.

## Roles mínimos

- **Lead:** contrato, autoridad, estrategia, presupuesto, integración y cierre.
- **Builder / Worker:** ejecución acotada, evidencia y artefacto propio.
- **Reviewer:** inspección independiente del contrato y del cambio real; veredicto `APPROVED` o `CHANGES_REQUIRED`. Si Iteración está activa, comprueba además línea base, comparabilidad, integridad de la validación, regresiones, costo de complejidad y restauración.

Añadir QA, seguridad, diseño, investigación o revisión de evidencia sólo cuando exista una frontera útil. Un mismo agente interpretando varios personajes no prueba independencia.

## Contrato de revisión previo

Cuando un cambio material requiera Reviewer independiente, éste debe inspeccionar antes de ejecutar: resultado esperado, decisiones materiales confirmadas, comportamientos observables, evidencia, flujos críticos, umbrales de rechazo y acciones no autorizadas. El Builder propone cómo demostrar `Done`; el Reviewer identifica cobertura insuficiente, criterios imposibles de probar o incentivos para aprobar trabajo incompleto. El Lead resuelve la discrepancia sin ampliar el alcance ni sustituir una decisión reservada al usuario.

No exigir esta negociación para tareas pequeñas o cuando la plataforma no permita independencia. En ese caso, aplicar la revisión previa proporcional y declarar la degradación. El acuerdo técnico permanece interno salvo que revele una decisión material para la persona.

## QA sobre el artefacto real

Cuando exista un artefacto ejecutable o interactivo y las herramientas estén disponibles, el Reviewer debe recorrer los flujos críticos mediante la misma superficie que usaría la persona y contrastar sus efectos observables en las capas relevantes. No basta leer el diff, inspeccionar una captura estática, comprobar que existe una función ni aceptar el reporte del Builder. Registrar flujo, acción, resultado esperado, resultado observado y evidencia.

Si la superficie real no está disponible, declarar `PARTIAL` y ejecutar la mejor verificación sustituta sin presentarla como prueba end-to-end. Cada criterio obligatorio tiene umbral de rechazo propio: una fortaleza visual, técnica o narrativa no compensa la falla de una función central.

## Delegación por oleadas

1. Delimitar frentes no redundantes y asignar la primera oleada mínima.
2. Usar `../03_plantillas/ASIGNACION_AGENTE.template.md` para cada frente material.
3. Evitar escrituras concurrentes sobre el mismo archivo y declarar exclusiones entre agentes.
4. Recibir estado, evidencia, artefacto, brechas e incertidumbres.
5. Integrar y comprobar cobertura antes de abrir otra oleada.
6. Crear una segunda oleada sólo para una brecha observada, no por inercia.

Cada asignación debe incluir objetivo, pregunta exacta, frontera, incluidos y excluidos, fuentes o herramientas preferidas, acciones no autorizadas, formato, evidencia, artefacto, condición de terminado, condición de parada y presupuesto.

## Dependencias entre resultados

Cuando existan al menos tres resultados materiales, una dependencia observable y la modificación de uno pueda afectar la validez de otro, generar internamente `../03_plantillas/MAPA_TRABAJO.template.md`. El Lead mantiene resultados, dependencias, artefactos y evidencia; la persona no dibuja el mapa ni configura relaciones.

El mapa es derivado y prescindible: no sustituye los artefactos ni el estado autoritativo. Registrar sólo dependencias sustentadas. Si una relación es ambigua o no verificable, no usar el mapa para conservar trabajo sin nueva validación.

## Artefactos y fidelidad

Cuando exista escritura durable compatible, el agente especializado conserva directamente su resultado y devuelve una referencia ligera al Lead. El Lead integra por referencia y no reescribe innecesariamente el contenido fuente. Si no existe escritura durable, declarar la degradación y preservar la salida estructurada en el medio disponible.

Para equipos materiales, auditorías o incidentes, usar `../03_plantillas/TRAZA_ORQUESTACION.template.md`. Registrar hechos operativos, nunca cadena de pensamiento.
