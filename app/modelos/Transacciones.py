from typing import Optional
from sqlmodel import SQLModel, Field


class Transaccion(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    cliente_id: int = Field(foreign_key="cliente.id")
    monto: float
    descripcion: Optional[str] = None


class TransaccionCrear(SQLModel):
    cliente_id: int
    monto: float
    descripcion: Optional[str] = None
