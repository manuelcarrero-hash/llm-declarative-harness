# Módulo: estado del proyecto

Mantener una sola fotografía autoritativa que responda: qué se hizo, dónde estamos, qué sigue y a dónde queremos llegar. Este módulo también gobierna continuidad, checkpoints, handoffs y reanudación cuando el trabajo cruza agentes, sesiones, compactación, fallas o fases.

## Modos

- `REPORT`: inspeccionar y reportar sin escribir.
- `SYNC`: crear o actualizar sólo con autorización explícita.

## Contenido mínimo

Identidad del proyecto, timestamp y anclas; trabajo validado; posición actual; riesgos y decisiones; siguiente acción; gates; destino y criterios de éxito. Separar hechos confirmados del encargo actual, antecedentes de memoria o proyectos previos, materiales reutilizables, referencias de estilo y propuestas aún no aceptadas. Si existe un mapa de trabajo activo, enlazarlo y registrar su frontera de reanudación sin duplicar sus detalles. Resolver contradicciones con evidencia más actual y directa, sin borrar decisiones intencionales.

No elevar a hecho confirmado una interpretación, tema, caso, dato o preferencia elegida por el agente. Usar la taxonomía factual de `../01_nucleo/CONTRATO_OPERATIVO.md`. Antes de persistir un elemento `INFERRED` o `PLANNED` que cambie materialmente el trabajo futuro, obtener confirmación o conservarlo explícitamente como pendiente. Una corrección posterior debe rectificar también el estado contaminado y dejar trazabilidad breve del cambio.

## Frontera de reanudación

Una frontera permite conservar resultados ya comprobados sólo cuando su evidencia siga vigente, sus dependencias sean conocidas y ningún cambio posterior afecte su validez. Registrar qué se conserva, qué se invalida, el punto exacto de reanudación y la evidencia que lo justifica.

El mapa es una vista derivada, no una segunda fuente de verdad. Ante dependencias ausentes, ambiguas, divergentes o no verificables, invalidar conservadoramente y repetir la validación aplicable.

## Pulso operativo

Cuando facilite reanudar o decidir, comenzar con la vista compacta de `../03_plantillas/PULSO_OPERATIVO.template.md`. Es una vista del estado autoritativo, no una segunda fuente de verdad.

Incluir telemetría opcional sólo cuando una fuente actual la exponga directamente. Clasificar cada señal con la taxonomía factual del Contrato Operativo, fuente y vigencia. Usar `UNAVAILABLE` únicamente cuando la capacidad sea `UNSUPPORTED`. No convertir cantidad de mensajes, tiempo transcurrido, volumen de salida o intuición en porcentajes, costos o límites exactos.

## Checkpoints y artefactos

Usar porcentajes sólo con telemetría real y capacidad total conocida. Política por defecto: checkpoint preventivo al 30% medido y rotación al 40% medido; sin telemetría, usar señales cualitativas y mantener el porcentaje `UNKNOWN`.

Crear también un checkpoint semántico cuando cambie materialmente la naturaleza del trabajo y la etapa cerrada haya producido evidencia o decisiones que la siguiente usará como premisas, cuando perderla obligaría a reconstrucción material, cuando cambien riesgo, autoridad o criterios, o cuando una revisión pueda invalidar dependientes. Ejemplos no obligatorios: investigación a decisión, decisión a producción, producción a revisión, revisión a corrección o liberación, e incidente a recuperación.

El checkpoint semántico registra motivo, etapa cerrada, siguiente etapa, resultados establecidos, evidencia, decisiones aprobadas, preguntas abiertas, trabajo preservado o invalidado y punto exacto de reanudación. No generarlo por cada mensaje, por un cambio nominal sin nueva evidencia, en una tarea breve de una sola etapa ni cuando no ayude a reanudar, revisar o proteger resultados. Explicarlo a la persona como cierre de una etapa, no como control técnico de contexto.

En cada checkpoint relevante, actualizar o enlazar el pulso operativo. Cuando exista escritura durable, cada agente conserva su salida material en origen y entrega referencia, estado, evidencia, brechas e incertidumbres. El receptor lee el artefacto autoritativo cuando una síntesis pueda perder precisión; una referencia rota o no verificable no completa un handoff.

## Fallas, reanudación y rotación

Aplicar la taxonomía y presupuesto de reintentos del Contrato Operativo. Antes de reiniciar trabajo costoso, conservar el último checkpoint seguro, causa observable, intentos y alternativa siguiente. Con mapa activo, recorrer sólo dependencias sustentadas y revalidar descendientes afectados; no empezar de cero salvo corrupción, incompatibilidad o ausencia demostrable de un punto seguro.

Para rotar: alcanzar un límite atómico seguro, escribir y verificar el handoff, sincronizar estado autorizado, iniciar al sucesor con contexto mínimo y exigir handshake antes de editar. No afirmar persistencia, reanudación, detención o creación de sesión que la plataforma no pueda demostrar.
