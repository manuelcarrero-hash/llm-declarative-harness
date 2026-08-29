# Módulo: continuidad de contexto

Proteger decisiones, evidencia, estado parcial y siguiente acción cuando el trabajo cruce agentes, sesiones, compactación o fases.

## Umbrales

Usar porcentajes sólo si existe telemetría real y se conoce la capacidad total. Política por defecto: checkpoint preventivo al 30% medido y rotación al 40% medido. Sin telemetría, usar señales cualitativas y declarar el porcentaje como desconocido.

## Rotación

Llegar a un límite atómico seguro; escribir handoff; verificarlo contra fuentes; sincronizar estado autorizado; iniciar sucesor con contexto mínimo; exigir handshake antes de editar; relevar al anterior sólo después del handshake.

No fingir que se detuvo o creó una sesión si la plataforma no lo permite.
