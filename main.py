from fastapi import FastAPI
from routers import gastos

app = FastAPI()

#routers (Se añade el router para gastos) 
#app.include_router(gastos.router)

""" @app.get("/status", status_code=200)
async def status():
    return {"message":"OK"} """