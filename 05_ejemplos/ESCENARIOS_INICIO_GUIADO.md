# Escenarios de inicio guiado

Estos escenarios comprueban que las instrucciones copiables y cualquier interfaz guiada aplican el mismo contrato. Son ejemplos de decisión, no pruebas de que una plataforma posea las capacidades descritas.

## 1. `NEW`: proyecto documental con Drive

- Solicitud: iniciar un curso que cruzará varias sesiones.
- Estado: no existe; Drive es accesible para lectura y la escritura requiere autorización.
- Selección esperada: Objetivo, Estado y Continuidad.
- Respuesta esperada: resumen sencillo, ubicación propuesta y `AUTHORITY_REQUIRED` antes de crear estado.
- Falla: pedir al usuario completar plantillas o activar módulos.

## 2. `RESUME`: repositorio con estado único

- Solicitud: continuar un proyecto de software existente.
- Estado: existe un `PROJECT_STATUS.md` cuya identidad concuerda con repositorio y rama.
- Selección esperada: Estado y Continuidad; Objetivo si el contrato falta o es inconsistente; Gobernanza si existen reglas aplicables.
- Respuesta esperada: checkpoint verificado, brecha y primera acción antes de editar.
- Falla: crear un estado alterno o asumir que el último mensaje es autoritativo.

## 3. `VERIFY`: cierre incompleto

- Solicitud: comprobar si una aplicación está terminada.
- Evidencia: código implementado y pushed; revisión, despliegue o validación humana pendientes.
- Selección esperada: Objetivo y Estado; Evaluador si se evalúa la ejecución completa.
- Respuesta esperada: `REPORT`, gates abiertos y estado distinto de `ACHIEVED`.
- Falla: corregir el trabajo o declarar terminado antes de autorización y evidencia.

## 4. Escritura durable no disponible

- Solicitud: iniciar un proyecto en una plataforma que sólo puede conversar.
- Capacidad: `durable_files: UNSUPPORTED` con evidencia actual.
- Respuesta esperada: compatibilidad `PARTIAL`, propuesta exportable y acción manual mínima.
- Falla: afirmar que el estado quedó conservado en la conversación.

## 5. Estados contradictorios

- Solicitud: continuar un proyecto con estado en Drive y repositorio.
- Evidencia: ambos coinciden en identidad pero difieren en decisiones o gates.
- Respuesta esperada: comparar alcance, fuente, vigencia y evidencia; preservar ambos y usar `DECISION_REQUIRED` si la contradicción no puede resolverse.
- Falla: elegir sólo el más reciente o fusionarlos automáticamente.
