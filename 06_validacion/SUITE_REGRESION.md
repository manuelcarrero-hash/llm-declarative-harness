# Suite de regresión del Arnés

La suite evalúa resultados y checkpoints materiales; no exige una ruta idéntica entre modelos. Tres corridas siguen siendo el piloto mínimo y cinco una base inicial de decisión. Antes de considerar estable una versión funcional, ejecutar entre 12 y 20 casos representativos, con al menos los 12 siguientes.

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
| R09 | Herramienta con falla transitoria y luego persistente | Continuidad | reintentos y degradación |
| R10 | Intentos `KEEP` y `DISCARD` | Iteración | comparación y restauración |
| R11 | Decisión subjetiva con disenso | Consejo | independencia y evidencia |
| R12 | Usuario no técnico en móvil | Experiencia | lenguaje sencillo y formato |

Añadir hasta ocho casos según riesgos del release: hechos actuales, fuentes insuficientes, pérdida de contexto, herramienta incorrecta, duplicidad entre agentes, presupuesto agotado, integración parcial y falla de despliegue.

## Evidencia por caso

Registrar estímulo, versión, proveedor/modelo/plataforma, capacidades, artefactos, controles aplicables, salida observada, intervención humana y veredicto. Combinar evaluación por reglas con revisión humana de una muestra. Una autoclasificación del agente no prueba el resultado.

## Comparación

Comparar contra la versión anterior por control y escenario. Una corrección es prometedora tras un pase y estable sólo después de sobrevivir otra corrida relevante sin debilitar la prueba.
