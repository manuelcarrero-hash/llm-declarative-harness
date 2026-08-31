# Arnés declarativo agnóstico para LLMs

[English](README.md) | [Español](README.es.md)

Creado por **Manuel Carrero Rojo** · Licencia MIT · Versión experimental 0.6.0

**Si no tienes conocimientos técnicos:** abre únicamente [`EMPEZAR_AQUI.md`](EMPEZAR_AQUI.md). Las carpetas restantes son el interior que debe consultar el LLM.

Este es un arnés bilingüe y neutral que permite iniciar, continuar y verificar proyectos sustanciales con un LLM sin pedir al usuario configurar archivos técnicos. Conserva estado durable, hace visibles capacidades y permisos, exige evidencia antes de declarar terminado y, cuando corresponde, permite probar cambios pequeños y conservar sólo los que demuestren una mejora.

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
- Controles de evaluación: consulta [`06_validacion/CATALOGO_DE_CONTROLES.md`](06_validacion/CATALOGO_DE_CONTROLES.md) y la [`suite de regresión`](06_validacion/SUITE_REGRESION.md).
- Política de traducción: consulta [`PARIDAD_BILINGUE.md`](PARIDAD_BILINGUE.md).
- Historial de versiones: consulta [`CHANGELOG.md`](CHANGELOG.md).

El repositorio define un protocolo operativo declarativo, no un runtime autónomo. No proporciona herramientas, memoria, subagentes, permisos o telemetría que la plataforma no tenga.

El inicio guiado pregunta en lenguaje sencillo qué se quiere lograr y dónde conservar el estado. El propio LLM comprueba sus capacidades, selecciona sólo los módulos necesarios, explica límites y autorizaciones y comienza por el menor checkpoint autorizado; la persona no configura archivos técnicos, roles ni agentes.

Cuando existen frentes realmente independientes, Equipo dimensiona internamente el esfuerzo como individual, enfocado o amplio, delega por oleadas y conserva los resultados en artefactos verificables. Para tareas pequeñas evita crear agentes innecesarios. Archivos internos: [`02_modulos/EQUIPO.md`](02_modulos/EQUIPO.md), [`03_plantillas/ASIGNACION_AGENTE.template.md`](03_plantillas/ASIGNACION_AGENTE.template.md) y [`03_plantillas/TRAZA_ORQUESTACION.template.md`](03_plantillas/TRAZA_ORQUESTACION.template.md).

Para decisiones difíciles, el módulo opcional de Consejo reúne perspectivas independientes, revisa propuestas anonimizadas y produce una síntesis razonada. No trata una votación como prueba ni concede autoridad para actuar.

Cuando un trabajo mejora mediante varios intentos comparables, el módulo opcional de Iteración establece una línea base, prueba cambios reversibles y registra qué se conserva o descarta. La persona no configura el loop: recibe únicamente una explicación sencilla de lo probado, el resultado y el siguiente paso. Archivos: [`02_modulos/ITERACION.md`](02_modulos/ITERACION.md) y [`03_plantillas/REGISTRO_ITERACIONES.template.md`](03_plantillas/REGISTRO_ITERACIONES.template.md).

Archivos del Consejo: [`02_modulos/CONSEJO.md`](02_modulos/CONSEJO.md) y [`03_plantillas/EXPEDIENTE_CONSEJO.template.md`](03_plantillas/EXPEDIENTE_CONSEJO.template.md).

El pulso operativo ofrece una vista breve para saber qué está implementado, comprobado o pendiente y cuál es la siguiente acción. Puede mostrar telemetría sólo si la plataforma la expone; los datos no disponibles permanecen explícitamente desconocidos. Plantilla: [`03_plantillas/PULSO_OPERATIVO.template.md`](03_plantillas/PULSO_OPERATIVO.template.md).

## Inspiración y reconocimientos

El arnés fue desarrollado de manera independiente, pero reconoce ideas públicas que influyeron en skills y módulos incorporados posteriormente a este protocolo: [`garrytan/gstack`](https://github.com/garrytan/gstack), [`mvanhorn/last30days-skill`](https://github.com/mvanhorn/last30days-skill), [`karpathy/llm-council`](https://github.com/karpathy/llm-council) y [`karpathy/autoresearch`](https://github.com/karpathy/autoresearch) y el artículo de Anthropic [`How we built our multi-agent research system`](https://www.anthropic.com/engineering/multi-agent-research-system). Consulta el alcance exacto de cada influencia y las aclaraciones de licencia en [`ACKNOWLEDGEMENTS.md`](ACKNOWLEDGEMENTS.md).

No existe afiliación, patrocinio ni respaldo por parte de sus autores o mantenedores.

Copyright (c) 2026 Manuel Carrero Rojo.
