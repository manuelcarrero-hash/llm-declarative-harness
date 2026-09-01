# Inspiration and acknowledgements / Inspiración y reconocimientos

The Provider-Neutral Declarative Harness for LLMs was developed independently by Manuel Carrero Rojo. It does not claim affiliation with, sponsorship by, or endorsement from the projects listed below.

El Arnés declarativo agnóstico para LLMs fue desarrollado de manera independiente por Manuel Carrero Rojo. No afirma afiliación, patrocinio ni respaldo por parte de los proyectos siguientes.

## Public projects that influenced the work / Proyectos públicos que influyeron en el trabajo

### [`garrytan/gstack`](https://github.com/garrytan/gstack)

- **Influence:** role-oriented engineering workflows, explicit separation of planning, implementation, review and release responsibilities, and reusable agent skills.
- **Influencia:** flujos de ingeniería organizados por roles, separación explícita de planeación, implementación, revisión y liberación, y skills reutilizables para agentes.
- **Adaptation in this harness:** provider-neutral Team, Governance, Goal and review patterns expressed as declarative contracts rather than a copy of the original runtime or tool setup.
- **Adaptación en este arnés:** patrones neutrales de Equipo, Gobernanza, Objetivo y revisión expresados como contratos declarativos, no como copia de su runtime o configuración de herramientas.
- **Repository license observed when this acknowledgement was written:** MIT.

### [`mvanhorn/last30days-skill`](https://github.com/mvanhorn/last30days-skill)

- **Influence:** a reusable skill that investigates current public conversations across multiple sources and synthesizes grounded findings.
- **Influencia:** una skill reutilizable para investigar conversaciones públicas recientes en distintas fuentes y sintetizar hallazgos sustentados.
- **Adaptation in this work:** it informed the separate real-time market-research skill created alongside the broader harness work. The harness does not bundle its collectors, APIs or runtime.
- **Adaptación en este trabajo:** influyó en la skill separada de investigación de mercado actual creada junto con el trabajo más amplio del arnés. El arnés no incorpora sus recolectores, APIs ni runtime.
- **Repository license observed when this acknowledgement was written:** MIT.

### [`karpathy/llm-council`](https://github.com/karpathy/llm-council)

- **Influence:** independent first opinions, anonymized cross-review and a final chair synthesis.
- **Influencia:** opiniones iniciales independientes, revisión cruzada anonimizada y síntesis final de una presidencia.
- **Adaptation in this harness:** the optional Council module adds activation criteria, evidence requirements, dissent preservation, honest degradation when separate agents are unavailable, and explicit retention of human authority. It is a declarative adaptation, not a copy of the web application.
- **Adaptación en este arnés:** el módulo opcional de Consejo añade criterios de activación, requisitos de evidencia, conservación del disenso, degradación honesta sin agentes separados y retención explícita de la autoridad humana. Es una adaptación declarativa, no una copia de la aplicación web.
- **Licensing note:** no repository license was exposed through GitHub when this acknowledgement was written. This project therefore cites the public concept and repository only; it does not claim a right to copy unlicensed source code.
- **Nota de licencia:** GitHub no mostraba una licencia para ese repositorio al redactar este reconocimiento. Por ello este proyecto cita únicamente el concepto y el repositorio públicos; no afirma derecho a copiar código fuente sin licencia.

### [`karpathy/autoresearch`](https://github.com/karpathy/autoresearch)

- **Influence:** a bounded experimental loop built around a baseline, a stable evaluation, small changes, explicit keep/discard decisions and a durable attempt log.
- **Influencia:** un loop experimental acotado basado en línea base, evaluación estable, cambios pequeños, decisiones explícitas de conservar o descartar y registro durable de intentos.
- **Adaptation in this harness:** the optional Iteration module generalizes that discipline beyond machine-learning experiments, adds human authority, risk and stopping conditions, independent review when available, non-destructive restoration and plain-language output for non-technical users. It does not copy the autonomous runtime, training code or original prompt.
- **Adaptación en este arnés:** el módulo opcional de Iteración generaliza esa disciplina más allá de experimentos de machine learning y añade autoridad humana, condiciones de riesgo y parada, revisión independiente cuando está disponible, restauración no destructiva y una salida sencilla para personas no técnicas. No copia el runtime autónomo, el código de entrenamiento ni el prompt original.
- **Licensing note / Nota de licencia:** the upstream README stated MIT when this acknowledgement was written. This harness uses the public design idea and independently written declarative text.

