from pydantic import BaseModel, Field
from typing import Optional


class Transaccion(BaseModel):
    id: int
    cliente_id: int
    monto: float
    descripcion: str


class TransaccionCrear(BaseModel):
    cliente_id: int = Field(..., gt=0, description="ID del cliente asociado")
    monto: float = Field(..., gt=0, description="Monto de la transacción")
    descripcion: str = Field(..., min_length=1, description="Descripción de la transacción")


class TransaccionActualizar(BaseModel):
    cliente_id: Optional[int] = Field(None, gt=0)
    monto: Optional[float] = Field(None, gt=0)
    descripcion: Optional[str] = Field(None, min_length=1)
