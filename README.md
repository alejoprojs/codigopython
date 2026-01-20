# Sistema de Gestión de Inventario (Python + SQLite)

## Descripción del proyecto

Este proyecto es un sistema de gestión de inventario desarrollado en
Python que permite registrar, consultar, actualizar y eliminar productos
utilizando una base de datos SQLite.

El programa funciona mediante un menú interactivo en consola,
permitiendo al usuario administrar un inventario de manera sencilla. La
base de datos se crea automáticamente al ejecutar el programa por
primera vez.

## Estructura del proyecto

    📁 Proyecto-Inventario
    │
    ├── crear_base_de_datos.py     # Crea la base de datos y la tabla 'productos'
    ├── operaciones_db.py          # Contiene las funciones CRUD y consultas
    ├── pre_entrega.py             # Programa principal con el menú del sistema
    └── inventario.db              # Se genera automáticamente

## Base de datos

El proyecto utiliza SQLite, sin necesidad de instalar servidores
externos.

### Tabla: productos

  Campo         Tipo      Descripción
  ------------- --------- ------------------------
  id            INTEGER   ID autoincremental
  nombre        TEXT      Nombre del producto
  descripcion   TEXT      Descripción opcional
  cantidad      INTEGER   Cantidad en stock
  precio        REAL      Precio unitario
  categoria     TEXT      Categoría del producto

## Descripción de cada archivo

### 1. crear_base_de_datos.py

-   Crea automáticamente el archivo inventario.db
-   Genera la tabla productos si no existe
-   Se ejecuta al iniciar el programa principal

### 2. operaciones_db.py

Contiene todas las operaciones con la base de datos (CRUD): - Registrar
producto - Obtener todos los productos - Actualizar por ID - Eliminar
por ID - Buscar por ID, nombre o categoría - Reporte de bajo stock

### 3. pre_entrega.py

Es el programa principal. Incluye: - Menú interactivo - Validación de
datos - Impresión de listados formateados - Llamadas a funciones del
archivo operaciones_db.py - Creación automática de la base de datos al
iniciar

## Cómo ejecutar el proyecto

### Requisitos

-   Python 3.8+
-   No requiere instalación adicional

### Ejecutar el programa

    python pre_entrega.py

## Funciones del sistema

1.  Registrar nuevo producto\
2.  Visualizar productos\
3.  Actualizar producto por ID\
4.  Eliminar producto\
5.  Buscar producto\
6.  Reporte de bajo stock\
7.  Salir

## Posibles mejoras futuras

-   Exportar reportes
-   Agregar interfaz gráfica
-   Crear login con contraseña
-   Stock mínimo automático
-   Sistema de logs
