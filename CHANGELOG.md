# Changelog / Registro de cambios

## 0.12.1 — 2026-09-03

### Español

- `CORROBORATED` sustituye a `SUPPORTED` como clase factual de respaldo indirecto; `SUPPORTED` queda reservado exclusivamente para capacidad.
- El manifiesto 1.4 declara `factual_legacy_aliases: {SUPPORTED: CORROBORATED}` para interpretar registros anteriores sin promover su evidencia.
- Plantillas, Inteligencia de Código, Estado y Contrato Operativo usan la nueva etiqueta sin cambiar las demás dimensiones.
- Se añadió R23 y la suite vigente pasa a 23 escenarios para detectar usos factuales nuevos de `SUPPORTED`.

### English

- `CORROBORATED` replaces `SUPPORTED` as the factual class for indirect support; `SUPPORTED` is now reserved exclusively for capability.
- Manifest 1.4 declares `factual_legacy_aliases: {SUPPORTED: CORROBORATED}` to interpret prior records without promoting their evidence.
- Templates, Code Intelligence, Status and the Operating Contract use the new label without changing other dimensions.
- Added R23 and raised the current suite to 23 scenarios to detect new factual uses of `SUPPORTED`.

## 0.12.0 — 2026-09-03

### Español

- Se unificaron premisas, afirmaciones, telemetría y relaciones en una taxonomía factual: `CONFIRMED`, `SUPPORTED`, `REPORTED`, `INFERRED`, `PLANNED` y `UNKNOWN`.
- Las etiquetas factuales quedaron separadas explícitamente de capacidad, autorización, progreso y veredictos.
- Estado del Proyecto absorbió continuidad, checkpoints, artefactos, reanudación y rotación; `CONTINUIDAD.md` permanece como alias de compatibilidad y ya no se activa como segundo módulo.
- La prueba de conformidad se redujo de una copia extensa de obligaciones a un procedimiento de seis pasos que usa el Catálogo de Controles y la Suite de Regresión como fuentes normativas.
- El esquema del manifiesto avanzó a 1.3; se preservaron rutas antiguas, IDs de control y los 22 escenarios.

### English

- Unified premises, claims, telemetry and relationships under one factual taxonomy: `CONFIRMED`, `SUPPORTED`, `REPORTED`, `INFERRED`, `PLANNED` and `UNKNOWN`.
- Explicitly separated factual labels from capability, authorization, progress and verdict labels.
- Project Status absorbed continuity, checkpoints, artifacts, resumption and rotation; `CONTINUITY.md` remains a compatibility alias and is no longer activated as a second module.
- Reduced the conformance test from an extensive duplicate of obligations to a six-step procedure using the Control Catalog and Regression Suite as normative sources.
- Advanced the manifest schema to 1.3 while preserving legacy paths, control IDs and all 22 scenarios.

## 0.11.0 — 2026-09-02

### Español

- Se unificaron comprobante y resumen en una sola vista de arranque auditable; las plantillas antiguas de resumen permanecen como rutas de compatibilidad y no deben generar un segundo artefacto.
- Las diez invariantes se consolidaron en seis obligaciones equivalentes, sin reducir límites de autoridad, evidencia, cierre o calibración.
- El Contrato Operativo ahora declara la propiedad normativa de reglas transversales; Equipo, Consejo, Iteración e Inteligencia de Código referencian el núcleo y conservan sólo su comportamiento diferencial.
- El Evaluador toma la lista vigente del Catálogo de Controles, cubre explícitamente Inteligencia de Código y exige los 22 escenarios actuales, eliminando números y enumeraciones duplicados que habían quedado obsoletos.
- Se preservaron rutas, IDs, taxonomías y comportamiento funcional para que esta consolidación sea compatible con consumidores existentes.

### English

- Unified receipt and summary into one auditable startup view; legacy summary templates remain as compatibility paths and must not create a second artifact.
- Consolidated ten invariants into six equivalent obligations without reducing authority, evidence, closure or calibration limits.
- The Operating Contract now declares normative ownership of cross-cutting rules; Team, Council, Iteration and Code Intelligence reference the core and retain only differential behavior.
- The Evaluator takes the current list from the Control Catalog, explicitly covers Code Intelligence and requires all 22 current scenarios, removing stale duplicated counts and enumerations.
- Preserved paths, IDs, taxonomies and functional behavior so the consolidation remains compatible with existing consumers.

## 0.10.0 — 2026-09-02

### Español

