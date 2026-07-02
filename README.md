# Sistema de Gestión SENA - API Unificada 🚀

### Información del Aprendiz
* **Nombre:** Daniel Santiago Rodriguez Cardozo
* **Ficha:** 3407184
* **Instructor:** Jhony Guerrero

---

## 🛠️ Descripción del Proyecto
Este proyecto consiste en una API REST modular desarrollada con **FastAPI** para la gestión unificada de **Clientes, Facturas y Transacciones**. Aplica una arquitectura limpia separando la lógica de negocio en enrutadores modulares con persistencia de datos mediante SQLite y SQLModel.

### 📐 Arquitectura y Buenas Prácticas Aplicadas
1. **Modularización con APIRouter:** Los endpoints no se saturan en el archivo principal (`main.py`), sino que están segmentados por módulos dentro de la carpeta `routers/`.
2. **Principio de Herencia de Clases (Pydantic):** Se diseñaron modelos base para optimizar la reutilización de código. Modelos como `FacturaCrear` y `Factura` heredan atributos automáticamente, asegurando consistencia.
3. **Validación de Datos Automática:** Tipado estricto mediante Pydantic que valida en tiempo real los tipos de datos entrantes (ej. montos flotantes, identificadores enteros).
4. **Desacoplamiento de Datos:** El archivo `conexion_bd.py` actúa como la capa de persistencia, aislando la configuración de base de datos de las rutas de la API.
5. **Lifespan moderno:** Se usa el patrón `lifespan` de FastAPI (reemplaza el deprecado `on_event`).

---

## 📁 Estructura del Proyecto

```
REPOSITORIO_DANIEL_RODRIGUEZ/
├── requirements.txt
├── README.md
├── main.py                  # Punto de entrada y montaje de Routers
├── app/
│   ├── __init__.py
│   ├── conexion_bd.py       # Motor SQLite y sesión (SQLModel)
│   └── modelos/             # Definición de tablas
│       ├── Clientes.py
│       ├── Facturas.py
│       └── Transacciones.py
└── routers/                 # Lógica de endpoints (CRUD completo)
    ├── clientes.py
    ├── facturas.py
    └── transacciones.py
```

---

## 🚀 Cómo ejecutar

```bash
# 1. Crear y activar entorno virtual
python -m venv mi_env
source mi_env/Scripts/activate   # Windows Git Bash
# source mi_env/bin/activate     # Mac / Linux

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Correr la API
uvicorn main:app --reload
```

Abrir en el navegador: http://127.0.0.1:8000/docs

---

## 📌 Implementación - SENA Junio 2025

1. Configuración de `conexion_bd.py` con `create_engine` y `Session` para persistencia SQLite.
2. Modelos relacionales con `SQLModel(table=True)` y llaves foráneas (`Field(foreign_key="cliente.id")`).
3. Routers con CRUD completo usando `Session(engine)` en todos los métodos.
4. Uso de `lifespan` (moderno) en lugar del deprecado `on_event("startup")`.

GRACIAS INSTRUCTOR JHONNY
