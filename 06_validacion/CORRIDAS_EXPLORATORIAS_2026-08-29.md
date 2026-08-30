# Corridas exploratorias multiplataforma — 2026-08-29

## Alcance

Tres ejecuciones reales del mismo escenario general: proyecto documental `NEW` para investigar y redactar un artículo de noticias de precios de transferencia, usando Arnés v0.4.0. Evidencia conservada mediante capturas aportadas por el usuario.

Estas corridas son exploratorias. No constituyen certificación, benchmark estadístico ni evaluación general de los proveedores. Variaron el modelo, la plataforma y algunos intercambios posteriores; sirven para detectar modos de falla del protocolo.

## Resultados observados

| Entorno | Resultado | Fortalezas | Desviaciones materiales |
| --- | --- | --- | --- |
| ChatGPT fuera de Work | Parcialmente conforme, alta calidad | Checkpoints reales, selección y descarte de fuentes, reconstrucción editorial, matriz de evidencia, prudencia inferencial | Exceso de ceremonia, reiteración y confirmaciones vacías; tabla poco usable en móvil |
| Claude | Parcialmente conforme | Carga, clasificación y comprobante claros; experiencia breve | Menor evidencia observable de investigación, reconstrucción y checkpoints; confusión inicial entre estado previo y referencias |
| Gemini Flash | No conforme en la ejecución observada | Identificó manifiesto, versión y modo | Omitió ubicación de estado en preguntas mínimas, declaró módulos/capacidades sin prueba suficiente y comenzó a redactar antes de cerrar evidencia y autorización declarada |

## Cambios derivados para v0.4.1

1. `COMPACT` predeterminado con presupuesto normal de 250 palabras por checkpoint; `AUDITABLE` bajo solicitud o necesidad.
2. Continuación automática entre checkpoints autorizados; pausa sólo ante decisión, riesgo, contradicción o autoridad nueva.
3. Salida mínima observable por módulo; nombrarlo o leerlo no demuestra aplicación.
4. Capacidad demostrada mediante acción vigente o degradada honestamente.
5. Prohibición de redacción prematura en trabajos basados en hechos actuales.
6. Separación de estado previo, materiales reutilizables y referencias de estilo.
7. Distinción explícita entre estado operativo en conversación y estado durable.
8. Representación móvil sin tablas anchas por defecto.

## Próxima validación

Repetir el escenario con v0.4.1 usando instrucciones y respuestas equivalentes. Registrar al menos tres ejecuciones por entorno antes de afirmar comportamiento repetible; cinco ofrecen una base de decisión más fuerte, conforme al manifiesto.
