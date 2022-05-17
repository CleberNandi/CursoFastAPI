from typing import Any
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status 
from fastapi.responses import JSONResponse
from fastapi import Response
from fastapi import Path
from fastapi import Depends
from pydantic import Json
from models import Curso

from time import sleep

def fake_db():
    try:
        print(f"Abrindo conexão com banco de dados")
        sleep(4)
    finally:
        print(f"Fechando conexao com banco de dados")
        sleep(1)
        
app = FastAPI()


cursos = {
    1:{
        "titulo": "Programação para Leigos",
        "aulas": 112,
        "horas": 58
    },
    2:{
        "titulo": "Algoritimos e Lógica de Programação",
        "aulas": 87,
        "horas": 67
    }
}

@app.get("/cursos")
async def get_cursos(db: Any = Depends(fake_db)):
    return cursos

@app.get("/cursos/{curso_id}")
async def get_curso(
    curso_id: int = Path(
        default=None,
        title="ID do curso",
        description="Deve ser entre 1 e 2", gt=0, lt=3
    )
):
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado.")

@app.post("/cursos", status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso):
    next_curso:int =  len(cursos) + 1
    cursos[next_curso] = curso
    del curso.id
    return curso
    
@app.put("/cursos/{curso_id}")
async def put_curso(curso_id: int, curso: Curso):
    if curso_id in cursos:
        cursos[curso_id] = curso
        del curso.id
        return curso
    else:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Não existe um curso com ID {curso.id}"
            )

@app.delete("/cursos/{curso_id}")
async def delete_curso(curso_id: int):
    if curso_id in cursos:
        del cursos[curso_id]
        
        return Response(status_code=status.HTTP_204_NO_CONTENT)
        # return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Não existe um curso com ID {curso_id}"
        )

@app.get("/calculadora")
async def calcular(a: int, b: int, c: int):
    soma = a+b+c
    return {"resultado": soma}


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        debug=True
    )