# Inicio guiado

Este protocolo convierte una solicitud sencilla en un arranque verificable. Es declarativo: una plataforma compatible lo interpreta, pero el arnés no proporciona por sí mismo herramientas, memoria, permisos ni automatización.

## Modos de entrada

- `NEW`: iniciar un proyecto y crear estado durable cuando esté autorizado.
- `RESUME`: localizar, contrastar y reanudar el estado autoritativo existente.
- `VERIFY`: comprobar en modo de solo lectura si el resultado satisface realmente su condición de terminado.

Las instrucciones listas para copiar y una interfaz guiada son entradas equivalentes al mismo protocolo. No deben producir reglas, módulos o criterios de cierre distintos.

La instrucción universal de `EMPEZAR_AQUI.md` es la entrada humana preferida. Las tres instrucciones específicas se conservan como alternativas y ejemplos, no como decisiones que el usuario deba comprender.

## Gate de carga

Antes de formular preguntas, el agente debe leer el manifiesto, informar la versión exacta observada y citar como evidencia el archivo del que la obtuvo. Después puede hacer las preguntas mínimas necesarias. Antes de cualquier acción material debe presentar el comprobante completo de `03_plantillas/COMPROBANTE_CARGA.template.md` en un máximo de cinco bloques.

Si no puede consultar el arnés, no encuentra el manifiesto o no puede confirmar la versión, debe detenerse. No puede sustituir la lectura por conocimiento previo, inferir la versión por el nombre de una carpeta ni afirmar que aplicó módulos que no leyó. Debe explicar la acción manual mínima para darle acceso.

## Tres pilares

1. Preguntar en lenguaje sencillo qué quiere lograr la persona y qué resultado observable demostraría que quedó terminado.
2. Preguntar si ya existe estado del proyecto y dónde está. Si no existe o la persona no sabe dónde guardarlo, recomendar únicamente ubicaciones que la plataforma pueda usar realmente.
3. Evaluar las capacidades del entorno con evidencia. Esta evaluación corresponde al agente, no al usuario. Preguntar sólo cuando una capacidad permanezca `UNKNOWN`, exista más de una fuente autoritativa posible o se requiera autorización.

No pedir al usuario que complete YAML, Markdown, manifiestos, rutas técnicas o una selección manual de módulos. El agente traduce las respuestas al contrato del arnés.

## Secuencia normativa

1. Cumplir el gate de carga y resolver el modo `NEW`, `RESUME` o `VERIFY` a partir de la solicitud universal; preguntar sólo si la intención es ambigua.
2. Identificar el proyecto, entorno y fuentes ya disponibles sin realizar sondeos ajenos al alcance.
3. Resolver objetivo y condición observable de terminado. Si la persona menciona alternativas, ejemplos o referencias amplias que cambiarían materialmente el resultado, hacer una sola pregunta decisiva o recomendar una opción y esperar confirmación; no elegirla silenciosamente. En `RESUME`, conservar el objetivo existente salvo evidencia de que falta, cambió o se contradice.
4. Localizar el estado autoritativo. Si hay varios candidatos, comparar identidad, alcance, fuente, vigencia y evidencia; no elegir sólo por fecha ni fusionarlos automáticamente.
5. Consultar `../04_adaptadores/MATRIZ_COMPATIBILIDAD.md` sólo como orientación y declarar capacidades mediante el perfil correspondiente. Para cada capacidad separar estado, evidencia, autorización y vigencia. La evidencia actual prevalece sobre la matriz; una contradicción actual corrige el perfil y marca la orientación para revisión.
6. Seleccionar sólo los módulos cuyo `activate_when` se cumpla y registrar el motivo. La ausencia de un módulo también puede ser una decisión correcta.
7. Presentar el comprobante de arranque en lenguaje sencillo con objetivo, estado, capacidades relevantes, módulos, límites, autorizaciones pendientes y primera acción, sin exceder cinco bloques visibles.
8. Operar en `REPORT` hasta obtener la autoridad necesaria para crear o actualizar estado. Agrupar aprobaciones reversibles y de bajo riesgo cuando su alcance esté claro; solicitar por separado publicar, desplegar, fusionar, borrar, enviar comunicaciones, cambiar permisos, gastar dinero o usar secretos.
9. Antes del primer checkpoint, identificar y cerrar las premisas materiales que podrían invalidar el resultado conforme a `CONTRATO_OPERATIVO.md`.
10. Ejecutar el menor primer checkpoint autorizado, aplicar la revisión previa a la entrega y conservar evidencia.

## Disciplina de interacción y evidencia

