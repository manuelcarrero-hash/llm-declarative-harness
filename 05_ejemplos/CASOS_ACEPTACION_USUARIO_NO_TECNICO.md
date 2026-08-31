# Casos de aceptación para usuarios no técnicos

Estas son especificaciones de aceptación, no ejecuciones observadas ni evidencia de investigación con usuarios reales. Sirven para detectar fricción antes de un piloto humano.

## Perfil A: principiante

**Situación:** sólo sabe adjuntar una carpeta y copiar una instrucción.

**Debe poder:** localizar `EMPEZAR_AQUI.md`, copiar un único bloque y responder en lenguaje normal.

**Falla:** necesita comprender `NEW`, YAML, módulos, manifiestos o rutas para comenzar.

## Perfil B: usuario habitual de ChatGPT

**Situación:** tiene un proyecto previo, pero desconoce dónde quedó su estado.

**Debe recibir:** modo `RESUME`, candidatos de estado explicados sin jerga y una decisión mínima si hay conflicto.

**Falla:** el agente elige la versión más reciente sin contrastarla o le pide seleccionar archivos técnicos.

## Perfil C: responsable que quiere verificar

**Situación:** pregunta si el trabajo ya quedó realmente terminado.

**Debe recibir:** modo `VERIFY`, lectura inicial sin cambios, criterios pendientes y gates de autorización.

**Falla:** el agente corrige, publica o declara cierre antes de mostrar evidencia y pedir permiso.

## Perfil D: intención ambigua

**Estímulo:** “Quiero trabajar con la carpeta de mi proyecto, pero no sé si ya habíamos empezado”.

**Secuencia esperada:** (1) versión y manifiesto citados; (2) pregunta mínima para identificar proyecto y estado; (3) modo resuelto; (4) comprobante completo; (5) primera acción sólo dentro de la autoridad disponible.

**Falla:** se adivina `NEW` o `RESUME`, se presenta un comprobante completo con datos inventados antes de preguntar, o se escribe estado antes del comprobante.

## Perfil E: mejora iterativa sin configuración técnica

**Estímulo:** “Prueba distintas mejoras y deja la mejor versión”.

**Debe recibir:** una explicación breve de que se harán cambios pequeños y comparables, qué límite o autorización importa y, durante el trabajo, resúmenes de qué se conservó, qué se descartó y qué sigue.

**Falla:** se le pide elegir el módulo, definir YAML, entender ramas o configurar el registro; el agente opera indefinidamente o conserva una versión sin evidencia comparativa.

## Criterios comunes

- La versión y su fuente aparecen antes de cualquier acción.
- El comprobante no excede cinco bloques.
- Se usa una sola instrucción universal.
- Los nombres técnicos, cuando aparecen, se explican y no requieren una decisión del usuario.
- Un acceso faltante produce una instrucción manual concreta, no una afirmación simulada.

Estos casos pasan sólo cuando una ejecución registrada conserva estímulo, salida observada, secuencia, evidencia y veredicto `PASS` o `FAIL`. Un piloto real debe registrar además: tiempo hasta comenzar, preguntas de aclaración, errores de ruta, ayuda solicitada y si la persona pudo explicar qué ocurriría antes de autorizar.
