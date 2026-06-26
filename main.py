from fastapi import FastAPI

app = FastAPI()

@app.get("/saludo")
def saludar():
    return {"mensaje": "¡Hola desde la nueva funcionalidad!"}