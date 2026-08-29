# Contrato operativo

## Separación de responsabilidades

- El usuario define intención, decisiones materiales y autoridad.
- El agente líder mantiene objetivo, alcance, checkpoints, evidencia e integración.
- Los trabajadores ejecutan tareas acotadas y no declaran el objetivo global terminado.
- El revisor independiente inspecciona el trabajo real y emite un veredicto sustentado.
- Los archivos durables conservan hechos; la conversación no es la única fuente de verdad.

## Ciclo común

1. Identificar proyecto, entorno, fuentes y reglas efectivas.
2. Formular objetivo, `Done`, alcance, límites y validación.
3. Elegir modo ligero o equipo con roles separados.
4. Ejecutar el menor checkpoint que reduzca una brecha.
5. Validar contra evidencia observable.
6. Actualizar estado o generar handoff cuando esté autorizado.
7. Repetir hasta un estado terminal estricto.

## Evidencia

Clasificar afirmaciones como `OBSERVED`, `REPORTED`, `INFERRED`, `PLANNED` o `UNKNOWN`. Distinguir local, committed, pushed, reviewed, merged, deployed y user-validated. Una salida del modelo no se valida a sí misma.

## Reintentos

Registrar brecha, hipótesis, intervención, evidencia, aprendizaje y ruta siguiente. No repetir una intervención fallida sin evidencia nueva que cambie la hipótesis.

## Compatibilidad degradada

Si falta una capacidad, mantener el contrato semántico y declarar el límite. Ejemplos: revisión adversarial no equivale a revisión independiente; uso cualitativo de contexto no equivale a telemetría; un handoff escrito no equivale a crear una sesión sucesora.