- Se añadió el módulo opcional y agnóstico de Inteligencia de Código para reconstruir proporcionalmente la superficie afectada antes de cambios técnicos materiales.
- Se definieron niveles BÁSICO, ESTRUCTURAL y PROFUNDO, independientes de cualquier herramienta o proveedor.
- Las relaciones materiales se clasifican como CONFIRMED, SUPPORTED, INFERRED o UNKNOWN; las incertidumbres capaces de invalidar el cambio deben resolverse, acotarse o elevarse antes de ejecutar.
- Índices, LSP y grafos como Codebase Memory MCP son aceleradores opcionales; el arnés conserva una ruta por lectura directa y no instala servicios persistentes sin autoridad.
- La verificación posterior exige revisar diff, dependientes y pruebas o flujos seleccionados, sin sustituir Git, PROJECT_STATUS, QA ni revisión humana.
- Se añadió CODE_INTELLIGENCE_01, el esquema de evaluación 1.9, los casos R21–R22, gates de conformidad y paridad bilingüe.
- Se reconoció la influencia conceptual de DeusData/codebase-memory-mcp sin incorporar su runtime o código fuente.

### English

- Added the optional provider-neutral Code Intelligence module to proportionally reconstruct the affected surface before material technical changes.
- Defined BASIC, STRUCTURAL and DEEP levels independent of any tool or provider.
- Material relationships are classified as CONFIRMED, SUPPORTED, INFERRED or UNKNOWN; uncertainty capable of invalidating the change must be resolved, bounded or escalated before execution.
- Indexes, LSP and graphs such as Codebase Memory MCP are optional accelerators; the harness retains direct reading and installs no persistent service without authority.
- Post-change verification requires inspecting the diff, dependents and selected tests or flows without replacing Git, PROJECT_STATUS, QA or human review.
- Added CODE_INTELLIGENCE_01, evaluation schema 1.9, R21–R22, conformance gates and bilingual parity.
- Acknowledged conceptual influence from DeusData/codebase-memory-mcp without incorporating its runtime or source code.

## 0.9.0 — 2026-09-01

### Español

- El Reviewer independiente ahora inspecciona el contrato de validación antes de ejecutar cambios materiales, incluidos comportamientos, flujos críticos, evidencia y umbrales de rechazo.
- Cuando existe artefacto ejecutable y capacidad, la revisión recorre la superficie real del usuario y contrasta efectos observables; diff, captura o reporte del Builder no sustituyen QA end-to-end.
- Cada criterio obligatorio tiene umbral propio: una aprobación global o promedio alto no compensa una función central fallida.
- Se añadió calibración acotada del Reviewer ante discrepancias humanas materiales, con estado `CALIBRATED` sólo después de otra corrida relevante sin regresiones.
- Cambios significativos de modelo o plataforma activan reevaluación del andamiaje contra línea base y una variable por vez; se conserva la solución más simple que mantenga controles críticos.
- Se incorporó la plantilla bilingüe de calibración, `CALIBRATION_01`, esquema de evaluación 1.8 y los casos R18–R20.
- La experiencia no técnica no cambia: negociación, QA y calibración son internas; sólo se escalan decisiones materiales o límites reales.
- Se reconoció la influencia conceptual del artículo de Anthropic sobre diseño de arneses para aplicaciones de larga duración.

### English

- The independent Reviewer now inspects the validation contract before material execution, including behaviors, critical flows, evidence and rejection thresholds.
- When an executable artifact and capability exist, review exercises the real user surface and verifies observable effects; a diff, screenshot or Builder report does not replace end-to-end QA.
- Every mandatory criterion has its own threshold: global approval or a high average cannot compensate for a failed core function.
- Added scoped Reviewer calibration after material human disagreement, with `CALIBRATED` available only after another relevant regression-free run.
- Significant model or platform changes trigger scaffolding reassessment against a baseline one variable at a time; the simplest solution preserving critical controls wins.
- Added the bilingual calibration template, `CALIBRATION_01`, evaluation schema 1.8 and R18–R20.
- The non-technical experience is unchanged: negotiation, QA and calibration stay internal; only material decisions or real limits are escalated.
- Acknowledged conceptual influence from Anthropic's article on harness design for long-running applications.

## 0.8.0 — 2026-09-01

### Español

