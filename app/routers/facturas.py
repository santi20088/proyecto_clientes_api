from fastapi import APIRouter, HTTPException
from app.models.facturas import Factura, FacturaCrear, FacturaActualizar
from app.database import facturas_db

router = APIRouter(prefix="/facturas", tags=["Facturas"])


@router.get("/", response_model=list[Factura])
async def listar_facturas():
    return facturas_db


@router.post("/", response_model=Factura, status_code=201)
async def crear_factura(datos: FacturaCrear):
    nueva = Factura(id=len(facturas_db) + 1, **datos.model_dump())
    facturas_db.append(nueva)
    return nueva


@router.get("/{id}", response_model=Factura)
async def obtener_factura(id: int):
    for factura in facturas_db:
        if factura.id == id:
            return factura
    raise HTTPException(status_code=404, detail="Factura no encontrada")


@router.put("/{id}", response_model=Factura)
async def actualizar_factura(id: int, datos: FacturaActualizar):
    for i, factura in enumerate(facturas_db):
        if factura.id == id:
            datos_actualizados = factura.model_dump()
            datos_actualizados.update({k: v for k, v in datos.model_dump().items() if v is not None})
            facturas_db[i] = Factura(**datos_actualizados)
            return facturas_db[i]
    raise HTTPException(status_code=404, detail="Factura no encontrada")


@router.delete("/{id}", response_model=Factura)
async def eliminar_factura(id: int):
    for i, factura in enumerate(facturas_db):
        if factura.id == id:
            return facturas_db.pop(i)
    raise HTTPException(status_code=404, detail="Factura no encontrada")
