from pydantic import BaseModel

class EstudianteBase(BaseModel):
    rut: str
    nombre_completo: str
    edad: int
    curso: str

class EstudianteCreate(EstudianteBase):
    pass

class EstudianteOut(EstudianteBase):
    class Config:
        orm_mode = True