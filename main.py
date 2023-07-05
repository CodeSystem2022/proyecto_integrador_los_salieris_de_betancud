from fastapi import FastAPI
from routers import gastos

description="""
    API REST para la gestión de gastos
    Proyecto integrador tercer semestre grupo Los salieries de betancud.
    Consulte el endpoint /docs para la documentación Swagger y el endpoint /redoc para la
    documentación ReDoc
"""
app = FastAPI(
    title="Gestión de Gastos",
    description=description
)

#routers (Se añade el router para gastos) 
app.include_router(gastos.router)

@app.get("/status", status_code=200)
async def status():
    return {"message":"OK"}