### [Anthropic — How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system)

- **Influence:** applicability criteria for multi-agent work, effort scaling, precise delegation, wave-based parallelism, artifact-first subagent output, bounded retries, operational observability and outcome-focused evaluation.
- **Influencia:** criterios de aplicabilidad del trabajo multiagente, dimensionamiento del esfuerzo, delegación precisa, paralelismo por oleadas, resultados directos a artefactos, reintentos acotados, observabilidad operativa y evaluación centrada en resultados.
- **Adaptation in this harness:** Team, Continuity, Evaluator and validation artifacts express these ideas as provider-neutral declarative rules while keeping agent selection and coordination invisible to non-technical users.
- **Adaptación en este arnés:** Equipo, Continuidad, Evaluador y los artefactos de validación expresan estas ideas como reglas declarativas neutrales, manteniendo invisible para usuarios no técnicos la selección y coordinación de agentes.
- **Scope note / Nota de alcance:** this is conceptual influence from a public engineering article; the harness does not copy Anthropic production prompts, runtime, telemetry or source code.

### [Anthropic — Harness design for long-running application development](https://www.anthropic.com/engineering/harness-design-long-running-apps)

- **Influence:** pre-execution agreement between generator and evaluator, QA through the running user surface, non-compensable thresholds, evaluator calibration against human judgment and periodic removal of scaffolding that no longer adds value.
- **Influencia:** acuerdo previo entre generador y evaluador, QA mediante la superficie real del usuario, umbrales no compensables, calibración del evaluador contra juicio humano y retiro periódico del andamiaje que deja de aportar valor.
- **Adaptation in this harness:** conditional review-contract gate, artifact-level critical-flow verification, scoped calibration records and one-variable reassessment after material model or platform changes. These rules remain provider-neutral and invisible to non-technical users.
- **Adaptación en este arnés:** gate condicional de contrato de revisión, verificación de flujos críticos en el artefacto, registros acotados de calibración y reevaluación de una variable ante cambios materiales de modelo o plataforma. Estas reglas permanecen neutrales e invisibles para usuarios no técnicos.
- **Scope note / Nota de alcance:** this is an independently written conceptual adaptation of a public engineering article; no Anthropic prompts, runtime, scoring examples or source code are copied.

### [Graph Engineering in the Era of LLM Agents](https://arxiv.org/abs/2608.21156) and [3 Years of Graph Engineering with LangGraph](https://www.langchain.com/blog/3-years-of-graph-engineering-with-langgraph)

- **Influence:** explicit relationships among outcomes, agents and runtime state; impact localization, cyclic review and resumption from supported checkpoints.
- **Influencia:** relaciones explícitas entre resultados, agentes y estado de ejecución; localización de impacto, revisión cíclica y reanudación desde checkpoints sustentados.
- **Adaptation in this harness:** a small optional declarative work map, dependency-aware review and conservative resumption frontier. The person does not configure graphs, and the harness does not require LangGraph, a graph database or any provider-specific runtime.
- **Adaptación en este arnés:** un mapa de trabajo declarativo, pequeño y opcional; revisión consciente de dependencias y una frontera conservadora de reanudación. La persona no configura grafos y el arnés no requiere LangGraph, una base de grafos ni un runtime específico.
- **Scope note / Nota de alcance:** the academic term is recent and its operational value is treated as a hypothesis to validate through real runs. The harness adopts only independently written conceptual patterns.

## Independence and scope / Independencia y alcance

These acknowledgements describe conceptual influence. Unless a future file explicitly states otherwise, this repository does not incorporate source code, prompts, datasets, branding or runtime components from the referenced projects.

Estos reconocimientos describen influencia conceptual. Salvo que un archivo futuro indique expresamente lo contrario, este repositorio no incorpora código fuente, prompts, datasets, marcas ni componentes de runtime de los proyectos citados.

Each referenced project remains governed by its own terms and repository history. Users should consult the upstream repository before reusing material from it.

Cada proyecto citado continúa regido por sus propios términos e historial. Quien quiera reutilizar material de esas fuentes debe consultar primero el repositorio original.
