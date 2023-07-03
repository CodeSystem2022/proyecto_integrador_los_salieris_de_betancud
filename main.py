from fastapi import FastAPI

app = FastAPI()

@app.get("/status", status_code=200)
async def status():
    return {"message":"OK"}