from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas
from .database import engine, SessionLocal, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/estudiantes", response_model=schemas.EstudianteOut)
def create_estudiante(estudiante: schemas.EstudianteCreate, db: Session = Depends(get_db)):
    db_est = db.query(models.Estudiante).filter(models.Estudiante.rut == estudiante.rut).first()
    if db_est:
        raise HTTPException(status_code=400, detail="Estudiante ya existe")
    nuevo = models.Estudiante(**estudiante.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@app.get("/estudiantes", response_model=list[schemas.EstudianteOut])
def get_all(db: Session = Depends(get_db)):
    return db.query(models.Estudiante).all()

@app.get("/estudiantes/{rut}", response_model=schemas.EstudianteOut)
def get_by_rut(rut: str, db: Session = Depends(get_db)):
    estudiante = db.query(models.Estudiante).filter(models.Estudiante.rut == rut).first()
    if not estudiante:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return estudiante