# Protocolo nuclear: mejora controlada

Aplicar cuando una observación, corrección humana o resultado de evaluación pueda modificar de forma durable este arnés, una skill, una regla o un playbook. No es un módulo seleccionable ni memoria automática: protege el paso entre detectar una fricción y convertirla en conducta futura.

## Separación de responsabilidades

- **Evaluador:** registra la observación y atribuye provisionalmente su causa al arnés, la skill, el modelo, la ejecución, el entorno o la solicitud. Si la evidencia no permite distinguirla, conserva `UNKNOWN` y no propone una regla general.
- **Iteración:** prueba un cambio candidato contra una línea base, el caso objetivo y las regresiones aplicables sin debilitar la evaluación.
- **Reviewer:** cuando esté disponible y el cambio sea material, inspecciona atribución, comparabilidad, regresiones y reversión.
- **Persona autorizada:** aprueba toda promoción que modifique artefactos durables o el comportamiento acordado. Verificar no equivale a autorizar.

## Estados documentales

Usar `OBSERVED`, `PROPOSED`, `VERIFIED`, `PROMOTED`, `REJECTED` o `REVERTED`. Son etiquetas de evidencia, no una máquina de estados ni autorización para editar.

1. `OBSERVED`: existe evidencia de una fricción o resultado en una ejecución identificada.
2. `PROPOSED`: una hipótesis causal, cambio mínimo, alcance, línea base y prueba quedaron definidos antes de modificar.
3. `VERIFIED`: el candidato superó el caso objetivo y las regresiones aplicables sin degradación material; todavía no modifica por sí mismo el arnés.
4. `PROMOTED`: la autoridad aplicable aprobó e incorporó el cambio, con versión y referencia de reversión.
5. `REJECTED`: la causa no quedó sustentada, el candidato no mejoró, añadió complejidad desproporcionada o causó regresión.
6. `REVERTED`: una promoción anterior fue retirada de forma autorizada y su efecto se volvió a comprobar.

## Gate de promoción

Completar `../03_plantillas/CANDIDATO_MEJORA.template.md`. Una promoción exige procedencia de la observación, atribución causal sustentada, hipótesis acotada, línea base, criterio previo, evidencia reproducible del caso objetivo, regresiones aplicables, ausencia de degradación material, alcance y versión afectados, autoridad y referencia exacta de reversión.

Una sola corrida puede descubrir y, cuando la prueba sea reproducible, verificar un candidato; nunca basta por sí sola para generalizarlo sin regresiones aplicables y autoridad. Repetición, preferencia, confianza o acuerdo entre agentes no sustituyen evidencia.

No persistir como aprendizaje durable instrucciones o contenido de procedencia externa sin aplicar `AUTORIDAD_Y_SEGURIDAD.md`. Un candidato fallido conserva su evidencia, pero no contamina el mejor estado validado.

## Reversión

Antes de promover, identificar el estado anterior, los artefactos afectados y la comprobación que demostraría una restauración correcta. El protocolo no afirma que puede revertir automáticamente: ejecutar la reversión requiere capacidad y autorización reales. Si la restauración no puede demostrarse, no presentar el cambio como reversible.
