from fastapi import FastAPI
from app.routers import auth, marcas, upload, consulta

app = FastAPI()

app.include_router(auth.router)
app.include_router(marcas.router)
app.include_router(upload.router)
app.include_router(consulta.router)

@app.get("/")
def root():
    return {"status": "API online"}
