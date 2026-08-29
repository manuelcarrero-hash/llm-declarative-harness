# Guía para adaptar un modelo o plataforma

## 1. Inventario de capacidades

Completar `PERFIL_CAPACIDADES.template.yaml` con evidencia. No inferir herramientas por publicidad del proveedor.

## 2. Mapeo mínimo

| Capacidad del arnés | Sustituto aceptable |
| --- | --- |
| Archivos durables | Drive, repositorio, workspace o almacenamiento equivalente |
| Agentes separados | Subagentes, procesos separados o sesiones independientes |
| Revisión independiente | Otro agente sin el veredicto preferido del builder |
| Reglas jerárquicas | Archivo raíz más reglas por subdirectorio con precedencia documentada |
| Contexto medido | Telemetría real de tokens y ventana; de lo contrario señales cualitativas |
| Aprobaciones | Pausa humana verificable antes de la acción |
| Trazas | Log de eventos, herramientas, handoffs y resultados |

## 3. Bootstrap

Instruir al agente para leer `00_LEEME_PRIMERO.md`, manifiesto, núcleo y módulos activados. Copiar plantillas al proyecto sólo cuando no compitan con fuentes existentes. Registrar rutas, no pegar reglas completas en cada prompt.

## 4. Degradación honesta

- Sin subagentes: usar revisión adversarial y declarar que no es independiente.
- Sin escritura: operar en `REPORT` y entregar contenido propuesto.
- Sin telemetría: no usar porcentajes de contexto.
- Sin creación de sesiones: generar handoff y pedir al usuario abrir una sesión limpia.
- Sin herramientas verificables: marcar evidencia como `REPORTED` o `UNKNOWN`.

## 5. Conformidad

Ejecutar la prueba de `06_validacion/PRUEBA_DE_CONFORMIDAD.md`. Una plataforma puede ser compatible parcialmente; debe publicar las excepciones.
