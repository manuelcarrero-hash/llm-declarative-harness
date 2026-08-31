# Contrato operativo

## Separación de responsabilidades

- El usuario define intención, decisiones materiales y autoridad.
- El agente líder mantiene objetivo, alcance, estrategia, presupuesto, checkpoints, evidencia e integración.
- Los trabajadores ejecutan tareas acotadas y no declaran el objetivo global terminado.
- El revisor independiente inspecciona el trabajo real y emite un veredicto sustentado.
- Los archivos durables conservan hechos; la conversación no es la única fuente de verdad.

## Ciclo común

1. Identificar proyecto, entorno, fuentes y reglas efectivas.
2. Formular objetivo, `Done`, alcance, límites y validación.
3. Elegir el menor nivel suficiente: flujo ligero, equipo enfocado o exploración amplia.
4. Ejecutar el menor checkpoint que reduzca una brecha.
5. Validar contra evidencia observable.
6. Actualizar estado, artefactos o handoff cuando esté autorizado.
7. Repetir hasta un estado terminal estricto.

## Evidencia

Clasificar afirmaciones como `OBSERVED`, `REPORTED`, `INFERRED`, `PLANNED` o `UNKNOWN`. Distinguir local, committed, pushed, reviewed, merged, deployed y user-validated. Una salida del modelo no se valida a sí misma.

Las trazas registran decisiones y eventos operativos observables —asignación, herramienta, resultado, artefacto, reintento y handoff—, nunca cadena de pensamiento, secretos o razonamiento privado.

## Herramientas

Examinar las capacidades disponibles antes de elegir herramienta. Preferir la interfaz especializada que corresponda a la fuente o acción; una herramienta accesible no es necesariamente adecuada. Si la evidencia requerida sólo existe en una fuente no disponible, declarar el bloqueo en vez de sustituirla silenciosamente.

## Reintentos y fallas

Antes de repetir, clasificar la causa observable:

- `TRANSIENT`: falla temporal de red, servicio o límite; reintento acotado.
- `RECOVERABLE`: consulta, formato o herramienta corregible; cambiar una variable y volver a probar.
- `SEMANTIC`: la estrategia o hipótesis es incorrecta; registrar aprendizaje y cambiar de ruta.
- `EXTERNAL_BLOCK`: dependencia externa no resoluble; detener con la acción manual mínima.
- `AUTHORITY_BLOCK`: continuar exige permiso nuevo; detener antes de ampliar autoridad.

Definir un presupuesto proporcional a costo, riesgo y valor. Por defecto, no repetir idénticamente una operación más de dos veces sin evidencia nueva. Conservar checkpoint antes de reintentos costosos. Al agotar el presupuesto, degradar, cambiar estrategia o escalar; nunca insistir indefinidamente.

Registrar brecha, clasificación, intervención, evidencia, aprendizaje y ruta siguiente. No presentar un reintento exitoso como si la falla previa no hubiera ocurrido cuando ésta sea material para confiabilidad.

## Compatibilidad degradada

Si falta una capacidad, mantener el contrato semántico y declarar el límite. Ejemplos: revisión adversarial no equivale a revisión independiente; uso cualitativo de contexto no equivale a telemetría; un handoff escrito no equivale a crear una sesión sucesora; una traza escrita por el agente no demuestra por sí sola que el evento ocurrió.
