# Módulo: estado del proyecto

Mantener una sola fotografía autoritativa que responda: qué se hizo, dónde estamos, qué sigue y a dónde queremos llegar.

## Modos

- `REPORT`: inspeccionar y reportar sin escribir.
- `SYNC`: crear o actualizar sólo con autorización explícita.

## Contenido mínimo

Identidad del proyecto, timestamp y anclas; trabajo validado; posición actual; riesgos y decisiones; siguiente acción; gates; destino y criterios de éxito. Separar hechos confirmados del encargo actual, antecedentes de memoria o proyectos previos, materiales reutilizables, referencias de estilo y propuestas aún no aceptadas. Si existe un mapa de trabajo activo, enlazarlo y registrar su frontera de reanudación sin duplicar sus detalles. Resolver contradicciones con evidencia más actual y directa, sin borrar decisiones intencionales.

No elevar a hecho confirmado una interpretación, tema, caso, dato o preferencia elegida por el agente. Registrar su procedencia y estado (`CONFIRMED`, `SUPPORTED`, `PROPOSED`, `ASSUMPTION` o `UNKNOWN`). Antes de persistir un elemento `PROPOSED` o `ASSUMPTION` que cambie materialmente el trabajo futuro, obtener confirmación o conservarlo explícitamente como pendiente. Una corrección posterior debe rectificar también el estado contaminado y dejar trazabilidad breve del cambio.

## Frontera de reanudación

Una frontera permite conservar resultados ya comprobados sólo cuando su evidencia siga vigente, sus dependencias sean conocidas y ningún cambio posterior afecte su validez. Registrar qué se conserva, qué se invalida, el punto exacto de reanudación y la evidencia que lo justifica.

El mapa es una vista derivada, no una segunda fuente de verdad. Ante dependencias ausentes, ambiguas, divergentes o no verificables, invalidar conservadoramente y repetir la validación aplicable.

## Pulso operativo

Cuando facilite reanudar o decidir, comenzar con la vista compacta de `../03_plantillas/PULSO_OPERATIVO.template.md`. Es una vista del estado autoritativo, no una segunda fuente de verdad.

Incluir telemetría opcional sólo cuando una fuente actual la exponga directamente. Etiquetar cada señal como `OBSERVED`, `REPORTED`, `INFERRED`, `PLANNED` o `UNKNOWN`, con fuente y vigencia. Usar `UNAVAILABLE` únicamente cuando la capacidad sea `UNSUPPORTED`. No convertir cantidad de mensajes, tiempo transcurrido, volumen de salida o intuición en porcentajes, costos o límites exactos.
