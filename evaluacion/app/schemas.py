from pydantic import BaseModel, confloat

class EvaluacionBase(BaseModel):
    rut_estudiante: str
    semestre: str
    asignatura: str
    evaluacion: confloat(ge=1.0, le=7.0)

class EvaluacionCreate(EvaluacionBase):
    pass

class EvaluacionOut(EvaluacionBase):
    id: int

    class Config:
        orm_mode = True