- Dos pruebas independientes con Claude y Gemini evidenciaron la misma falla: producir antes de cerrar una decisión material y validar la premisa técnica central.
- Se añadió un gate de especificación: ejemplos, listas y temas posibles no autorizan elecciones silenciosas; el agente hace la pregunta mínima o recomienda y espera confirmación.
- Se exige clasificar las premisas capaces de invalidar el resultado como `CONFIRMED`, `SUPPORTED`, `ASSUMPTION` o `UNKNOWN` antes de producir.
- Toda entrega incorpora una revisión interna proporcional contra decisiones inventadas, confusiones, afirmaciones sin sustento, incumplimiento del objetivo y exposición innecesaria del arnés; los cambios materiales conservan Reviewer independiente.
- El estado ahora separa hechos actuales, antecedentes, materiales, estilo, propuestas y supuestos con procedencia, y exige rectificar cualquier contaminación.
- Se fortalecieron `GOAL_01`, `REVIEW_01`, `STATE_01`, `EXECUTION_01` y `EXPERIENCE_01`, se añadieron R14–R17 y el esquema de evaluación avanzó a 1.7.
- La experiencia no técnica permanece ligera: estas comprobaciones son internas y la entrega conserva su formato natural.

### English

- Two independent Claude and Gemini tests exposed the same failure: producing before closing a material decision and validating the central technical premise.
- Added a specification gate: examples, lists and possible topics do not authorize silent choices; the agent asks the minimum question or recommends and waits for confirmation.
- Premises capable of invalidating the outcome must be classified as `CONFIRMED`, `SUPPORTED`, `ASSUMPTION` or `UNKNOWN` before production.
- Every deliverable receives a proportional internal review for invented decisions, confusions, unsupported claims, objective compliance and unnecessary harness exposure; material changes retain independent Reviewer requirements.
- Status now separates current facts, background, materials, style, proposals and assumptions with provenance, and requires repair of any contamination.
- Strengthened `GOAL_01`, `REVIEW_01`, `STATE_01`, `EXECUTION_01` and `EXPERIENCE_01`, added R14–R17 and advanced the evaluation schema to 1.7.
- The non-technical experience remains light: these checks stay internal and the deliverable keeps its natural format.

## 0.7.0 — 2026-08-31

### Español

- Se añadió un mapa interno de trabajo, opcional y derivado, sólo para tres o más resultados materiales con dependencias observables.
- Los hallazgos del Reviewer ahora vinculan resultado directo, evidencia fallida o faltante y dependientes que requieren nueva validación.
- Se definió una frontera válida para conservar trabajo comprobado y reanudar parcialmente; la ambigüedad obliga a invalidar y ampliar la reverificación.
- Se incorporaron la plantilla bilingüe de mapa, campos de estado y traza, el control crítico condicional `DEPENDENCY_01` y el escenario de regresión R13.
- Se mantuvo la experiencia no técnica: la persona no configura grafos, relaciones ni archivos y recibe únicamente qué está comprobado, qué se corregirá y desde dónde se retomará.
- Se reconoció la influencia conceptual del survey de Graph Engineering y del análisis de LangChain sin incorporar su runtime.

### English

- Added an optional derived internal work map only for three or more material outcomes with observable dependencies.
- Reviewer findings now link direct outcome, failed or missing evidence and dependents requiring renewed validation.
- Defined a valid frontier for preserving verified work and resuming partially; ambiguity requires invalidation and wider reverification.
- Added the bilingual work-map template, state and trace fields, conditional critical control `DEPENDENCY_01`, and regression scenario R13.
- Preserved the non-technical experience: the person configures no graphs, relationships or files and sees only what is verified, what will be corrected and where work will resume.
- Acknowledged conceptual influence from the Graph Engineering survey and LangChain analysis without incorporating their runtime.

## 0.6.0 — 2026-08-31

### Español

- Equipo ahora exige frentes independientes y beneficio proporcional antes de activar varios agentes.
- Se añadieron niveles internos `SINGLE`, `FOCUSED` y `BROAD`, delegación por oleadas y presupuesto.
- Se incorporaron plantillas bilingües de asignación y traza operativa sin cadena de pensamiento.
- Los agentes especializados conservan artefactos directamente y el Lead integra por referencia.
- Se añadió taxonomía de fallas, reintentos acotados y reanudación desde checkpoints.
- Se añadió el control crítico `ORCHESTRATION_01` y esquema de evaluación 1.5.
- Se creó una suite bilingüe de regresión de 12–20 escenarios antes de considerar estable una versión funcional.
- Se mantuvo la experiencia no técnica: el agente decide internamente roles, nivel, herramientas y oleadas.
- GitHub `main` quedó declarado como fuente canónica y Drive como réplica.
- Se reconoció la influencia conceptual del artículo de ingeniería multiagente de Anthropic.

### English

