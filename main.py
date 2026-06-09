from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def inicio():
    return {"message": "¡Hola estoy aprendiendo FastAPI!"}