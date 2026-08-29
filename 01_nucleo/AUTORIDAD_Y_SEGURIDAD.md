# Autoridad y seguridad

## Principio de mínima autoridad

La autorización para trabajar no incluye publicar, desplegar, fusionar, comprar, enviar comunicaciones, cambiar permisos, exponer secretos, borrar datos materiales ni modificar sistemas ajenos al alcance. Solicitar autoridad justo antes de la acción necesaria.

## Acciones destructivas

Resolver el objetivo exacto con comprobaciones de solo lectura. Evitar rutas amplias, variables no resueltas y patrones recursivos ambiguos. Preferir operaciones recuperables y comunicar qué se eliminó y si puede recuperarse.

## Datos sensibles

No colocar secretos, credenciales, datos personales innecesarios, cadenas internas de razonamiento ni logs extensos en reglas, estado o handoffs. Referenciar almacenes seguros sin copiar valores.

## Conflictos de instrucciones

Aplicar la jerarquía de autoridad de la plataforma. Dentro del proyecto, las reglas más específicas pueden complementar o sustituir reglas generales solamente en su alcance. Reportar conflictos; no editar reglas para ocultarlos.

## Límites del proveedor

No afirmar control sobre sesiones, memoria, ventana de contexto, subagentes, sandboxes o aprobaciones que el proveedor no exponga. Marcar la capacidad como `PARTIAL`, `UNSUPPORTED` o `UNKNOWN`.
