from datetime import datetime
from typing import Optional
from pydantic import BaseModel

#Entidad Gasto
class Gasto(BaseModel):
    id: Optional[str]
    fecha: Optional[datetime]
    monto: float 
    gasto: str
    desc: Optional[str]
