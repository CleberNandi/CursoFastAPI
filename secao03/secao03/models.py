from typing import Optional
from pydantic import BaseModel, validator


class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int
    
    @validator("titulo")
    def validar_titulo(cls, value):
        palavras = value.split(" ")
        if len(palavras) < 3:
            raise ValueError("O Titulo deve ter pelo menos 3 palavras")
        
        return value
    
    
cursos = [
    Curso(id=1, titulo="Programação para Leigos", aulas=42, horas=50),
    Curso(id=2, titulo="Algoritimos e Logica de Programação", aulas=52, horas=90),
    Curso(id=3, titulo="Programação de Python", aulas=24, horas=12)
]