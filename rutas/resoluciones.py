
from datetime import date
from flask import Blueprint, jsonify, request
from db import get_db

bp = Blueprint("resoluciones", __name__)


def incidente_json(fila):
    return {
        "id": fila["id"],
        "activo_id": fila["activo_id"],
        "descripcion": fila["descripcion"],
        "severidad": fila["severidad"],
        "estado": fila["estado"],
        "fecha_reporte": fila["fecha_reporte"],
        "accion_tomada": fila["accion_tomada"],
        "fecha_resolucion": fila["fecha_resolucion"],
    }


@bp.put("/api/incidentes/<int:incidente_id>/resolucion")
def resolver_incidente(incidente_id):
    datos = request.get_json(silent=True) or {}
    accion = str(datos.get("accion_tomada", "")).strip()

    if not accion:
        return jsonify(error="Se requiere accion_tomada"), 400

    db = get_db()
    incidente = db.execute(
        "SELECT * FROM incidentes WHERE id = ?",
        (incidente_id,),
    ).fetchone()

    if incidente is None:
        return jsonify(error="Incidente no encontrado"), 404

    if incidente["estado"] == "cerrado":
        return jsonify(error="Este incidente ya fue resuelto"), 409

    fecha = date.today().isoformat()

    db.execute(
        """
        UPDATE incidentes
        SET estado = 'cerrado', accion_tomada = ?, fecha_resolucion = ?
        WHERE id = ?
        """,
        (accion, fecha, incidente_id),
    )
    db.commit()

    actualizado = db.execute(
        "SELECT * FROM incidentes WHERE id = ?",
        (incidente_id,),
    ).fetchone()

    return jsonify(
        mensaje="Incidente resuelto",
        incidente=incidente_json(actualizado),
    ), 200
