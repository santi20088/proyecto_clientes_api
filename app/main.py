from fastapi import FastAPI
from app.routers import clientes, facturas, transacciones

app = FastAPI(
    title="API Proyecto Clientes",
    description="API para gestión de clientes, facturas y transacciones",
    version="1.0.0"
)

app.include_router(clientes.router)
app.include_router(facturas.router)
app.include_router(transacciones.router)


@app.get("/", tags=["Root"])
async def root():
    return {"mensaje": "Bienvenido a la API de Proyecto Clientes 🚀"}
