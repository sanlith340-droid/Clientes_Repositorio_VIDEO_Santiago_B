from fastapi import FastAPI

app = FastAPI()

# Endpoint principal
@app.get("/")
def inicio(Inicio):
    return {
        "mensaje": "Este es el proyecto de clientes a desarrollar"
    }

# Endpoint de clientes
@app.get("/clientes")
def obtener_clientes(lista):
    clientes = [
        {
            "id": 1,
            "nombre": "Ana Perez",
            "edad": 19
        },
        {
            "id": 2,
            "nombre": "Carlos Gomez",
            "edad": 25
        },
        {
            "id": 3,
            "nombre": "Maria Lopez",
            "edad": 30
        }
    ]

    return clientes