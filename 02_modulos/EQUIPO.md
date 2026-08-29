# Módulo: equipo agéntico

Usar roles reales cuando la plataforma permita agentes separados y la independencia mejore la corrección.

## Roles mínimos

- **Lead:** contrato, autoridad, integración y cierre.
- **Builder:** implementación acotada y pruebas.
- **Reviewer:** inspección independiente del cambio real; veredicto `APPROVED` o `CHANGES_REQUIRED`.

Añadir QA, seguridad, diseño o investigación sólo cuando exista una frontera útil. Un mismo agente interpretando varios personajes no prueba independencia.

Evitar escrituras concurrentes sobre el mismo archivo. Cada asignación debe incluir directorio, reglas aplicables, límites, entregable y evidencia de cierre.
