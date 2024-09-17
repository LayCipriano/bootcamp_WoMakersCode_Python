from pydantic import BaseModel #base model, esqueleto base da modelagem de dados
from uuid import UUID, uuid4 #gerar ID's para trabalhar de forma dinâmica, gerar ID's randomicos
from typing import Optional, List #preenchimento opcional
from enum import Enum #trabalhar com a lista de características, o perfil de acesso do usuário dentro do sistema


class Role(str, Enum):
    role_1 = "admin"
    role_2 = "aluna"
    role_3 = "instrutora"



class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    email: str
    role: List[Role]