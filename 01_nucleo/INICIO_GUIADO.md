# Inicio guiado

Este protocolo convierte una solicitud sencilla en un arranque verificable. Es declarativo: una plataforma compatible lo interpreta, pero el arnés no proporciona por sí mismo herramientas, memoria, permisos ni automatización.

## Modos de entrada

- `NEW`: iniciar un proyecto y crear estado durable cuando esté autorizado.
- `RESUME`: localizar, contrastar y reanudar el estado autoritativo existente.
- `VERIFY`: comprobar en modo de solo lectura si el resultado satisface realmente su condición de terminado.

Las instrucciones listas para copiar y una interfaz guiada son entradas equivalentes al mismo protocolo. No deben producir reglas, módulos o criterios de cierre distintos.

## Tres pilares

1. Preguntar en lenguaje sencillo qué quiere lograr la persona y qué resultado observable demostraría que quedó terminado.
2. Preguntar si ya existe estado del proyecto y dónde está. Si no existe o la persona no sabe dónde guardarlo, recomendar únicamente ubicaciones que la plataforma pueda usar realmente.
3. Evaluar las capacidades del entorno con evidencia. Esta evaluación corresponde al agente, no al usuario. Preguntar sólo cuando una capacidad permanezca `UNKNOWN`, exista más de una fuente autoritativa posible o se requiera autorización.

No pedir al usuario que complete YAML, Markdown, manifiestos, rutas técnicas o una selección manual de módulos. El agente traduce las respuestas al contrato del arnés.

## Secuencia normativa

1. Resolver el modo `NEW`, `RESUME` o `VERIFY` a partir de la solicitud; preguntar sólo si la intención es ambigua.
2. Identificar el proyecto, entorno y fuentes ya disponibles sin realizar sondeos ajenos al alcance.
3. Resolver objetivo y condición observable de terminado. En `RESUME`, conservar el objetivo existente salvo evidencia de que falta, cambió o se contradice.
4. Localizar el estado autoritativo. Si hay varios candidatos, comparar identidad, alcance, fuente, vigencia y evidencia; no elegir sólo por fecha ni fusionarlos automáticamente.
5. Declarar capacidades mediante el perfil correspondiente. Para cada capacidad separar estado, evidencia, autorización y vigencia.
6. Seleccionar sólo los módulos cuyo `activate_when` se cumpla y registrar el motivo. La ausencia de un módulo también puede ser una decisión correcta.
7. Presentar un resumen de arranque en lenguaje sencillo con objetivo, estado, capacidades relevantes, módulos, límites, autorizaciones pendientes y primera acción.
8. Operar en `REPORT` hasta obtener la autoridad necesaria para crear o actualizar estado. Agrupar aprobaciones reversibles y de bajo riesgo cuando su alcance esté claro; solicitar por separado publicar, desplegar, fusionar, borrar, enviar comunicaciones, cambiar permisos, gastar dinero o usar secretos.
9. Ejecutar el menor primer checkpoint autorizado y conservar evidencia.

## Selección mínima por modo

| Modo | Módulos base | Activación adicional |
| --- | --- | --- |
| `NEW` | Objetivo y Estado | Continuidad si cruza sesiones; Gobernanza si existen reglas; Equipo sólo si roles separados mejoran trabajo material |
| `RESUME` | Estado y Continuidad | Objetivo si falta o es inconsistente; Gobernanza si la reanudación modifica un espacio con reglas |
| `VERIFY` | Objetivo y Estado | Evaluador cuando se evalúa la ejecución o madurez; Equipo sólo si una revisión independiente aplicable está disponible |

Consejo permanece condicionado a una decisión ambigua, costosa o subjetiva. No se activa por el solo hecho de iniciar, reanudar o verificar.

## Reglas de estado

- Proyecto de software: preferir el repositorio o workspace autoritativo cuando exista escritura durable compatible.
- Proyecto documental: preferir la carpeta autoritativa de Drive o almacenamiento equivalente.
- Sin escritura durable: entregar una propuesta exportable, declarar `PARTIAL` y explicar la acción manual mínima.
- Estado ausente: proponer reconstrucción desde fuentes actuales; escribir sólo en `SYNC` autorizado.
- Estado contradictorio: conservar las fuentes, presentar la contradicción y solicitar la decisión mínima si la evidencia no la resuelve.

El resumen de arranque es una vista. No sustituye ni compite con `PROJECT_STATUS.md` o su equivalente como fuente autoritativa.

## Cierre del arranque

El arranque queda listo sólo cuando se conocen: modo, objetivo, fuente de estado, capacidades relevantes, módulos activados, límites, autoridad pendiente y primera acción. Si cualquiera permanece materialmente ambiguo, usar `DECISION_REQUIRED`, `AUTHORITY_REQUIRED` o `BLOCKED_EXTERNAL`; no fingir que el proyecto comenzó.
