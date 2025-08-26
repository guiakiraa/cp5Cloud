from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import mysql.connector
from urllib.parse import urlparse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db_url = os.environ.get("DATABASE_URL")
url = urlparse(db_url)

class UsuarioBase(BaseModel):
    nome: str
    email: str

class UsuarioCreate(UsuarioBase):
    pass

class Usuario(UsuarioBase):
    id: int

    class Config:
        from_attributes = True

def get_connection():
    return mysql.connector.connect(
        host=url.hostname,
        user=url.username,
        password=url.password,
        database=url.path[1:],  # remove o /
        port=url.port
    )

@app.get("/")
def root():
    return {"message": "FastAPI com MySQL funcionando!"}

@app.get("/usuarios")
def listar_usuarios():
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuario")
        usuarios = cursor.fetchall()
        cursor.close()
        conn.close()
        return {"usuarios": usuarios}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/usuarios/{usuario_id}")
def obter_usuario(usuario_id: int):
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuario WHERE id = %s", (usuario_id,))
        usuario = cursor.fetchone()
        cursor.close()
        conn.close()
        
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
            
        return usuario
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/usuarios")
def criar_usuario(usuario: UsuarioCreate):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO usuario (nome, email) VALUES (%s, %s)",
            (usuario.nome, usuario.email)
        )
        conn.commit()
        novo_id = cursor.lastrowid
        cursor.close()
        conn.close()
        
        return {"id": novo_id, **usuario.dict()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/usuarios/{usuario_id}")
def atualizar_usuario(usuario_id: int, usuario: UsuarioCreate):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        # Verifica se o usuário existe
        cursor.execute("SELECT id FROM usuario WHERE id = %s", (usuario_id,))
        if not cursor.fetchone():
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        
        cursor.execute(
            "UPDATE usuario SET nome = %s, email = %s WHERE id = %s",
            (usuario.nome, usuario.email, usuario_id)
        )
        conn.commit()
        cursor.close()
        conn.close()
        
        return {"id": usuario_id, **usuario.dict()}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/usuarios/{usuario_id}")
def deletar_usuario(usuario_id: int):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        # Verifica se o usuário existe
        cursor.execute("SELECT id FROM usuario WHERE id = %s", (usuario_id,))
        if not cursor.fetchone():
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        
        cursor.execute("DELETE FROM usuario WHERE id = %s", (usuario_id,))
        conn.commit()
        cursor.close()
        conn.close()
        
        return {"message": "Usuário deletado com sucesso"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
