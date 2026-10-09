from typing import Literal
from pydantic import BaseModel, ConfigDict, Field, field_validator


class Entrada(BaseModel):
    id_paquete: str
    peso_kg: float = Field(gt=0, le=30)
    distancia_km: float = Field(ge=0, le=200)

    @field_validator("id_paquete", mode="before")
    @classmethod
    def no_vacio(cls, value)
        id_paquete = id_paquete.strip()
        if (id_paquete != ""):
            value = id_paquete
        return value



class Salida(BaseModel):
    id_paquete: str
    peso_kg: Literal["normal", "urgente"]
    confianza: float(ge=0, le=1)

    @field_validator("id_paquete", mode="before")
    @classmethod
    def no_vacio(cls, value)
        if (id_paquete != ""):
            value = id_paquete
        return value
