# Proyecto Clientes API

API REST construida con FastAPI para gestión de clientes, facturas y transacciones.

## Estructura del proyecto

```
proyecto_clientes/
├── app/
│   ├── __init__.py
│   ├── main.py          <- Punto de entrada de la API
│   ├── database.py      <- Almacenamiento en memoria
│   ├── models/          <- Modelos Pydantic
│   │   ├── __init__.py
│   │   ├── clientes.py
│   │   ├── facturas.py
│   │   └── transacciones.py
│   └── routers/         <- Endpoints (APIRouter)
│       ├── __init__.py
│       ├── clientes.py
│       ├── facturas.py
│       └── transacciones.py
├── venv/
├── requirements.txt
└── README.md
```

## Instalación

```bash
pip install -r requirements.txt
```

## Correr el servidor

```bash
uvicorn app.main:app --reload
```

## Documentación

Una vez corriendo, visita: http://127.0.0.1:8000/docs
```
