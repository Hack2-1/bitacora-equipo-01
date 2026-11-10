PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS activos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    tipo TEXT NOT NULL,
    ubicacion TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS incidentes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    activo_id INTEGER NOT NULL,
    descripcion TEXT NOT NULL,
    severidad TEXT NOT NULL,
    estado TEXT NOT NULL DEFAULT 'abierto',
    fecha_reporte TEXT NOT NULL,
    accion_tomada TEXT,
    fecha_resolucion TEXT,
    FOREIGN KEY (activo_id) REFERENCES activos (id)
);
