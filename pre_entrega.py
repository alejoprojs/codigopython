"""
pre_entrega.py
Programa principal con menú de opciones para gestionar productos.
"""

from crear_base_de_datos import crear_base_de_datos
from operaciones_db import *

# Crear la base de datos al iniciar
crear_base_de_datos()

# Pedir nombre de usuario
usuario = input("Ingrese su nombre de usuario: ").strip()

if usuario == "":
    print("Error: El nombre de usuario no puede estar vacío.")
    exit()

print("")
print(f"== Bienvenido/a {usuario} al Sistema de Gestión de Inventario ==")

# Menú principal
while True:
    print("")
    print("=" * 60)
    print("MENÚ PRINCIPAL")
    print("=" * 60)
    print("1. Registrar nuevo producto")
    print("2. Visualizar todos los productos")
    print("3. Actualizar producto (por ID)")
    print("4. Eliminar producto (por ID)")
    print("5. Buscar producto")
    print("6. Reporte de bajo stock")
    print("7. Salir")
    print("=" * 60)
    
    # Pedir opción
    try:
        opcion = int(input("Ingresa el número de opción: "))
    except:
        print("Error: Debes ingresar un número del 1 al 7.")
        continue

    # OPCIÓN 1: REGISTRAR PRODUCTO

    if opcion == 1:
        print("")
        print("--- REGISTRAR NUEVO PRODUCTO ---")
        print("")
        
        # Pedir datos del producto
        nombre = input("Nombre del producto: ").strip()
        
        if nombre == "":
            print("Error: El nombre no puede estar vacío.")
            continue
        
        descripcion = input("Descripción del producto: ").strip()
        
        cantidad_valida = False
        while not cantidad_valida:
            try:
                cantidad = int(input("Cantidad en stock: "))
                if cantidad < 0:
                    print("Error: La cantidad no puede ser negativa.")
                else:
                    cantidad_valida = True
            except:
                print("Error: Debes ingresar un número válido.")
        
        precio_valido = False
        while not precio_valido:
            try:
                precio = float(input("Precio: $"))
                if precio <= 0:
                    print("Error: El precio debe ser mayor que 0.")
                else:
                    precio_valido = True
            except:
                print("Error: Debes ingresar un número válido.")
        
        categoria = input("Categoría: ").strip()
        
        # Registrar en la base de datos
        if registrar_producto(nombre, descripcion, cantidad, precio, categoria):
            print("")
            print(f"Producto '{nombre}' registrado exitosamente.")
        else:
            print("")
            print("Error al registrar el producto.")
    
    # OPCIÓN 2: VISUALIZAR PRODUCTOS

    elif opcion == 2:
        print("")
        print("--- LISTA DE PRODUCTOS ---")
        print("")
        
        productos = obtener_todos_productos()
        
        if len(productos) == 0:
            print("No hay productos registrados.")
        else:
            # Mostrar encabezado
            print(f"{'ID':<5} {'Nombre':<20} {'Descripción':<25} {'Cantidad':<10} {'Precio':<12} {'Categoría':<15}")
            print("-" * 95)
            
            # Mostrar cada producto
            for producto in productos:
                id_p = producto[0]
                nombre = producto[1][:19] if len(producto[1]) > 19 else producto[1]
                desc = producto[2][:24] if producto[2] and len(producto[2]) > 24 else (producto[2] if producto[2] else "N/A")
                cant = producto[3]
                precio = producto[4]
                cat = producto[5] if producto[5] else "N/A"
                
                print(f"{id_p:<5} {nombre:<20} {desc:<25} {cant:<10} ${precio:<11.2f} {cat:<15}")
            
            print("-" * 95)
            print(f"Total de productos: {len(productos)}")
    
    # OPCIÓN 3: ACTUALIZAR PRODUCTO

    elif opcion == 3:
        print("")
        print("--- ACTUALIZAR PRODUCTO ---")
        print("")
        
        # Pedir ID del producto
        try:
            id_producto = int(input("Ingresa el ID del producto a actualizar: "))
        except:
            print("Error: Debes ingresar un ID válido.")
            continue
        
        # Buscar si existe
        producto_actual = buscar_producto_por_id(id_producto)
        
        if producto_actual is None:
            print(f"No existe un producto con ID {id_producto}.")
            continue
        
        # Mostrar datos actuales
        print("")
        print("Datos actuales del producto:")
        print(f"Nombre: {producto_actual[1]}")
        print(f"Descripción: {producto_actual[2] if producto_actual[2] else 'N/A'}")
        print(f"Cantidad: {producto_actual[3]}")
        print(f"Precio: ${producto_actual[4]:.2f}")
        print(f"Categoría: {producto_actual[5] if producto_actual[5] else 'N/A'}")
        print("")
        
        # Pedir nuevos datos
        print("Ingresa los nuevos datos (Enter para mantener el valor actual):")
        
        nombre = input(f"Nombre [{producto_actual[1]}]: ").strip()
        if nombre == "":
            nombre = producto_actual[1]
        
        descripcion = input(f"Descripción [{producto_actual[2] if producto_actual[2] else ''}]: ").strip()
        if descripcion == "":
            descripcion = producto_actual[2]
        
        cantidad_input = input(f"Cantidad [{producto_actual[3]}]: ").strip()
        if cantidad_input == "":
            cantidad = producto_actual[3]
        else:
            try:
                cantidad = int(cantidad_input)
            except:
                print("Cantidad inválida, se mantendrá el valor actual.")
                cantidad = producto_actual[3]
        
        precio_input = input(f"Precio [{producto_actual[4]:.2f}]: ").strip()
        if precio_input == "":
            precio = producto_actual[4]
        else:
            try:
                precio = float(precio_input)
            except:
                print("Precio inválido, se mantendrá el valor actual.")
                precio = producto_actual[4]
        
        categoria = input(f"Categoría [{producto_actual[5] if producto_actual[5] else ''}]: ").strip()
        if categoria == "":
            categoria = producto_actual[5]
        
        # Actualizar en la base de datos
        if actualizar_producto(id_producto, nombre, descripcion, cantidad, precio, categoria):
            print("")
            print("Producto actualizado exitosamente.")
        else:
            print("")
            print("Error al actualizar el producto.")
    
    # OPCIÓN 4: ELIMINAR PRODUCTO

    elif opcion == 4:
        print("")
        print("--- ELIMINAR PRODUCTO ---")
        print("")
        
        # Pedir ID del producto
        try:
            id_producto = int(input("Ingresa el ID del producto a eliminar: "))
        except:
            print("Error: Debes ingresar un ID válido.")
            continue
        
        # Buscar si existe
        producto = buscar_producto_por_id(id_producto)
        
        if producto is None:
            print(f"No existe un producto con ID {id_producto}.")
            continue
        
        # Mostrar datos y confirmar
        print("")
        print("Producto a eliminar:")
        print(f"ID: {producto[0]}")
        print(f"Nombre: {producto[1]}")
        print(f"Categoría: {producto[5] if producto[5] else 'N/A'}")
        print("")
        
        confirmacion = input("¿Estás seguro de eliminar este producto? (si/no): ").lower()
        
        if confirmacion == "si":
            if eliminar_producto(id_producto):
                print("")
                print("Producto eliminado exitosamente.")
            else:
                print("")
                print("Error al eliminar el producto.")
        else:
            print("")
            print("Eliminación cancelada.")
    
    # OPCIÓN 5: BUSCAR PRODUCTO

    elif opcion == 5:
        print("")
        print("--- BUSCAR PRODUCTO ---")
        print("")
        print("Buscar por:")
        print("1. ID")
        print("2. Nombre")
        print("3. Categoría")
        print("")
        
        try:
            tipo_busqueda = int(input("Selecciona opción: "))
        except:
            print("Opción inválida.")
            continue
        
        if tipo_busqueda == 1:
            # Buscar por ID
            try:
                id_producto = int(input("Ingresa el ID: "))
            except:
                print("Error: Debes ingresar un ID válido.")
                continue
            
            producto = buscar_producto_por_id(id_producto)
            
            if producto:
                print("")
                print("Producto encontrado:")
                print(f"ID: {producto[0]}")
                print(f"Nombre: {producto[1]}")
                print(f"Descripción: {producto[2] if producto[2] else 'N/A'}")
                print(f"Cantidad: {producto[3]}")
                print(f"Precio: ${producto[4]:.2f}")
                print(f"Categoría: {producto[5] if producto[5] else 'N/A'}")
            else:
                print("")
                print("No se encontró el producto.")
        
        elif tipo_busqueda == 2:
            # Buscar por nombre
            nombre = input("Ingresa el nombre a buscar: ").strip()
            productos = buscar_producto_por_nombre(nombre)
            
            if len(productos) == 0:
                print("")
                print("No se encontraron productos con ese nombre.")
            else:
                print("")
                print(f"Se encontraron {len(productos)} producto(s):")
                print("")
                for producto in productos:
                    print(f"ID: {producto[0]} - {producto[1]} - ${producto[4]:.2f}")
        
        elif tipo_busqueda == 3:
            # Buscar por categoría
            categoria = input("Ingresa la categoría a buscar: ").strip()
            productos = buscar_producto_por_categoria(categoria)
            
            if len(productos) == 0:
                print("")
                print("No se encontraron productos en esa categoría.")
            else:
                print("")
                print(f"Se encontraron {len(productos)} producto(s):")
                print("")
                for producto in productos:
                    print(f"ID: {producto[0]} - {producto[1]} - Categoría: {producto[5]}")
        
        else:
            print("Opción inválida.")
    
    # OPCIÓN 6: REPORTE DE BAJO STOCK
    
    elif opcion == 6:
        print("")
        print("--- REPORTE DE BAJO STOCK ---")
        print("")
        
        # Pedir límite
        try:
            limite = int(input("Ingresa el límite de stock: "))
        except:
            print("Error: Debes ingresar un número válido.")
            continue
        
        productos = reporte_bajo_stock(limite)
        
        if len(productos) == 0:
            print("")
            print(f"No hay productos con stock igual o menor a {limite}.")
        else:
            print("")
            print(f"Productos con stock igual o menor a {limite}:")
            print("")
            print(f"{'ID':<5} {'Nombre':<25} {'Cantidad':<10} {'Categoría':<15}")
            print("-" * 60)
            
            for producto in productos:
                id_p = producto[0]
                nombre = producto[1][:24] if len(producto[1]) > 24 else producto[1]
                cant = producto[3]
                cat = producto[5] if producto[5] else "N/A"
                
                print(f"{id_p:<5} {nombre:<25} {cant:<10} {cat:<15}")
            
            print("-" * 60)
            print(f"Total: {len(productos)} producto(s) con bajo stock")
    
    # OPCIÓN 7: SALIR
   
    elif opcion == 7:
        print("")
        print("Saliendo del sistema...")
        print(f"¡Hasta pronto, {usuario}!")
        print("")
        break
    
    else:
        print("Opción no válida. Por favor, selecciona un número del 1 al 7.")