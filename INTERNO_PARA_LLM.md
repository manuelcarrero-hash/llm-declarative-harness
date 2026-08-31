# Interior para LLM — Arnés declarativo agnóstico

Versión: 0.7.0
Autor y mantenedor: Manuel Carrero Rojo

## Instrucción de arranque

Si eres una persona, usa únicamente `EMPEZAR_AQUI.md`; el resto es el interior técnico del arnés. Este archivo es el entrypoint técnico que `HARNESS_MANIFEST.yaml` ordena leer después del propio manifiesto. Si eres un LLM agéntico, confirma la versión observada, aplica `01_nucleo/INICIO_GUIADO.md`, presenta el comprobante de carga y activa únicamente los módulos compatibles y necesarios.

Este paquete define un arnés declarativo: reglas, contratos, estados, transferencias y evaluaciones. No contiene un runtime propio, no controla el bucle de inferencia del proveedor y no garantiza ejecución autónoma. Un modelo o plataforma debe interpretar los archivos y proporcionar herramientas, memoria, agentes, permisos y telemetría.

## Para qué sirve

Este arnés sirve para dar a un LLM agéntico una forma consistente, verificable y transferible de trabajar en proyectos complejos. Convierte buenas prácticas de coordinación en archivos que cualquier modelo compatible puede consultar, sin depender de una conversación previa ni de un proveedor específico.

Ayuda a:

- transformar una solicitud amplia en un objetivo con alcance y condición de terminado;
- establecer reglas durables para los agentes que trabajen en un proyecto;
- coordinar un líder, ejecutores y revisores sólo cuando existan frentes independientes que justifiquen el costo;
- dimensionar el esfuerzo, delegar por oleadas y preservar artefactos sin pérdida por resúmenes sucesivos;
- representar dependencias entre resultados complejos, localizar el impacto de una revisión y reanudar sólo desde una frontera respaldada por evidencia;
- conservar el estado real del proyecto fuera de la ventana de contexto;
- transferir trabajo entre agentes o sesiones mediante handoffs verificables;
- impedir cierres basados únicamente en afirmaciones del modelo;
- probar cambios pequeños y reversibles, conservando sólo los que superen una comparación predefinida;
- evaluar con evidencia si el proceso agéntico está funcionando de manera confiable;
- consultar perspectivas independientes y sintetizar decisiones sin confundir consenso con evidencia;
- adaptar el mismo marco de trabajo a distintos modelos y plataformas.

## Cuándo usarlo

Úsalo cuando el trabajo tenga una o varias de estas características:

- durará varias fases, sesiones o ventanas de contexto;
- incluye cambios materiales en código, documentos, datos o arquitectura;
- requiere coordinación entre agentes o roles con responsabilidades separadas;
- necesita reglas de operación, seguridad, revisión o definición de terminado;
- debe poder retomarse sin depender de la memoria de una conversación;
- necesita trazabilidad de decisiones, pruebas, despliegues o validación humana;
- existe un costo relevante si el modelo declara terminado algo incompleto;
- se quiere comparar la confiabilidad del trabajo entre modelos o plataformas;
- se busca crear un proceso repetible para varios proyectos o usuarios.

También puede aplicarse parcialmente: por ejemplo, usar únicamente objetivo y estado para un proyecto largo, o gobernanza y revisión para un repositorio de software.

## Cuándo no usarlo

No lo uses como proceso completo cuando:

- la solicitud es sencilla, de una sola respuesta y sin continuidad posterior;
- basta con explicar, resumir, traducir o redactar un texto breve;
- el trabajo es una modificación pequeña, local, reversible y de bajo riesgo;
- no existe un proyecto, estado durable ni necesidad de coordinación;
- una lista de tareas simple resuelve mejor la necesidad;
- se pretende usarlo como sustituto de permisos, sandboxes, autenticación, backups o controles técnicos reales;
- se espera que cree autonomía, memoria, agentes o telemetría que la plataforma no ofrece;
- se quiere eliminar la supervisión humana en decisiones sensibles, legales, financieras, médicas, de seguridad o de producción;
- el costo de mantener los artefactos sería mayor que el riesgo o complejidad del trabajo.

No debe activarse por inercia. Usa sólo los módulos que reduzcan un riesgo concreto o mejoren materialmente la continuidad, coordinación o verificabilidad.

## Objetivo

Permitir que un LLM capaz de actuar sobre proyectos pueda:

1. convertir una intención en un objetivo verificable;
2. descubrir las reglas aplicables al lugar de trabajo;
3. dividir y dimensionar trabajo sin perder propiedad, fidelidad ni autoridad;
4. mantener estado durable fuera de la conversación;
5. transferir trabajo a una sesión o agente limpio;
6. cerrar únicamente con evidencia;
7. evaluar la confiabilidad del proceso en ejecuciones reales.

## Orden de lectura

1. `HARNESS_MANIFEST.yaml`
2. `INTERNO_PARA_LLM.md` (este archivo)
3. `01_nucleo/CONTRATO_OPERATIVO.md`
4. `01_nucleo/AUTORIDAD_Y_SEGURIDAD.md`
5. `01_nucleo/INICIO_GUIADO.md`
6. Los módulos que el manifiesto marque para la tarea
7. Las plantillas correspondientes
8. `06_validacion/PRUEBA_DE_CONFORMIDAD.md` antes de afirmar compatibilidad

## Regla de honestidad

Usa siempre una de estas etiquetas para cada capacidad: `SUPPORTED`, `PARTIAL`, `UNSUPPORTED` o `UNKNOWN`. Una instrucción leída no demuestra que fue obedecida; una tarea ejecutada no demuestra que quedó validada.

## Inicio rápido para un proyecto

1. Lee la solicitud universal de `EMPEZAR_AQUI.md`, confirma la versión y resuelve si la persona quiere iniciar, continuar o verificar un proyecto.
2. Pregunta en lenguaje sencillo qué quiere lograr y dónde está o debe conservarse el estado.
3. Evalúa tú las capacidades reales; no pidas al usuario configurar archivos técnicos.
4. Selecciona sólo los módulos necesarios y presenta el comprobante de carga en cinco bloques como máximo.
5. Solicita autoridad antes de crear o actualizar estado y ejecuta el primer checkpoint autorizado.
6. Si existe rotación, genera handoff y exige handshake de reanudación.
7. Evalúa la ejecución cuando forme parte de un piloto o auditoría.

## Distribución

Este paquete se distribuye bajo la licencia MIT. Puede usarse, copiarse, modificarse y redistribuirse, incluso comercialmente, siempre que se conserve el aviso de copyright y el texto de la licencia incluidos en `LICENSE`.

Crédito: **Arnés declarativo agnóstico para LLMs, creado por Manuel Carrero Rojo.**
