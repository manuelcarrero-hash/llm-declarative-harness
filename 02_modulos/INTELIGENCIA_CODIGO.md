# Módulo: Inteligencia de Código

## Propósito

Reducir cambios aislados o regresiones causadas por comprender el repositorio como una colección de archivos. Antes de un cambio técnico material, el agente construye una visión suficiente y sustentada de la superficie afectada: puntos de entrada, símbolos, llamadas, datos, dependencias, pruebas y límites entre servicios. La profundidad debe ser proporcional al riesgo; este módulo no obliga a indexar todo el repositorio.

La persona describe el cambio en lenguaje natural. El agente selecciona internamente las herramientas y comunica sólo qué partes podrían verse afectadas, qué comprobó, qué permanece incierto y cómo verificará el cambio.

## Activación

Activar cuando:

- se modifica código o arquitectura y el impacto puede extenderse fuera del archivo objetivo;
- el repositorio es desconocido, mediano o grande;
- existen rutas, servicios, datos o repositorios conectados;
- una corrección previa produjo regresiones o la relación entre componentes es incierta;
- el Reviewer necesita comprobar impacto indirecto.

No activar como ceremonia para una edición local, reversible y de bajo riesgo cuya frontera sea evidente. Tampoco usarlo para afirmar comprensión total cuando sólo se inspeccionó una parte.

## Niveles proporcionales

- **BÁSICO:** búsqueda y lectura directa de los archivos relevantes; adecuado para cambios locales con dependencias evidentes.
- **ESTRUCTURAL:** mapa acotado de puntos de entrada, módulos, símbolos, pruebas y dependencias; predeterminado para cambios materiales.
- **PROFUNDO:** grafo de llamadas, flujo de datos, enlaces entre servicios o repositorios y análisis de impacto asistido por herramientas; usar sólo cuando la complejidad y capacidad disponible lo justifiquen.

El nivel describe evidencia requerida, no una herramienta específica.

## Protocolo

### 1. Identidad y reglas

Confirmar repositorio, rama, commit o estado del workspace y reglas aplicables. Separar código confirmado, documentación, resultados de herramientas e inferencias.

### 2. Delimitar la pregunta

Definir el comportamiento que cambiará y la superficie inicial. No explorar todo el repositorio por inercia.

### 3. Reconstruir la superficie afectada

Identificar, según corresponda:

- puntos de entrada y rutas;
- símbolos modificados y sus llamadores o consumidores;
- contratos, tipos, esquemas y persistencia;
- efectos laterales, tareas asíncronas e integraciones;
- pruebas existentes y superficies de usuario relacionadas;
- límites entre paquetes, servicios o repositorios.

Registrar sólo relaciones sustentadas. Una coincidencia textual no demuestra una dependencia ni una herramienta demuestra exhaustividad.

### 4. Clasificar certeza

Clasificar cada relación material con la taxonomía factual del Contrato Operativo. Para dependencias existentes suelen aplicar `CONFIRMED`, `SUPPORTED`, `INFERRED` o `UNKNOWN`; `REPORTED` y `PLANNED` no demuestran una dependencia actual. Una relación `INFERRED` o `UNKNOWN` capaz de invalidar el cambio debe resolverse, acotar el alcance o elevarse antes de ejecutar.

### 5. Analizar impacto

Producir internamente una nota breve con:

- superficie directa;
- dependientes potenciales;
- pruebas y flujos que deben repetirse;
- incertidumbres y exclusiones;
- nivel aplicado, herramientas usadas y vigencia de la evidencia.

Si existe el mapa de trabajo de Equipo, enlazar sólo los resultados afectados sin confundir dependencias del código con dependencias de gestión.

### 6. Implementar y verificar

Modificar únicamente dentro de la frontera autorizada. Después:

- revisar el diff y los símbolos afectados;
- ejecutar pruebas relevantes y, cuando exista superficie real, recorrer los flujos críticos;
- comprobar que no aparecieron dependencias rotas, rutas huérfanas o cambios fuera del alcance;
- actualizar el estado durable sólo con conclusiones útiles y evidencia, no con un volcado del grafo.

## Herramientas estructurales opcionales

Cuando la plataforma disponga de inteligencia de código, búsqueda semántica, LSP, índices o grafos —por ejemplo Codebase Memory MCP— usarlos como aceleradores para arquitectura, llamadas e impacto. Verificar su disponibilidad y vigencia. Aplicar los límites de autoridad y datos sensibles de `../01_nucleo/AUTORIDAD_Y_SEGURIDAD.md`; la disponibilidad de una herramienta no autoriza instalarla, configurarla, mantener servicios persistentes ni transferir código externamente.

Si no están disponibles, aplicar el nivel posible mediante búsqueda, lectura, manifiestos, pruebas y herramientas locales. Declarar la degradación. El arnés sigue funcionando y nunca depende de un proveedor, servidor MCP o producto específico.

## Límites

- Un índice no sustituye PROJECT_STATUS, Git, pruebas ni revisión humana.
- El análisis estático puede omitir reflexión, generación de código, configuración dinámica y efectos de runtime.
- No presentar métricas del proveedor, cobertura declarada o ahorro de tokens como resultados propios.
- No conservar secretos, código completo o salidas voluminosas en el estado del proyecto.

## Salida mínima observable

Para acreditar el módulo deben existir: nivel aplicado, identidad del código inspeccionado, superficie directa, dependientes relevantes, certeza de relaciones materiales, pruebas o flujos seleccionados, incertidumbres y evidencia posterior al cambio. Nombrar la herramienta o afirmar que el repositorio fue analizado no es suficiente.