- Usar `COMPACT` por defecto: cada comprobante o checkpoint visible debe caber normalmente en 250 palabras y mostrar sólo decisiones, evidencia crítica, incertidumbres, autorización pendiente y siguiente acción. Usar `AUDITABLE` únicamente si la persona lo solicita o si una auditoría exige trazabilidad ampliada.
- Continuar automáticamente entre checkpoints ya autorizados. Detenerse sólo ante una decisión que cambie materialmente el alcance, una contradicción no resoluble, un riesgo nuevo o una acción que requiera autoridad adicional. No pedir “continúa” o “adelante” sin una decisión real.
- No afirmar que un módulo fue aplicado por haberlo nombrado o leído. Cada módulo activado debe producir su evidencia mínima observable: Objetivo, resultado y `Done`; Estado, ubicación, durabilidad, decisiones vigentes, continuidad y siguiente acción; investigación, fuentes y descartes materiales; evidencia, hecho, fuente, inferencia y confianza; voz, patrones concretos derivados de referencias; Equipo, aplicabilidad, nivel, frentes y artefactos; Consejo, expediente, perspectivas y síntesis; Iteración, línea base, criterio predeclarado, veredictos y restauración.
- No declarar una capacidad por inferencia. Demostrarla con una acción verificable y vigente o marcarla `UNKNOWN`, `PARTIAL` o `UNSUPPORTED`.
- No pedir a la persona completar la matriz de compatibilidad. Las diferencias entre productos, interfaces, planes o versiones del mismo proveedor deben comprobarse, no presumirse.
- En trabajos dependientes de hechos actuales, no redactar el entregable hasta cerrar selección de fuentes y suficiencia de evidencia. El comprobante de carga no cierra la investigación.
- Distinguir siempre: estado previo del proyecto, materiales que pueden aprovecharse y referencias de estilo o formato. Uno no implica los otros.
- Tratar la memoria y los proyectos anteriores como antecedentes con procedencia, no como hechos del encargo actual. Confirmar antes de reutilizar temas, casos, estilo, decisiones o datos que cambien materialmente el resultado.
- Mantener internos los nombres de módulos, restricciones y arquitectura salvo que la persona solicite una vista auditable. La entrega final debe usar el formato natural del trabajo, no representar instrucciones del arnés como contenido.
- En interfaces móviles evitar tablas anchas. Presentar matrices como fichas o listas compactas salvo que la persona pida el formato tabular.

## Selección mínima por modo

| Modo | Módulos base | Activación adicional |
| --- | --- | --- |
| `NEW` | Objetivo y Estado | Gobernanza si existen reglas; Equipo sólo si existen frentes independientes y el beneficio justifica la coordinación; el agente elige el nivel |
| `RESUME` | Estado | Objetivo si falta o es inconsistente; Gobernanza si la reanudación modifica un espacio con reglas |
| `VERIFY` | Objetivo y Estado | Evaluador cuando se evalúa la ejecución o madurez; Equipo sólo si la verificación material contiene frentes independientes, mejora con roles separados y las capacidades necesarias están disponibles |

Consejo permanece condicionado a una decisión ambigua, costosa o subjetiva. Iteración se activa sólo cuando varios intentos reversibles puedan compararse contra una validación estable. Ninguno se activa por el solo hecho de iniciar, reanudar o verificar. La persona no elige estos módulos ni configura el loop.

## Reglas de estado

- Proyecto de software: preferir el repositorio o workspace autoritativo cuando exista escritura durable compatible.
- Proyecto documental: preferir la carpeta autoritativa de Drive o almacenamiento equivalente.
- Sin escritura durable: entregar una propuesta exportable, declarar `PARTIAL` y explicar la acción manual mínima.
- Estado ausente: proponer reconstrucción desde fuentes actuales; escribir sólo en `SYNC` autorizado.
- Estado contradictorio: conservar las fuentes, presentar la contradicción y solicitar la decisión mínima si la evidencia no la resuelve.

El comprobante de arranque es una vista. No sustituye ni compite con `PROJECT_STATUS.md` o su equivalente como fuente autoritativa.

`REPORT` y `SYNC` clasifican únicamente la inspección o escritura del estado del proyecto. No conceden ni revocan autoridad para modificar otros artefactos o ejecutar acciones externas; esas acciones se rigen por su alcance autorizado y por `AUTORIDAD_Y_SEGURIDAD.md`.

## Cierre del arranque

El arranque queda listo sólo cuando se conocen: modo, objetivo, fuente de estado, capacidades relevantes, módulos activados, límites, autoridad pendiente y primera acción. Si cualquiera permanece materialmente ambiguo, usar `DECISION_REQUIRED`, `AUTHORITY_REQUIRED` o `BLOCKED_EXTERNAL`; no fingir que el proyecto comenzó.
