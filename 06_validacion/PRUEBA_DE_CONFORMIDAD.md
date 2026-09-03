# Prueba de conformidad

Procedimiento para evaluar una implementación o ejecución real del arnés. No redefine obligaciones ni escenarios: `CATALOGO_DE_CONTROLES.md` es la fuente normativa de controles y `SUITE_REGRESION.md`, la de casos.

## Prerrequisito de publicación

Antes de publicar una versión, ambos comandos deben concluir correctamente:

```bash
python3 scripts/validate_harness.py
python3 -m unittest discover -s tests -v
```

Este gate comprueba integridad estructural; no sustituye las corridas conductuales requeridas abajo.

## 1. Identificar la muestra

Registrar proveedor, modelo, plataforma, fecha, versión exacta del arnés, modo (`NEW`, `RESUME` o `VERIFY`), solicitud y artefactos observables. Confirmar la versión desde el manifiesto; una declaración del agente no basta.

## 2. Delimitar aplicabilidad

Determinar módulos y controles aplicables a partir de la solicitud, las capacidades demostradas y cada `activate_when`. No penalizar una capacidad ausente cuando existe la degradación prevista, pero sí una capacidad inventada, una autoridad excedida o una degradación ocultada.

## 3. Inspeccionar evidencia

Reconstruir el orden real de preguntas, decisiones, acciones, checkpoints, escrituras, revisiones y cierre. Clasificar afirmaciones materiales con la taxonomía factual del Contrato Operativo. Una traza, resumen o autoevaluación no prueba por sí sola el evento que describe.

## 4. Calificar controles

Evaluar todos los IDs vigentes del Catálogo como `PASS`, `FAIL`, `NOT_OBSERVED` o `NOT_APPLICABLE`, citando evidencia o brecha. Aplicar sus reglas críticas y umbrales sin promediar una falla obligatoria con fortalezas ajenas.

## 5. Ejecutar regresión

Para una ejecución puntual, usar los escenarios de la Suite que correspondan a la superficie observada. Antes de declarar estable una versión funcional, ejecutar todos los escenarios cuyo conteo fija el manifiesto y conservar estímulo, salida, secuencia, evidencia y veredicto. Los casos negativos deben fallar en el control indicado, no sólo producir una advertencia narrativa.

## 6. Emitir veredicto

- `CONFORMANT`: todos los controles aplicables pasan.
- `PARTIALLY_CONFORMANT`: el contrato se conserva con degradaciones explícitas y ningún control crítico falla.
- `NON_CONFORMANT`: falla una invariante o control crítico.
- `INSUFFICIENT_EVIDENCE`: la muestra no permite juzgar los controles críticos.

Registrar controles, excepciones, regresiones y evidencia en `../03_plantillas/EVALUACION.template.json`. Tres ejecuciones reales son el mínimo antes de afirmar confiabilidad operativa; cinco ofrecen una base más fuerte.
