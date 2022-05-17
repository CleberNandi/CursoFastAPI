from http.client import HTTPException
from fastapi import APIRouter
from fastapi import Path
from fastapi import status
from models import cursos


curso_router = APIRouter()


@curso_router.get("/api/v1/cursos")
async def get_cursos():
    return cursos

@curso_router.get("/api/v1/cursos/{curso_id}")
async def get_cursos(
    curso_id: int = Path(
        default=None,
        title="ID do curso",
        description="Deve ser entre 1 e 2", gt=0, lt=3
    )
):
    try:
        print(cursos)
        return cursos[curso_id]
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado.")


@curso_router.get("/api/v1/cursos")
async def get_cursos():
    return cursos
