# Diseño de la API — Bitácora de incidentes de ciberseguridad

## Funcionalidad 1: activos

| Método | Ruta | Propósito | Éxito |
|---|---|---|---|
| GET | `/api/activos` | Consultar todos los activos | 200 |
| GET | `/api/activos/<id>` | Consultar un activo | 200 |
| POST | `/api/activos` | Registrar un activo | 201 |
| PUT | `/api/activos/<id>` | Actualizar nombre, tipo o ubicación | 200 |
| DELETE | `/api/activos/<id>` | Eliminar un activo sin incidentes | 200 |

## Funcionalidad 2: incidentes

| Método | Ruta | Propósito | Éxito |
|---|---|---|---|
| GET | `/api/incidentes` | Consultar incidentes | 200 |
| POST | `/api/incidentes` | Reportar un incidente sobre un activo existente | 201 |

## Funcionalidad 3: resoluciones

| Método | Ruta | Propósito | Éxito |
|---|---|---|---|
| PUT | `/api/incidentes/<id>/resolucion` | Cerrar un incidente y registrar la acción tomada | 200 |

## Reglas principales

- Para registrar un activo se requieren `nombre`, `tipo` y `ubicacion`.
- Un incidente debe estar asociado a un activo existente.
- La severidad debe ser `baja`, `media`, `alta` o `critica`.
- Todo incidente nuevo inicia con estado `abierto`.
- Para resolver un incidente se requiere `accion_tomada`.
- No se puede resolver dos veces el mismo incidente.
- No se puede eliminar un activo que tenga incidentes registrados.
