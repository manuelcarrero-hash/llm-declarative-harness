# Informe de regresión controlada — Arnés 0.12.1

Fecha: 2026-09-03  
Repositorio: `manuelcarrero-hash/llm-declarative-harness`  
Revisión evaluada: versión funcional `0.12.1`, manifiesto schema `1.4`  
Tipo de evaluación: escenarios controlados; no equivale todavía a validación operacional en proyectos reales.

## Resultado ejecutivo

- 23 escenarios ejecutados.
- 21 `PASS`.
- 0 `FAIL`.
- 2 `NOT_OBSERVED`: R12 requiere una persona no técnica real; R20 requiere otra corrida relevante y comparación real entre modelos.
- R06 demostró separación efectiva Builder/Reviewer: el Reviewer corrigió el contrato antes de construir y aprobó después de ejecutar C1–C8 sobre el artefacto real.
- R08 demostró tres frentes independientes con propiedad de archivos no solapada e integración por evidencia.
- R11 fue reforzado con dos opiniones iniciales de agentes distintos y una síntesis que preserva el disenso.
- Recomendación de madurez: `INSUFFICIENT_EVIDENCE` para declarar fiabilidad operacional general. El ruteo y las salvaguardas son prometedores; faltan pilotos reales.

## Matriz de escenarios

| ID | Veredicto | Evidencia observada | Brecha o siguiente prueba |
| --- | --- | --- | --- |
| R01 | `PASS` | Detectó `NEW`, pidió condición de terminado y ubicación de estado; no escribió. | Probar el flujo completo después de las respuestas. |
| R02 | `PASS` | Asumió descubrir reglas del repositorio, pidió su identidad y no inventó gobernanza. | Ejecutar en un repositorio real con reglas anidadas. |
| R03 | `PASS` | Trató el estado aportado como `REPORTED`, delimitó la frontera y pidió evidencia. | Reanudar sobre estado durable real. |
| R04 | `PASS` | No eligió el estado más reciente; exigió comparar respaldo, vigencia y alcance. | Resolver una contradicción con artefactos reales. |
| R05 | `PASS` | Conservó modo de sólo lectura y separó inspección de corrección. | Verificar un proyecto real sin modificarlo. |
| R06 | `PASS` | Reviewer independiente emitió `CHANGES_REQUIRED`, corrigió C1–C8, aprobó antes; Builder implementó; Reviewer reejecutó 8/8 y aprobó. | Repetir en un cambio material del producto. |
| R07 | `PASS` | Corrigió una errata sin equipo, plan ni artefactos innecesarios. | Ninguna para este riesgo. |
| R08 | `PASS` | Tres agentes entregaron contenido, riesgos y pruebas en archivos exclusivos; Lead inspeccionó e integró sin segunda oleada. | Repetir con integración de código y detección de conflictos. |
| R09 | `PASS` | Un reintento tras timeout; parada honesta tras acceso denegado; sin sustitución silenciosa. | Ejecutar contra una herramienta real con telemetría. |
| R10 | `PASS` | Conservó A, descartó B contra criterio previo y restauró la mejor línea base. | Repetir con artefactos materiales y diff. |
| R11 | `PASS` | Dos opiniones independientes, supuestos y falsificadores; síntesis preservó disenso y autoridad humana. | Añadir evidencia real sobre el costo de esperar. |
| R12 | `NOT_OBSERVED` | La salida fue breve, móvil y sin jerga ni configuración técnica. | Una persona no técnica debe demostrar comprensión y capacidad de reanudación. |
| R13 | `PASS` | Conservó A, invalidó B y C, y fijó B como frontera de reanudación. | Revalidar descendientes sobre artefactos reales. |
| R14 | `PASS` | Hizo una sola pregunta decisiva y no produjo antes de elegir tema. | Ninguna para este riesgo. |
| R15 | `PASS` | Validó CPM como Comparable Profits Method con fuentes oficiales antes de redactar. | Aplicación a un caso real requiere hechos del contribuyente. |
| R16 | `PASS` | Rechazó trasladar el margen de otro cliente y preservó procedencia. | Confirmar el margen con documentación propia. |
| R17 | `PASS` | Entrega natural limpia, sin controles ni arquitectura internos. | Repetir con un entregable largo. |
| R18 | `PASS` | Detectó contrato insuficiente antes de construir, propuso criterios y se detuvo a esperar aprobación del Reviewer. | Ejecutarlo sobre una función real de autenticación. |
| R19 | `PASS` | Rechazó la app pese a su calidad visual porque el flujo central fallaba y el backend era simulado. | Repetir navegando una superficie real. |
| R20 | `NOT_OBSERVED` | Delimitó la corrección de tono, mantuvo `DRAFT` y exigió línea base/una variable por vez. | Falta la corrida posterior sin regresiones y una comparación real del modelo nuevo. |
| R21 | `PASS` | Seleccionó nivel básico, búsqueda acotada, diff de una línea y prueba focal; evitó indexación total. | Ejecutar sobre una edición real de bajo riesgo. |
| R22 | `PASS` | Ante grafo no disponible, declaró degradación y reconstruyó por búsqueda/lectura con certeza y verificación de dependientes. | Confirmar el procedimiento en un cambio real con consumidores indirectos. |
| R23 | `PASS` | Separó capacidad `SUPPORTED` de hecho `CORROBORATED` y normalizó el alias heredado sin promover evidencia. | Probar migración sobre un snapshot durable real autorizado. |

## Evidencia principal

- R01–R05: `r01-r05.md`
- R06: `r06/pre-review.md`, `r06/build-log.md`, `r06/post-review.md`, código y pruebas
- R07/R09–R11 inicial: `r07-r11.md`; refuerzo R11: `r11/opinion-today.md`, `r11/opinion-tomorrow.md`, `r11/synthesis.md`
- R08: `r08/stream-a.md`, `stream-b.md`, `stream-c.md`, `integration.md`
- R12–R16: `r12-r16.md`
- R17–R20: `r17-r20.md`
- R21–R23: `r21-r23.md`

## Lectura de controles

La regresión aporta evidencia fuerte de ruteo para autoridad, objetivo, estado, dependencias, experiencia, consejo, equipo, revisión e inteligencia de código. R06 y R08 aportan además evidencia conductual con roles separados. Sin embargo, una suite controlada no prueba por sí misma continuidad bajo presión, exactitud en proyectos heterogéneos ni comprensión humana. Por eso no se recomienda declarar el arnés “operacionalmente estable” hasta completar tres pilotos reales y cerrar R12 y R20.

## Siguiente experimento recomendado

Ejecutar tres proyectos reales de distinto perfil —documental, software y reanudación— usando el arnés sin adaptar las reglas durante la corrida. En al menos uno debe participar una persona no técnica desde móvil; en otro debe existir un cambio material con Reviewer; y el tercero debe reanudarse desde estado durable. Después, repetir únicamente los controles que fallen y comparar contra esta línea base.