- Team now requires independent workstreams and proportional benefit before activating multiple agents.
- Added internal `SINGLE`, `FOCUSED` and `BROAD` levels, wave-based delegation and budget.
- Added bilingual assignment and operational-trace templates without chain of thought.
- Specialist agents preserve artifacts directly and the Lead integrates by reference.
- Added failure taxonomy, bounded retries and checkpoint resumption.
- Added critical control `ORCHESTRATION_01` and evaluation schema 1.5.
- Created a bilingual 12–20 scenario regression suite before treating a functional version as stable.
- Preserved the non-technical experience: the agent internally decides roles, level, tools and waves.
- Declared GitHub `main` as canonical source and Drive as mirror.
- Acknowledged conceptual influence from Anthropic's multi-agent engineering article.


## 0.5.0 — 2026-08-31

### Español

- Se añadió el módulo opcional de Iteración para trabajos con intentos reversibles y comparables.
- Se exige línea base, criterio de aceptación previo, evaluación íntegra, veredicto y restauración o incorporación verificable.
- Se fortaleció al Reviewer para comprobar comparabilidad, regresiones, costo de complejidad y restauración.
- Se añadieron registro bilingüe de iteraciones, resumen sencillo en el pulso y control crítico `ITERATION_01`.
- Se corrigió la plantilla de evaluación para incluir `EXECUTION_01` y `EXPERIENCE_01`, ya presentes en el catálogo.
- Se mantuvo la experiencia no técnica: el agente selecciona y configura internamente el loop; la persona recibe sólo resultados y decisiones materiales.
- Se reconoció la influencia conceptual de `karpathy/autoresearch`.

### English

- Added the optional Iteration module for work with reversible comparable attempts.
- Required a baseline, prior acceptance criterion, intact evaluation, verdict, and verifiable restoration or incorporation.
- Strengthened Reviewer duties to verify comparability, regressions, complexity cost and restoration.
- Added bilingual iteration logs, a plain pulse summary and critical control `ITERATION_01`.
- Corrected the evaluation template to include `EXECUTION_01` and `EXPERIENCE_01`, which were already present in the catalog.
- Preserved the non-technical experience: the agent selects and configures the loop internally; the person sees only results and material decisions.
- Acknowledged the conceptual influence of `karpathy/autoresearch`.


## 0.4.1 — 2026-08-30

### Español

- Se añadió modo visible `COMPACT` por defecto y `AUDITABLE` bajo solicitud o necesidad, con presupuesto normal de 250 palabras por checkpoint.
- Se estableció continuación automática entre checkpoints autorizados y pausa sólo ante decisiones, riesgos, contradicciones o autoridad nueva.
- Se exige salida mínima observable por módulo y demostración vigente de capacidades; nombrar, leer o declarar ya no acredita ejecución.
- Se prohíbe redactar entregables basados en actualidad antes de cerrar fuentes y suficiencia de evidencia.
- Se separaron estado operativo, estado durable, estado previo, materiales reutilizables y referencias de estilo.
- Se añadieron los controles `EXECUTION_01` y `EXPERIENCE_01`, casos negativos y reglas de representación móvil.
- Se documentaron tres corridas exploratorias multiplataforma de v0.4.0 como evidencia de diseño, sin presentarlas como certificación o benchmark estadístico.

### English

- Added visible `COMPACT` mode by default and `AUDITABLE` on request or need, with a normal 250-word checkpoint budget.
- Established automatic continuation between authorized checkpoints and pauses only for decisions, risks, contradictions or new authority.
- Required minimum observable output per module and current capability proof; naming, reading or claiming no longer demonstrates execution.
- Prohibited current-fact deliverable drafting before source selection and evidence sufficiency are closed.
- Separated operational state, durable state, prior state, reusable materials and style references.
- Added `EXECUTION_01` and `EXPERIENCE_01`, negative cases and mobile representation rules.
- Recorded three exploratory cross-platform v0.4.0 runs as design evidence without presenting them as certification or a statistical benchmark.

## 0.4.0 — 2026-08-29

### Español

- Se añadió `EMPEZAR_AQUI.md` como única entrada humana recomendada, con una instrucción universal que resuelve `NEW`, `RESUME` o `VERIFY`.
- Se separó explícitamente la experiencia del usuario del interior técnico sin ocultar ni debilitar el contrato auditable.
- Se incorporó un gate de carga: el agente demuestra versión y fuente antes de preguntar y presenta un comprobante de cinco bloques tras las aclaraciones y antes de actuar materialmente.
- Se añadió `LOAD_01`, casos negativos y especificaciones bilingües de aceptación para perfiles no técnicos, sin presentarlas como pruebas humanas ejecutadas.
- Se conserva la limitación honesta: el arnés sigue siendo declarativo y necesita un LLM con acceso real a sus archivos.

### English

