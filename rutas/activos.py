from flask import Blueprint, jsonify, request
from db import get_db

bp = Blueprint("activos", __name__)

def activo_json(fila):
    """Convierte una fila de SQLite en un recurso JSON."""
    return {
        "id": fila["id"],
        "nombre": fila["nombre"],
        "tipo": fila["tipo"],
        "ubicacion": fila["ubicacion"],
    }

def buscar_activo(db, activo_id):
    return db.execute(
        "SELECT * FROM activos WHERE id = ?", (activo_id,)
    ).fetchone()

@bp.get("/api/activos")
def listar_activos():
    filas = get_db().execute("SELECT * FROM activos ORDER BY id").fetchall()
    return jsonify([activo_json(fila) for fila in filas])

@bp.get("/api/activos/<int:activo_id>")
def obtener_activo(activo_id):
    activo = buscar_activo(get_db(), activo_id)
    if activo is None:
        return jsonify(error="Activo no encontrado"), 404
    return jsonify(activo_json(activo))

@bp.post("/api/activos")
def crear_activo():
    datos = request.get_json(silent=True) or {}
    nombre = str(datos.get("nombre", "")).strip()
    tipo = str(datos.get("tipo", "")).strip()
    ubicacion = str(datos.get("ubicacion", "")).strip()

    if not nombre or not tipo or not ubicacion:
        return jsonify(error="Se requieren nombre, tipo y ubicacion"), 400

    db = get_db()
    cursor = db.execute(
        "INSERT INTO activos (nombre, tipo, ubicacion) VALUES (?, ?, ?)",
        (nombre, tipo, ubicacion),
    )
    db.commit()
    activo = buscar_activo(db, cursor.lastrowid)
    return jsonify(activo_json(activo)), 201

@bp.put("/api/activos/<int:activo_id>")
def actualizar_activo(activo_id):
    db = get_db()
    activo = buscar_activo(db, activo_id)
    if activo is None:
        return jsonify(error="Activo no encontrado"), 404

    datos = request.get_json(silent=True) or {}
    nombre = str(datos.get("nombre", activo["nombre"])).strip()
    tipo = str(datos.get("tipo", activo["tipo"])).strip()
    ubicacion = str(datos.get("ubicacion", activo["ubicacion"])).strip()

    if not nombre or not tipo or not ubicacion:
        return jsonify(error="Los campos no pueden estar vacios"), 400

    db.execute(
        "UPDATE activos SET nombre = ?, tipo = ?, ubicacion = ? WHERE id = ?",
        (nombre, tipo, ubicacion, activo_id),
    )
    db.commit()
    return jsonify(activo_json(buscar_activo(db, activo_id)))

@bp.delete("/api/activos/<int:activo_id>")
def eliminar_activo(activo_id):
    db = get_db()
    activo = buscar_activo(db, activo_id)
    if activo is None:
        return jsonify(error="Activo no encontrado"), 404

    incidente = db.execute(
        "SELECT id FROM incidentes WHERE activo_id = ? LIMIT 1", (activo_id,)
    ).fetchone()

    if incidente is not None:
        return jsonify(error="El activo tiene incidentes y no puede eliminarse"), 409

    db.execute("DELETE FROM activos WHERE id=?", (activo_id,))
    db.commit()
    return jsonify(mensaje="Activo eliminado")