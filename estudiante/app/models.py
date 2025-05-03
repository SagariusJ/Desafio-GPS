from sqlalchemy import Column, String, Integer
from .database import Base

class Estudiante(Base):
    __tablename__ = "estudiantes"

    rut = Column(String, primary_key=True, index=True)
    nombre_completo = Column(String, nullable=False)
    edad = Column(Integer, nullable=False)
    curso = Column(String, nullable=False)