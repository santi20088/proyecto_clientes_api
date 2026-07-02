from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select

from app.conexion_bd import get_session
from app.modelos.Transacciones import Transaccion, TransaccionCrear
from app.modelos.Clientes import Cliente

router = APIRouter(
    prefix="/transacciones",
    tags=["Transacciones"]
)


@router.get("/", response_model=list[Transaccion])
def listar_transacciones(session: Session = Depends(get_session)):
    return session.exec(select(Transaccion)).all()


@router.post("/", response_model=Transaccion)
def crear_transaccion(datos_transaccion: TransaccionCrear, session: Session = Depends(get_session)):
    cliente = session.get(Cliente, datos_transaccion.cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="El cliente no existe")
    transaccion = Transaccion.model_validate(datos_transaccion)
    session.add(transaccion)
    session.commit()
    session.refresh(transaccion)
    return transaccion


@router.get("/{id}", response_model=Transaccion)
def obtener_transaccion(id: int, session: Session = Depends(get_session)):
    transaccion = session.get(Transaccion, id)
    if not transaccion:
        raise HTTPException(status_code=404, detail="Transacción no encontrada")
    return transaccion


@router.put("/{id}", response_model=Transaccion)
def actualizar_transaccion(id: int, datos_transaccion: TransaccionCrear, session: Session = Depends(get_session)):
    transaccion = session.get(Transaccion, id)
    if not transaccion:
        raise HTTPException(status_code=404, detail="Transacción no encontrada")
    cliente = session.get(Cliente, datos_transaccion.cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="El cliente no existe")
    transaccion.cliente_id = datos_transaccion.cliente_id
    transaccion.monto = datos_transaccion.monto
    transaccion.descripcion = datos_transaccion.descripcion
    session.add(transaccion)
    session.commit()
    session.refresh(transaccion)
    return transaccion


@router.delete("/{id}")
def eliminar_transaccion(id: int, session: Session = Depends(get_session)):
    transaccion = session.get(Transaccion, id)
    if not transaccion:
        raise HTTPException(status_code=404, detail="Transacción no encontrada")
    session.delete(transaccion)
    session.commit()
    return {"mensaje": "Transacción eliminada correctamente"}
