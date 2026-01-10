from pydantic import BaseModel

class Pessoa(BaseModel):
    nome: str
    altura: float
    peso: int