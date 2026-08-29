# Ejemplo de bootstrap para un proyecto no-código

Solicitud: “Ayúdame a escribir un curso sobre negociación. Quiero investigar, redactar, revisar y dejarlo listo para publicar sin perder decisiones entre conversaciones.”

## Traducción del flujo

| En software | En escritura o investigación |
| --- | --- |
| Implementación | Borrador o desarrollo de contenido |
| Diff | Cambios entre versiones |
| Tests | Comprobación de fuentes, estructura, requisitos y coherencia |
| Reviewer | Editor, revisor académico o crítico |
| Bug | Inconsistencia, vacío argumental o afirmación sin respaldo |
| Deploy | Publicación o entrega |
| User-validated | Aprobación del autor, cliente o responsable académico |

## Ejecución

1. El agente lee el arnés y declara capacidades reales.
2. Identifica el proyecto, audiencia, entregables, fuentes existentes y decisiones ya tomadas.
3. Crea un contrato con alcance, índice esperado, criterios de calidad, fuentes permitidas, límites y condición observable de terminado.
4. Mantiene `PROJECT_STATUS.md` con capítulos o módulos validados, borradores pendientes, decisiones editoriales, riesgos y siguiente acción.
5. El autor o investigador produce un borrador acotado y registra fuentes y supuestos.
6. Un revisor inspecciona el borrador real contra audiencia, estructura, exactitud, evidencia y criterios editoriales; devuelve `APPROVED` o `CHANGES_REQUIRED`.
7. Los comentarios se convierten en cambios trazables. Un comentario resuelto no equivale a contenido publicado.
8. Si cambia la sesión, se crea un handoff con el último borrador autoritativo, decisiones, fuentes, comentarios abiertos y primera acción del sucesor.
9. Sólo se declara `ACHIEVED` cuando todos los entregables están completos, revisados y aprobados por la persona autorizada. Publicar requiere autoridad separada.

Si no existe un revisor independiente, registrar la revisión como adversarial no independiente. Si no existe acceso verificable a las fuentes, etiquetar las afirmaciones como `REPORTED` o `UNKNOWN`, no como comprobadas.
