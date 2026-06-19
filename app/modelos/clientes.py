from pydantic import BaseModel

<<<<<<< HEAD

#crear el modelo clientes (id, nombre, email, descripcion)
=======
>>>>>>> f3786b8d242ecf9db67ad78ddb117ed5b98668c7
class ClienteBase(BaseModel):
    nombre: str
    email: str
    descripcion: str

<<<<<<< HEAD
class Clientecrear(ClienteBase):
=======
class ClienteCrear(ClienteBase):
>>>>>>> f3786b8d242ecf9db67ad78ddb117ed5b98668c7
    pass

class ClienteEditar(ClienteBase):
    pass

<<<<<<< HEAD
=======

>>>>>>> f3786b8d242ecf9db67ad78ddb117ed5b98668c7
class Cliente(ClienteBase):
    id: int | None = None