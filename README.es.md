# Arnés declarativo agnóstico para LLMs

[English](README.md) | [Español](README.es.md)

Creado por **Manuel Carrero Rojo** · Licencia MIT · Versión experimental 0.4.0

**Si no tienes conocimientos técnicos:** abre únicamente [`EMPEZAR_AQUI.md`](EMPEZAR_AQUI.md). Las carpetas restantes son el interior que debe consultar el LLM.

Este es un conjunto accesible y neutral de instrucciones y plantillas para que los LLMs agénticos administren proyectos sustanciales con objetivos claros, estado durable, handoffs seguros, revisión independiente y cierres respaldados por evidencia.

## ¿Qué problema resuelve?

Úsalo cuando una IA olvida decisiones, pierde el estado entre conversaciones, declara terminado sin pruebas suficientes o cuando varios agentes necesitan propiedad y continuidad claras.

Sirve para software, investigaciones, libros, cursos y otros proyectos de varias etapas. No hace falta para preguntas breves, redacciones sencillas o tareas de bajo riesgo que terminan en una conversación.

## Empieza aquí

- Personas no técnicas: abre únicamente [`EMPEZAR_AQUI.md`](EMPEZAR_AQUI.md).
- LLMs agénticos: lee [`HARNESS_MANIFEST.yaml`](HARNESS_MANIFEST.yaml) y después el entrypoint declarado, [`INTERNO_PARA_LLM.md`](INTERNO_PARA_LLM.md).
- Protocolo común para iniciar, continuar o verificar: [`01_nucleo/INICIO_GUIADO.md`](01_nucleo/INICIO_GUIADO.md).
- English version: read [`en/START_HERE.md`](en/START_HERE.md).
- Ejemplo no-código: lee [`05_ejemplos/BOOTSTRAP_NO_CODIGO.md`](05_ejemplos/BOOTSTRAP_NO_CODIGO.md).
- Escenarios de inicio guiado: consulta [`05_ejemplos/ESCENARIOS_INICIO_GUIADO.md`](05_ejemplos/ESCENARIOS_INICIO_GUIADO.md).
- Controles de evaluación: consulta [`06_validacion/CATALOGO_DE_CONTROLES.md`](06_validacion/CATALOGO_DE_CONTROLES.md).
- Política de traducción: consulta [`PARIDAD_BILINGUE.md`](PARIDAD_BILINGUE.md).
- Historial de versiones: consulta [`CHANGELOG.md`](CHANGELOG.md).

El repositorio define un protocolo operativo declarativo, no un runtime autónomo. No proporciona herramientas, memoria, subagentes, permisos o telemetría que la plataforma no tenga.

El inicio guiado pregunta en lenguaje sencillo qué se quiere lograr y dónde conservar el estado. El propio LLM debe comprobar sus capacidades, seleccionar sólo los módulos necesarios, explicar límites y autorizaciones y comenzar por el menor checkpoint autorizado; la persona no configura archivos técnicos.

Para decisiones difíciles, el módulo opcional de Consejo reúne perspectivas independientes, revisa propuestas anonimizadas y produce una síntesis razonada. No trata una votación como prueba ni concede autoridad para actuar.

Archivos del Consejo: [`02_modulos/CONSEJO.md`](02_modulos/CONSEJO.md) y [`03_plantillas/EXPEDIENTE_CONSEJO.template.md`](03_plantillas/EXPEDIENTE_CONSEJO.template.md).

El pulso operativo ofrece una vista breve para saber qué está implementado, comprobado o pendiente y cuál es la siguiente acción. Puede mostrar telemetría sólo si la plataforma la expone; los datos no disponibles permanecen explícitamente desconocidos. Plantilla: [`03_plantillas/PULSO_OPERATIVO.template.md`](03_plantillas/PULSO_OPERATIVO.template.md).

Copyright (c) 2026 Manuel Carrero Rojo.
