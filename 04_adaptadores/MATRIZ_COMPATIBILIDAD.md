# Matriz orientativa de compatibilidad

Esta referencia ayuda a identificar qué capacidades deben comprobarse en cada plataforma. No concede capacidades ni sustituye `PERFIL_CAPACIDADES.template.yaml`. La evidencia actual de la ejecución prevalece siempre sobre esta matriz; después prevalece el perfil completado, luego esta referencia fechada y, al final, cualquier supuesto general.

## Regla de mantenimiento

Usar únicamente `SUPPORTED`, `PARTIAL`, `UNSUPPORTED` o `UNKNOWN`. Cada afirmación distinta de `UNKNOWN` debe indicar plataforma e interfaz concretas, alcance, fuente verificable y fecha. Una marca vencida, ambigua o contradicha vuelve a `UNKNOWN` hasta nueva comprobación. No inferir paridad entre aplicaciones, planes, versiones o configuraciones del mismo proveedor.

## Referencia inicial

Las celdas permanecen deliberadamente `UNKNOWN` hasta registrar evidencia en una ejecución real. El agente consulta esta tabla para planear verificaciones; no pide al usuario completarla.

| Plataforma / interfaz | Archivos durables | Instrucciones jerárquicas | Herramientas | Agentes separados | Revisión independiente | Telemetría de contexto | Rotación de sesión | Pausa de aprobación | Trazas | Estado reanudable | Fuente / fecha / alcance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Plataforma actual | `UNKNOWN` | `UNKNOWN` | `UNKNOWN` | `UNKNOWN` | `UNKNOWN` | `UNKNOWN` | `UNKNOWN` | `UNKNOWN` | `UNKNOWN` | `UNKNOWN` | Verificar durante el inicio guiado |

## Registro de evidencia

Cuando mantener una orientación recurrente aporte valor, añadir una fila con:

- nombre exacto de proveedor, producto e interfaz;
- versión, plan o configuración relevante;
- capacidad y etiqueta;
- prueba observada o documentación primaria;
- fecha de comprobación;
- limitaciones y condiciones.

Una contradicción en la ejecución actual corrige el perfil de esa ejecución y marca la orientación para revisión; nunca se fuerza el trabajo para que coincida con la tabla.
