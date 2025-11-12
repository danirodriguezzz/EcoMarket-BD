# EcoMarket S.A.

Sistema de gestión de inventario y ventas desarrollado en **Python + Oracle Database (PL/SQL)**  
para el curso de **Base de Datos II** – Universidad Nacional de Costa Rica.

---

## Estructura general del proyecto

| Carpeta | Descripción |
|----------|-------------|
| [`sql/`](./sql) | Contiene el script principal (`avance2.sql`) y el diccionario de datos. |
| [`python/`](./python) | Contiene el código de conexión entre Python y Oracle. |
| [`docs/`](./docs) | Documentación, README y registro de avances. |

---

## Ejecución

### 1. Crear la base de datos
Ejecutar el archivo [`sql/avance2.sql`](./sql/avance2.sql) en Oracle SQL Developer, DBeaver o Oracle Live SQL.

### 2. Instalar dependencias de Python
```bash
pip install -r python/requirements.txt
