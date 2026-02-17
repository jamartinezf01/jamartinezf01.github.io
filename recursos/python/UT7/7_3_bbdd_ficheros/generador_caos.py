import sqlite3
import random

def generar_caos():
    """
    Crea una base de datos de la Cripta llena de 'trampas' e inconsistencias
    para que los alumnos practiquen limpieza y manejo de errores.
    """
    db_name = "cripta_corrupta.db"
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    print(f"--- Generando Caos en {db_name} ---")

    # 1. Crear esquema básico sin demasiadas restricciones (para permitir el caos inicial)
    cursor.executescript("""
    DROP TABLE IF EXISTS libros;
    CREATE TABLE libros (
        id INTEGER PRIMARY KEY,
        titulo TEXT,
        autor TEXT,
        paginas INTEGER,
        estado TEXT
    );
    """)

    # 2. Insertar datos con problemas diversos
    datos_caoticos = [
        ("El Quijote", "Cervantes", 1032, "disponible"),
        ("1984", "George Orwell", -50, "disponible"),  # ERROR: Páginas negativas
        (None, "Autor Desconocido", 100, "disponible"), # ERROR: Título nulo
        ("Drácula", "Bram Stoker", 418, "disponible"),
        ("Drácula", "Bram Stoker", 418, "prestado"),   # ERROR: Título duplicado (si fuera UNIQUE)
        ("El Hobbit", "J.R.R. Tolkien", "MUCHAS", "disponible"), # ERROR: Tipo incorrecto (string en vez de int)
        ("Neuromante", "William Gibson", 271, "roto"), # ERROR: Estado no válido
        ("Fundación", "Isaac Asimov", 255, None),      # ERROR: Estado nulo
    ]

    for d in datos_caoticos:
        try:
            cursor.execute("INSERT INTO libros (titulo, autor, paginas, estado) VALUES (?, ?, ?, ?)", d)
        except:
            pass

    conn.commit()
    conn.close()
    print("✅ La Cripta está ahora llena de inconsistencias. ¡Suerte limpiándola!")

if __name__ == "__main__":
    generar_caos()
