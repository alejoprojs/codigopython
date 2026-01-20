"""
operaciones_db.py
Funciones para trabajar con la base de datos de productos.
"""

import sqlite3

# Nombre de la base de datos
DB_NAME = 'inventario.db'

# ============================================================
# FUNCIONES AUXILIARES
# ============================================================

def conectar():
    """Conecta con la base de datos y retorna la conexión."""
    return sqlite3.connect(DB_NAME)

# ============================================================
# 1. REGISTRAR NUEVO PRODUCTO
# ============================================================

def registrar_producto(nombre, descripcion, cantidad, precio, categoria):
    """
    Registra un nuevo producto en la base de datos.
    
    Retorna: True si se registró correctamente, False si hubo error.
    """
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        
        cursor.execute("""
            INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
            VALUES (?, ?, ?, ?, ?)
        """, (nombre, descripcion, cantidad, precio, categoria))
        
        conexion.commit()
        conexion.close()
        return True
        
    except:
        return False

# ============================================================
# 2. VISUALIZAR PRODUCTOS
# ============================================================

def obtener_todos_productos():
    """
    Obtiene todos los productos de la base de datos.
    
    Retorna: Lista con todos los productos.
    """
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
        
        conexion.close()
        return productos
        
    except:
        return []

# ============================================================
# 3. ACTUALIZAR PRODUCTO POR ID
# ============================================================

def actualizar_producto(id_producto, nombre, descripcion, cantidad, precio, categoria):
    """
    Actualiza los datos de un producto mediante su ID.
    
    Retorna: True si se actualizó correctamente, False si hubo error.
    """
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        
        cursor.execute("""
            UPDATE productos 
            SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?, categoria = ?
            WHERE id = ?
        """, (nombre, descripcion, cantidad, precio, categoria, id_producto))
        
        conexion.commit()
        filas_afectadas = cursor.rowcount
        conexion.close()
        
        return filas_afectadas > 0
        
    except:
        return False

# ============================================================
# 4. ELIMINAR PRODUCTO POR ID
# ============================================================

def eliminar_producto(id_producto):
    """
    Elimina un producto de la base de datos mediante su ID.
    
    Retorna: True si se eliminó correctamente, False si hubo error.
    """
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        
        cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
        
        conexion.commit()
        filas_afectadas = cursor.rowcount
        conexion.close()
        
        return filas_afectadas > 0
        
    except:
        return False

# ============================================================
# 5. BUSCAR PRODUCTO POR ID
# ============================================================

def buscar_producto_por_id(id_producto):
    """
    Busca un producto específico por su ID.
    
    Retorna: Tupla con los datos del producto o None si no existe.
    """
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        
        cursor.execute("SELECT * FROM productos WHERE id = ?", (id_producto,))
        producto = cursor.fetchone()
        
        conexion.close()
        return producto
        
    except:
        return None

# ============================================================
# BÚSQUEDA OPCIONAL POR NOMBRE
# ============================================================

def buscar_producto_por_nombre(nombre):
    """
    Busca productos por nombre (búsqueda parcial).
    
    Retorna: Lista de productos que coinciden con el nombre.
    """
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        
        cursor.execute("SELECT * FROM productos WHERE nombre LIKE ?", (f"%{nombre}%",))
        productos = cursor.fetchall()
        
        conexion.close()
        return productos
        
    except:
        return []

# ============================================================
# BÚSQUEDA OPCIONAL POR CATEGORÍA
# ============================================================

def buscar_producto_por_categoria(categoria):
    """
    Busca productos por categoría.
    
    Retorna: Lista de productos de esa categoría.
    """
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        
        cursor.execute("SELECT * FROM productos WHERE categoria LIKE ?", (f"%{categoria}%",))
        productos = cursor.fetchall()
        
        conexion.close()
        return productos
        
    except:
        return []

# ============================================================
# 6. REPORTE DE BAJO STOCK
# ============================================================

def reporte_bajo_stock(limite):
    """
    Obtiene productos con cantidad igual o menor al límite especificado.
    
    Retorna: Lista de productos con bajo stock.
    """
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        
        cursor.execute("SELECT * FROM productos WHERE cantidad <= ?", (limite,))
        productos = cursor.fetchall()
        
        conexion.close()
        return productos
        
    except:
        return []