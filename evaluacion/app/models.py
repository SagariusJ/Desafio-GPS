from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Evaluacion(Base):
    __tablename__ = "evaluaciones"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    rut_estudiante = Column(String, nullable=False)
    semestre = Column(String, nullable=False)
    asignatura = Column(String, nullable=False)
    evaluacion = Column(Float, nullable=False)