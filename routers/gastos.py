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

#Modificar un gasto
@router.put('/{id}',response_model=Gasto,status_code=status.HTTP_200_OK)
async def modificar_gasto(id:str, gasto:Gasto):
    try:
        #convertimos a diccionario
        gasto_dict = gasto.dict()
        #eliminamos el campo id porque no se debe modificar
        del gasto_dict["id"]
        #buscamos por id y remplazamos los datos
        client_db.pagos.find_one_and_update({"_id":ObjectId(id)},gasto_dict)
        
        #recuperamos el gasto actualizado desde la base de datos y lo retornamos como un Objeto Gasto
        return buscar_gasto({"_id",ObjectId(id)})
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="No se elimino el gasto")


