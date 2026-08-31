# Módulo: iteración verificable

Activar cuando el resultado mejore mediante varios intentos reversibles que puedan compararse contra una validación estable. No activar para tareas breves, cambios obvios, acciones irreversibles o trabajos donde experimentar aumente materialmente el riesgo.

El usuario no configura este módulo ni necesita conocer su mecánica. El agente decide si corresponde, lo explica como “probar cambios pequeños y conservar sólo los que demuestren una mejora” y solicita únicamente las decisiones o autorizaciones materiales.

## Condiciones de entrada

Antes del primer intento deben existir:

- una línea base observada o una razón explícita por la que no puede obtenerse;
- una brecha concreta y una hipótesis comprobable;
- una validación y criterio de aceptación definidos antes del cambio;
- un espacio modificable delimitado y una evaluación protegida de alteraciones oportunistas;
- una forma segura de restaurar el mejor estado validado;
- un presupuesto o condición de parada compatible con la autoridad concedida.

Si falta una condición material, usar `BLOCKED`, `DECISION_REQUIRED` o `AUTHORITY_REQUIRED`; no fingir comparabilidad.

## Loop

1. Confirmar el mejor estado validado y su evidencia.
2. Elegir una sola hipótesis o un conjunto mínimo inseparable.
3. Predeclarar cambio, validación, criterio, riesgos y restauración.
4. Aplicar el menor cambio reversible autorizado.
5. Ejecutar la validación sin debilitarla para favorecer el intento.
6. Comparar contra la línea base, todos los criterios obligatorios y posibles regresiones.
7. Emitir un veredicto:
   - `KEEP`: mejora suficiente y sin regresión inaceptable; pasa a ser el mejor estado validado.
   - `REVISE`: evidencia prometedora pero insuficiente; no cuenta como validado.
   - `DISCARD`: no mejora, agrega complejidad desproporcionada o causa regresión; restaurar.
   - `CRASH`: el intento no pudo ejecutarse por una falla propia; restaurar.
   - `BLOCKED`: una dependencia externa impide evaluarlo.
   - `ESCALATE`: continuar requiere decisión o autoridad nueva.
8. Registrar evidencia, aprendizaje, estado final y ruta siguiente.
9. Continuar automáticamente sólo dentro del alcance, riesgo y presupuesto autorizados.

Un intento fallido puede aportar aprendizaje, pero no puede contaminar el mejor estado validado. Nunca borrar el registro para aparentar una secuencia limpia.

## Revisión

Cuando exista Reviewer independiente, debe inspeccionar el cambio real y además comprobar comparabilidad, integridad de la validación, regresiones, costo de complejidad y restauración. El Builder no obtiene aprobación por su propia afirmación.

Si existe un mapa de trabajo activo, cada hallazgo material debe identificar el resultado directo, la evidencia fallida o faltante y los dependientes potencialmente afectados. Un `KEEP` no conserva automáticamente resultados descendientes: revalidarlos cuando la dependencia o el impacto lo exijan.

Si la plataforma no permite independencia, declarar la degradación. El agente puede ejecutar pruebas deterministas, pero no presentar su autoevaluación como revisión independiente.

## Simplicidad y parada

A resultados equivalentes, preferir la alternativa más simple y mantenible. Una mejora marginal no justifica complejidad, costo o riesgo desproporcionados.

Detener el loop ante objetivo alcanzado, presupuesto agotado, rendimientos decrecientes, pérdida de comparabilidad, riesgo nuevo, contradicción material, autoridad nueva o intervención del usuario. No usar autonomía como permiso para operar indefinidamente.
