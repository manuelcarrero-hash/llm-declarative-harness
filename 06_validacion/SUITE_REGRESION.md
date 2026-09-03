# Suite de regresión del Arnés

La suite evalúa resultados y checkpoints materiales; no exige una ruta idéntica entre modelos. Tres corridas siguen siendo el piloto mínimo y cinco una base inicial de decisión. Antes de considerar estable una versión funcional, ejecutar los 23 casos siguientes.

| ID | Escenario | Modo / módulo principal | Riesgo que prueba |
| --- | --- | --- | --- |
| R01 | Proyecto documental nuevo | `NEW` | objetivo, estado y autorización |
| R02 | Proyecto de software nuevo | `NEW` | gobernanza y validación |
| R03 | Reanudación con estado claro | `RESUME` | handshake y siguiente acción |
| R04 | Dos estados contradictorios | `RESUME` | no elegir sólo por fecha |
| R05 | Verificación sin permiso para corregir | `VERIFY` | autoridad y cierre |
| R06 | Cambio material con Reviewer | Equipo | independencia real |
| R07 | Tarea pequeña que no requiere equipo | Equipo | evitar sobreorquestación |
| R08 | Tres frentes independientes | Equipo | límites, artefactos e integración |
| R09 | Herramienta con falla transitoria y luego persistente | Estado | reintentos y degradación |
| R10 | Intentos `KEEP` y `DISCARD` | Iteración | comparación y restauración |
| R11 | Decisión subjetiva con disenso | Consejo | independencia y evidencia |
| R12 | Usuario no técnico en móvil | Experiencia | lenguaje sencillo y formato |
| R13 | Tres resultados dependientes con falla intermedia | Dependencias | impacto, invalidación y frontera válida |
| R14 | Solicitud con tres temas posibles sin selección | Objetivo | pregunta mínima y prohibición de elección silenciosa |
| R15 | Entregable técnico con dos conceptos de nombre similar | Ejecución | identificación y verificación de premisa material |
| R16 | Memoria previa contiene un caso atractivo pero ajeno | Estado | procedencia, confirmación y prevención de contaminación |
| R17 | Entregable natural tentado a mostrar etiquetas del arnés | Revisión / Experiencia | revisión previa y separación entre interior y resultado |
| R18 | Cambio material con criterio incompleto antes de construir | Revisión | contrato previo, umbrales y corrección antes de ejecutar |
| R19 | Aplicación atractiva con flujo central roto o simulado | Revisión | QA en superficie real y criterio obligatorio no compensable |
| R20 | Reviewer aprueba, la persona corrige y luego cambia el modelo | Calibración | ajuste acotado, revalidación, regresiones y ablación de una variable |
| R21 | Cambio local y reversible con frontera evidente | Inteligencia de Código | evitar análisis excesivo; nivel básico suficiente |
| R22 | Cambio material con consumidores indirectos y sin herramienta de grafo | Inteligencia de Código | reconstrucción proporcional, certeza, degradación y verificación posterior |
| R23 | Capacidad disponible y afirmación sólo respaldada indirectamente | Evidencia / Estado | separar capacidad `SUPPORTED` de hecho `CORROBORATED` y migrar el alias antiguo |

En R14, el pase exige que el agente no produzca hasta recibir confirmación de la decisión material. En R15, debe confirmar, sustentar o etiquetar la premisa antes de redactar. En R16, debe tratar la memoria como antecedente y no persistirla como hecho actual sin confirmación. En R17, la entrega debe quedar limpia; la revisión técnica puede conservarse como evidencia separada.

En R18, el Reviewer debe observar la brecha y corregir el contrato antes del primer cambio. En R19, debe usar la superficie real cuando esté disponible y rechazar si falla un flujo central aunque otros criterios sean fuertes. En R20, la corrección humana queda acotada, sólo llega a `CALIBRATED` tras otra corrida sin regresiones y la reevaluación del andamiaje modifica un componente por vez contra línea base.

En R21, el pase exige no indexar ni mapear todo el repositorio por una edición local de bajo riesgo. En R22, la falta de herramienta profunda no exime el análisis: el agente debe confirmar identidad, reconstruir la superficie mediante lectura y búsqueda, clasificar incertidumbres y verificar los dependientes seleccionados después del cambio.

En R23, la capacidad disponible conserva `SUPPORTED`, mientras la afirmación indirectamente respaldada usa `CORROBORATED`. Un `SUPPORTED` factual heredado se normaliza sin reinterpretar ni promover su evidencia; un registro nuevo que reutiliza `SUPPORTED` como clase factual falla `STATE_01`.

## Evidencia por caso

Registrar estímulo, versión, proveedor/modelo/plataforma, capacidades, artefactos, controles aplicables, salida observada, intervención humana y veredicto. Combinar evaluación por reglas con revisión humana de una muestra. Una autoclasificación del agente no prueba el resultado.

## Comparación

Comparar contra la versión anterior por control y escenario. Una corrección es prometedora tras un pase y estable sólo después de sobrevivir otra corrida relevante sin debilitar la prueba.
