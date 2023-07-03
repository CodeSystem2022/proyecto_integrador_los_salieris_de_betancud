from fastapi import APIRouter, HTTPException, Response,status
from bson import ObjectId
from db.models.Gasto import Gasto
from db.client import client_db
from db.schemas.gasto import gasto_schema, gastos_schema

#se define el router con el prefijo gastos 
router = APIRouter(prefix="/gastos")

#Retorna todos los gastos
@router.get('/',response_model=list[Gasto], status_code=status.HTTP_200_OK)
async def obtener_gastos():
    return gastos_schema(client_db.gastos.find())