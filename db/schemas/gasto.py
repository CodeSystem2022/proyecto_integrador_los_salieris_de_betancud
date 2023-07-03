#convierte el gasto obtenido desde la base de datos a un diccionario
def gasto_schema(gasto) -> dict:
    return {
        "id": str(gasto["_id"]),
        "fecha": gasto["fecha"],
        "gasto": gasto["gasto"],
        "monto": gasto["monto"],
        "desc": gasto["desc"]
    }

def gastos_schema(gastos)-> list:
    return[gasto_schema(gasto) for gasto in gastos]