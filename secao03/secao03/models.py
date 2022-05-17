from typing import Optional
from pydantic import BaseModel


class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int
    
    
cursos = [
    Curso(id=1, titulo="Programação para Leigos", aulas=42, horas=50),
    Curso(id=2, titulo="Algoritimos e Logica de Programação", aulas=52, horas=90),
    Curso(id=2, titulo="Programação Python", aulas=24, horas=12)
]