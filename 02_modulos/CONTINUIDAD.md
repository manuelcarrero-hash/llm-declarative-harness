# Módulo: continuidad de contexto

Proteger decisiones, evidencia, estado parcial, artefactos y siguiente acción cuando el trabajo cruce agentes, sesiones, compactación, fallas o fases.

## Umbrales

Usar porcentajes sólo si existe telemetría real y se conoce la capacidad total. Política por defecto: checkpoint preventivo al 30% medido y rotación al 40% medido. Sin telemetría, usar señales cualitativas y declarar el porcentaje como desconocido.

En cada checkpoint relevante, actualizar o enlazar el pulso operativo: fase, estados de entrega, última comprobación, riesgo, estado de continuidad y siguiente acción. Etiquetar fuente y vigencia de toda señal de runtime. `UNKNOWN` no es una falla; inventar precisión sí lo es.

## Artefactos entre agentes

Cuando la plataforma lo permita, cada agente guarda directamente su salida material en el workspace durable y entrega al sucesor o Lead una referencia, estado, evidencia, brechas e incertidumbres. No canalizar artefactos completos por resúmenes sucesivos si pueden conservarse en origen.

El receptor debe leer el artefacto autoritativo cuando una síntesis pueda perder precisión. Una referencia rota o un artefacto no verificable no constituye handoff completo.

## Fallas y reanudación

Aplicar la taxonomía y presupuesto de reintentos de `../01_nucleo/CONTRATO_OPERATIVO.md`. Antes de reiniciar trabajo costoso, conservar el último checkpoint seguro, la causa observable, intentos realizados y la alternativa siguiente. Reanudar desde el checkpoint; no empezar de cero salvo que la evidencia muestre corrupción o incompatibilidad.

## Rotación

Llegar a un límite atómico seguro; escribir handoff; verificarlo contra fuentes; sincronizar estado autorizado; iniciar sucesor con contexto mínimo; exigir handshake antes de editar; relevar al anterior sólo después del handshake.

No fingir que se detuvo, persistió, reanudó o creó una sesión si la plataforma no lo permite.
