from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas
from .database import engine, SessionLocal, Base
import requests

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/evaluaciones", response_model=schemas.EvaluacionOut)
def create_evaluacion(evaluacion: schemas.EvaluacionCreate, db: Session = Depends(get_db)):
    response = requests.get(f"http://estudiante:8000/estudiantes/{evaluacion.rut_estudiante}")
    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="Estudiante no existe")

    nueva = models.Evaluacion(**evaluacion.dict())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

@app.get("/evaluaciones", response_model=list[schemas.EvaluacionOut])
def get_all(db: Session = Depends(get_db)):
    return db.query(models.Evaluacion).all()

@app.get("/evaluaciones/{id}", response_model=schemas.EvaluacionOut)
def get_by_id(id: int, db: Session = Depends(get_db)):
    evaluacion = db.query(models.Evaluacion).filter(models.Evaluacion.id == id).first()
    if not evaluacion:
        raise HTTPException(status_code=404, detail="Evaluación no encontrada")
    return evaluacion