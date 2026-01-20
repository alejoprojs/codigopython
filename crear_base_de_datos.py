import sqlite3

def crear_base_de_datos():
    """Crea la base de datos 'inventario.db' y la tabla 'productos'."""
    
    # Conectar con la base de datos (si no existe, se crea automáticamente)
    conexion = sqlite3.connect('inventario.db')
    
    # Crear el cursor para ejecutar comandos SQL
    cursor = conexion.cursor()
    
    # Crear la tabla 'productos' con todas las columnas
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL,
            categoria TEXT
        )
    """)
    
    # Guardar los cambios
    conexion.commit()
    
    # Cerrar la conexión
    conexion.close()
    
    print("Base de datos 'inventario.db' creada exitosamente.")

# Ejecutar la función cuando se corre este archivo directamente
if __name__ == '__main__':
    crear_base_de_datos()