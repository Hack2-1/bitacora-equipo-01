# Bitácora de incidentes de ciberseguridad — servicio base

Servicio REST didáctico con Flask y SQLite. Esta primera versión crea la base de datos y expone únicamente el endpoint de salud; las funcionalidades se desarrollan en archivos separados y en ramas independientes.

## Preparación

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python3 main.py
```

Comprobar en otra terminal:

```bash
curl http://127.0.0.1:5000/api/salud
```

Respuesta esperada:

```json
{"estado":"ok","servicio":"bitacora-ciberseguridad"}
```

## Estructura

- `main.py`: archivo principal; crea la aplicación y registra las funcionalidades.
- `db.py`: administra la conexión con SQLite.
- `schema.sql`: define las tablas `activos` e `incidentes`.
- `rutas/`: contiene un archivo por funcionalidad.
- `docs/diseno_api.md`: contrato de endpoints y reglas del sistema.
- `instance/bitacora.sqlite`: archivo generado al ejecutar; no se sube a Git.

## Trabajo en equipo

1. Un integrante crea el repositorio y agrega a los otros dos como colaboradores.
2. El primer commit contiene esta base funcionando, antes de agregar funcionalidades.
3. Cada integrante crea su rama desde `main`:
   - `feature/activos`
   - `feature/incidentes`
   - `feature/resoluciones`
4. Cada funcionalidad se escribe en su propio archivo dentro de `rutas/` y se registra en `main.py`.
5. Cada funcionalidad se prueba y se integra mediante un pull request.
6. Después de cada integración, las ramas restantes actualizan su copia de `main` y resuelven los posibles conflictos conservando las tres funcionalidades.

La solución integrada debe conservar el endpoint `/api/salud` y todos los endpoints descritos en `docs/diseno_api.md`.
