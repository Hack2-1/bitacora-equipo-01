from pathlib import Path

from flask import Flask, jsonify

from db import init_app

from rutas.activos import bp as activos_bp


def create_app():
    """Crea la aplicación e inicializa la base de datos."""
    app = Flask(__name__)
    app.config["DATABASE"] = str(Path(app.instance_path) / "bitacora.sqlite")

    Path(app.instance_path).mkdir(parents=True, exist_ok=True)
    init_app(app)
    app.register_blueprint(activos_bp)

    @app.get("/api/salud")
    def salud():
        """Permite comprobar que el servicio está funcionando."""
        return jsonify(estado="ok", servicio="bitacora-ciberseguridad")

    return app


app = create_app()

if __name__ == "__main__":
    # El modo depuración es solo para desarrollo local.
    app.run(debug=True, port=5000)
