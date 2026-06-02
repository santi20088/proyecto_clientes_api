from fastapi import APIRouter, HTTPException
from app.models.transacciones import Transaccion, TransaccionCrear, TransaccionActualizar
from app.database import transacciones_db

router = APIRouter(prefix="/transacciones", tags=["Transacciones"])


@router.get("/", response_model=list[Transaccion])
async def listar_transacciones():
    return transacciones_db


@router.post("/", response_model=Transaccion, status_code=201)
async def crear_transaccion(datos: TransaccionCrear):
    nueva = Transaccion(id=len(transacciones_db) + 1, **datos.model_dump())
    transacciones_db.append(nueva)
    return nueva


@router.get("/{id}", response_model=Transaccion)
async def obtener_transaccion(id: int):
    for transaccion in transacciones_db:
        if transaccion.id == id:
            return transaccion
    raise HTTPException(status_code=404, detail="Transacción no encontrada")


@router.put("/{id}", response_model=Transaccion)
async def actualizar_transaccion(id: int, datos: TransaccionActualizar):
    for i, transaccion in enumerate(transacciones_db):
        if transaccion.id == id:
            datos_actualizados = transaccion.model_dump()
            datos_actualizados.update({k: v for k, v in datos.model_dump().items() if v is not None})
            transacciones_db[i] = Transaccion(**datos_actualizados)
            return transacciones_db[i]
    raise HTTPException(status_code=404, detail="Transacción no encontrada")


@router.delete("/{id}", response_model=Transaccion)
async def eliminar_transaccion(id: int):
    for i, transaccion in enumerate(transacciones_db):
        if transaccion.id == id:
            return transacciones_db.pop(i)
    raise HTTPException(status_code=404, detail="Transacción no encontrada")
