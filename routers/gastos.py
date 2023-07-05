from fastapi import APIRouter, HTTPException, Response,status
from bson import ObjectId
from db.models.Gasto import Gasto
from db.client import client_db
from db.schemas.gasto import gasto_schema, gastos_schema

#se define el router con el prefijo gastos 
router = APIRouter(prefix="/gastos")

#crear un gasto y guardar en la base de datos
@router.post('/',response_model=Gasto,status_code=status.HTTP_201_CREATED)
async def crear_gasto(gasto: Gasto):
    #transformamos los datos a un diccionario para poder almacenarlo en la base de datos
    _gasto = dict(gasto)
    #eliminarmos el campo id ya que el mismo se genera de forma automatica al guardar en db
    del _gasto["id"]
    # guardamos el gasto en la base de datos y obtenemos su id
    # Se utiliza la instancia client_db usando la base de datos app_gastos
    id =client_db.gastos.insert_one(_gasto).inserted_id
    
    #se obtiene el nuevo gasto desde la base de datos buscando por el (_id) ya que utilizamos mongodb y 
    #se convierte a un diccionario
    nuevo_gasto = gasto_schema(client_db.gastos.find_one({"_id": id}))
    
    #Se crea un objeto Gasto y se retorna
    return Gasto(**nuevo_gasto)

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


