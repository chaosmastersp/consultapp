from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "API online"}

@app.get("/docs")
def redirect_to_docs():
    from fastapi.responses import RedirectResponse
    return RedirectResponse(url="/docs")
