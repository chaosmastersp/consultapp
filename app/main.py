from fastapi import FastAPI
from app.routers import auth, marca, upload, consulta
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

app.include_router(auth.router)
app.include_router(marca.router)
app.include_router(upload.router)
app.include_router(consulta.router)

@app.get("/")
def root():
    return {"message": "API online"}
