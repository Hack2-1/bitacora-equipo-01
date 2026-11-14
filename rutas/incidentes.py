from flask import Blueprint, jsonify, request
# Importa la conexión a la base de datos (según cómo esté definida en db.py)
from db import get_db 

# Creamos el Blueprint para los incidentes
bp_incidentes = Blueprint('incidentes', __name__, url_prefix='/api/incidentes')

@bp_incidentes.route('/', methods=['GET'])
def listar_incidentes():
    # Aquí irá tu lógica para hacer SELECT a la tabla de incidentes
    return jsonify({"mensaje": "Endpoint de incidentes funcionando"}), 200

@bp_incidentes.route('/', methods=['POST'])
def registrar_incidente():
    # Aquí irá tu lógica para hacer INSERT en la tabla de incidentes
    datos = request.get_json()
    return jsonify({"mensaje": "Incidente registrado", "datos_recibidos": datos}), 201
