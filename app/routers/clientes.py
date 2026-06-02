from fastapi import APIRouter, HTTPException
from app.models.clientes import Cliente, ClienteCrear, ClienteActualizar
from app.database import clientes_db

router = APIRouter(prefix="/clientes", tags=["Clientes"])


@router.get("/", response_model=list[Cliente])
async def listar_clientes():
    return clientes_db


@router.post("/", response_model=Cliente, status_code=201)
async def crear_cliente(datos: ClienteCrear):
    nuevo = Cliente(id=len(clientes_db) + 1, **datos.model_dump())
    clientes_db.append(nuevo)
    return nuevo


@router.get("/{id}", response_model=Cliente)
async def obtener_cliente(id: int):
    for cliente in clientes_db:
        if cliente.id == id:
            return cliente
    raise HTTPException(status_code=404, detail="Cliente no encontrado")


@router.put("/{id}", response_model=Cliente)
async def actualizar_cliente(id: int, datos: ClienteActualizar):
    for i, cliente in enumerate(clientes_db):
        if cliente.id == id:
            datos_actualizados = cliente.model_dump()
            datos_actualizados.update({k: v for k, v in datos.model_dump().items() if v is not None})
            clientes_db[i] = Cliente(**datos_actualizados)
            return clientes_db[i]
    raise HTTPException(status_code=404, detail="Cliente no encontrado")


@router.delete("/{id}", response_model=Cliente)
async def eliminar_cliente(id: int):
    for i, cliente in enumerate(clientes_db):
        if cliente.id == id:
            return clientes_db.pop(i)
    raise HTTPException(status_code=404, detail="Cliente no encontrado")
