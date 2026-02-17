-- Esquema inicial para La Cripta de Datos
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS autores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS categorias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS libros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL UNIQUE,
    autor_id INTEGER NOT NULL,
    categoria_id INTEGER,
    paginas INTEGER CHECK(paginas > 0),
    estado TEXT DEFAULT 'disponible',
    FOREIGN KEY (autor_id) REFERENCES autores(id) ON DELETE CASCADE,
    FOREIGN KEY (categoria_id) REFERENCES categorias(id)
);

-- Datos iniciales de ejemplo
INSERT OR IGNORE INTO autores (nombre) VALUES ('Miguel de Cervantes'), ('George Orwell'), ('Isaac Asimov');
INSERT OR IGNORE INTO categorias (nombre) VALUES ('Clásicos'), ('Distopía'), ('Ciencia Ficción');

INSERT OR IGNORE INTO libros (titulo, autor_id, categoria_id, paginas) VALUES 
('Don Quijote de la Mancha', 1, 1, 1032),
('1984', 2, 2, 328),
('Fundación', 3, 3, 255);
