# EcoMarket S.A. – Avance 2

Proyecto correspondiente al **Avance 2** del sistema de gestión de inventario y ventas de *EcoMarket S.A.*  
Desarrollado con **Python** (lenguaje de conexión) y **Oracle Database (PL/SQL)**.

---

## Contenido del repositorio

| Carpeta | Contenido |
|----------|------------|
| `sql/` | Script principal (`avance2.sql`) con tablas, vistas, procedimientos, funciones, triggers y paquetes. |
| `python/` | Código de conexión en Python para ejecutar procedimientos almacenados. |
| `docs/` | Documentación general, README y registro de cambios. |

---

## Tecnologías utilizadas
- Lenguaje de conexión: **Python**
- Base de datos: **Oracle Database 21c (PL/SQL)**
- Librería: `cx_Oracle`

---

## Instrucciones de ejecución

1. **Ejecutar la base de datos**
   - Abrir Oracle SQL Developer, DBeaver o LiveSQL.
   - Ejecutar `sql/avance2.sql` para crear las tablas y objetos PL/SQL.

2. **Conectar desde Python**
   - Instalar dependencias:
     ```bash
     pip install -r python/requirements.txt
     ```
   - Ejecutar:
     ```bash
     python python/conexion.py
     ```

3. **Verificar resultados**
   - Revisar que se haya insertado el producto de prueba en la tabla `PRODUCTO`.

---

## Integrante
- Daniel Rodríguez  


---

## 📅 Resumen del avance
- Implementado el 50 % de la programación del sistema.  
- Creación de tablas y estructuras principales.  
- Procedimientos, funciones, vistas y paquetes básicos operativos.  
- Conexión Python–Oracle funcional.  
- Diccionario de datos generado en SQL Developer.

---

## 📂 Estructura de carpetas

