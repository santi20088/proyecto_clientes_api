from contextlib import asynccontextmanager
from fastapi import FastAPI
from routers import clientes, facturas, transacciones
from app.conexion_bd import crear_bd


@asynccontextmanager
async def lifespan(app: FastAPI):
    crear_bd()
    yield


app = FastAPI(
    title="API de Daniel Santiago Rodriguez Cardozo",
    description="Sistema de Gestión - Ficha 3407184",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(clientes.router)
app.include_router(facturas.router)
app.include_router(transacciones.router)


@app.get("/")
def root():
    return {"mensaje": "API Daniel Rodriguez - Hola mundo"}
