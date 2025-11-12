import cx_Oracle

# -------------------------------------------------------
# Archivo: conexion.py
# Descripción: Ejemplo de conexión a Oracle Database
#              y ejecución de un procedimiento almacenado
# Proyecto: EcoMarket S.A.
# -------------------------------------------------------

try:
    # Conexión al servicio local de Oracle (ajustar credenciales)
    connection = cx_Oracle.connect("usuario", "contraseña", "localhost/XE")
    cursor = connection.cursor()
    print("✅ Conexión exitosa a la base de datos Oracle")

    # Ejemplo: ejecutar un procedimiento almacenado
    cursor.callproc("pm_productos.crear_producto", [
        'P-100',          # código
        'Producto Prueba',# nombre
        12.50,            # precio
        15,               # stock
        1,                # categoría
        1                 # proveedor
    ])
    connection.commit()

    print("✅ Procedimiento ejecutado correctamente")

except cx_Oracle.Error as error:
    print("❌ Error en la conexión o ejecución:", error)

finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()
        print("🔒 Conexión cerrada")
