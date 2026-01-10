from database import get_connection
from models import Pessoa

def criar_usuario(usuario: Pessoa):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO usuario (nome, altura, peso)
        VALUES (%s, %s, %s)
    """
    cursor.execute(query, (usuario.nome, usuario.altura, usuario.peso))

    conn.commit()
    cursor.close()
    conn.close()
