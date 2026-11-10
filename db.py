import sqlite3
from pathlib import Path

from flask import current_app, g


def get_db():
    """Abre una conexión por petición y devuelve filas con nombre de columna."""
    if "db" not in g:
        g.db = sqlite3.connect(current_app.config["DATABASE"])
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys = ON")
    return g.db


def close_db(error=None):
    """Cierra la conexión al terminar la petición."""
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    """Crea las tablas si todavía no existen."""
    db = get_db()
    ruta_esquema = Path(__file__).with_name("schema.sql")
    db.executescript(ruta_esquema.read_text(encoding="utf-8"))
    db.commit()


def init_app(app):
    """Registra el cierre automático y prepara la base de datos."""
    app.teardown_appcontext(close_db)
    with app.app_context():
        init_db()
