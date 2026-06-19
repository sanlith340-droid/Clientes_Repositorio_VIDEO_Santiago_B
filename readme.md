#SANTIAGO BUITRAGO GOYENECHE 
NOTAS 

primero creamos el entorno virtual 

python -m venv venv // 

se crea una carpeta automaticamente la carpeta venv 

// ACTIVAR ENTORNO //

.\venv\scripts\activate

//intalar flask //

pip install "fastapi[standard]"

para actulizar : python.exe -m pip install --upgrade pip

//notasn extra//

venv _ entorno virtual
raiz - carpeta
servidor - unicon

//CREACION DEL MAIN// 

Ahora empezamos a construir los end points 


para iniciar el proyecto o iniciar el servidor usa : fastapi dev main.py 


@app.get("/")
def inicio(Inicio):
    return {
        "mensaje": "Este es el proyecto de clientes a desarrollar"
    }

CREAMOS un get donde nos retorna un mensaje que dice "Este es el proyecto de clientes a desarrollar" Es un comando sencillo donde defines una variable como es inicio y defines la url en este caso es Inico puedes agregar mas para hacer otros mensaje o funciones 

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

DESPUES TENEMOS LA LISTA CLIENTES al igual que la anterior definimos unas variables y creamos una lista de clientes, en mi caso agregue cosas como un id unico y nombre junto con la edad, la avriable definida es obtener_clientes y con esto terminamos con el 2 endpoint 