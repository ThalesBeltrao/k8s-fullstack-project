from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Pessoa
from repository import criar_usuario



app = FastAPI(title="API de Cadastro")



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/usuarios")
def usuario(pessoa: Pessoa):
    criar_usuario(pessoa)
    return {
        "mensagem": "Usuário criado com sucesso",
        "dados": pessoa.model_dump()
    }