- Added `START_HERE.md` as the single recommended human entry, with one universal instruction that resolves `NEW`, `RESUME` or `VERIFY`.
- Explicitly separated the user experience from technical internals without hiding or weakening the auditable contract.
- Added a load gate: the agent demonstrates version and source before asking and presents a five-block receipt after clarification and before material action.
- Added `LOAD_01`, negative cases and bilingual acceptance specifications for non-technical profiles without presenting them as executed human tests.
- Preserved the honest limitation: the harness remains declarative and requires an LLM with real file access.

## 0.3.0 — 2026-08-29

### Español

- Se añadió un inicio guiado declarativo con modos `NEW`, `RESUME` y `VERIFY`.
- Se trasladó al agente la evaluación de capacidades y selección mínima de módulos; el usuario no configura archivos técnicos.
- Se incorporó un resumen de arranque sencillo y auditable sin crear una segunda fuente de estado.
- El perfil de capacidades 1.1 separa disponibilidad, evidencia, autorización, vigencia y alcance.
- Se añadieron los controles críticos `ONBOARDING_01` y `AUTHORITY_01`, casos negativos y esquema de evaluación 1.2.
- Se publicaron tres instrucciones equivalentes y escenarios bilingües para iniciar, continuar y verificar.

### English

- Added a declarative guided start with `NEW`, `RESUME` and `VERIFY` modes.
- Made the agent responsible for capability evaluation and minimum module selection; the user does not configure technical files.
- Added a plain and auditable startup summary without creating a second state source.
- Capability profile 1.1 separates availability, evidence, authorization, freshness and scope.
- Added critical `ONBOARDING_01` and `AUTHORITY_01` controls, negative cases and evaluation schema 1.2.
- Published three equivalent instructions and bilingual scenarios for starting, resuming and verifying.

## 0.2.2 — 2026-08-29

### Español

- Se conectó el módulo de Consejo con la evaluación operacional mediante `COUNCIL_01`.
- Se añadieron metadatos de aplicabilidad, activación, intensidad e independencia al esquema de evaluación 1.1.
- Se definieron criticidad condicional, uso válido de `NOT_APPLICABLE` y una prueba negativa contra mayoría sin evidencia.
- Se aclaró que los controles de Consejo de 0.2.0 eran inicialmente narrativos y ahora son registrables.

### English

- Connected the Council module to operational evaluation through `COUNCIL_01`.
- Added applicability, activation, intensity and independence metadata to evaluation schema 1.1.
- Defined conditional criticality, valid `NOT_APPLICABLE` use and a negative test against unsupported majority.
- Clarified that the 0.2.0 Council checks were initially narrative and are now operationally recordable.

## 0.2.1 — 2026-08-29

### Español

- Se añadió una plantilla bilingüe de pulso operativo para resumir entrega, evidencia, continuidad y siguiente acción.
- Se integró el pulso en estado del proyecto, continuidad y evaluación sin crear un módulo adicional.
- Se prohibió presentar inferencias como telemetría exacta y se definieron fuente, vigencia y degradación explícita.

### English

- Added a bilingual operational-pulse template for delivery, evidence, continuity and the next action.
- Integrated the pulse into project status, continuity and evaluation without adding another module.
- Prohibited presenting inference as exact telemetry and defined source, freshness and explicit degradation.

## 0.2.0 — 2026-08-29

### Español

- Se añadió un módulo opcional de Consejo deliberativo para decisiones difíciles.
- Se incorporó un expediente común, perspectivas independientes, revisión anonimizada y síntesis de presidencia.
- Se agregó la invariante de que consenso, mayoría y repetición no sustituyen evidencia.
- Se añadieron controles de conformidad y degradación honesta sin agentes separados.

### English

- Added an optional deliberative Council module for difficult decisions.
- Added a common brief, independent perspectives, anonymized cross-review and chair synthesis.
- Added the invariant that consensus, majority and repetition do not replace evidence.
- Added conformance checks and honest degradation without separate agents.

## 0.1.1 — 2026-08-29

### Español

- Se restauró la paridad funcional del manifiesto y núcleo inglés.
- Se añadieron criterios `activate_when` y el invariante faltante en inglés.
- Se incorporó un ejemplo bilingüe para escritura, investigación, libros y cursos.
- Se documentaron los IDs normativos de evaluación.
- Se agregó una política y matriz de paridad bilingüe.

### English

- Restored functional parity in the English manifest and core.
- Added missing `activate_when` criteria and invariant in English.
- Added a bilingual example for writing, research, books and courses.
- Documented normative evaluation control IDs.
- Added a bilingual parity policy and matrix.

## 0.1.0 — 2026-08-29

Initial public bilingual release / Publicación bilingüe inicial.
