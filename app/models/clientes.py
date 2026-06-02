from pydantic import BaseModel, Field
from typing import Optional


class Cliente(BaseModel):
    id: int
    nombre: str
    edad: int
    descripcion: str


class ClienteCrear(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=100, description="Nombre del cliente")
    edad: int = Field(..., gt=0, lt=150, description="Edad del cliente")
    descripcion: str = Field(..., min_length=1, description="Descripción del cliente")


class ClienteActualizar(BaseModel):
    nombre: Optional[str] = Field(None, min_length=1, max_length=100)
    edad: Optional[int] = Field(None, gt=0, lt=150)
    descripcion: Optional[str] = Field(None, min_length=1)
