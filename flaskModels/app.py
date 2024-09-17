from fastapi import FastAPI, HTTPException
from uuid import UUID
from typing import List
from models import User, Role

app = FastAPI()

db: List[User] = [
    User(id=UUID("d611e27a-1e1d-4197-be32-092172e133ea"), first_name="Laysa", last_name="Cipriano", email="laysa@cipriano.com", role=[Role.role_1]),
    User(id=UUID("30b2b9b8-9355-4831-8001-43d62617a9ac"), first_name="Yoann", last_name="Hasraz", email="yoann@hasraz.com", role=[Role.role_2]),
    User(id=UUID("24889bcc-bb0a-473d-bab7-aa9bbc70eeaa"), first_name="Dominic", last_name="Lima", email="dominic@lima.com", role=[Role.role_3]),
]


@app.get("/")
async def root():
    return{"message": "Olá, Lay!"}


@app.get("/api/users")
async def get_users():
    return db;

@app.get("/api/users/{id}")
async def get_user(id: UUID):
    """
    Lista todos os usuários na base de dados:
    - **id**: UUID
    - **first_name**: string
    - **last_name**: string
    - **email**: string
    - **role**: Role
    """
    for user in db:
        if user.id == id:
            return user
    return {"message": "Usuário não encontrado"}

@app.post("/api/users")
async def add_user(user: User):
    """
    Adicionar um usuário na base de dados:
    - **id**: UUID
    - **first_name**: string
    - **last_name**: string
    - **email**: string
    - **role**: Role
    """
    db.append(user)
    return {"id": user.id}


@app.delete("/api/users/{id}")
async def remove_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return {"message": "Usuário removido com sucesso"}
    raise HTTPException( #tratamento de erro para informar ao usuário que não é possível remover um usuário 2x
        status_code=404,
        detail=f"Usuário com ID {id} não encontrado!"
    )