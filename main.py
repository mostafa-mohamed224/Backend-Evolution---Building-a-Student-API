from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

import crud
import models
import schemas

from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Student Management API")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/students", response_model=schemas.StudentResponse, status_code=201)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):

    if crud.get_student(db, student.id):
        raise HTTPException(400, "Student ID already exists")

    return crud.create_student(db, student)


@app.get("/students", response_model=list[schemas.StudentResponse])
def get_students(db: Session = Depends(get_db)):
    return crud.get_students(db)


@app.get("/students/{student_id}", response_model=schemas.StudentResponse)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = crud.get_student(db, student_id)

    if not student:
        raise HTTPException(404, "Student not found")

    return student


@app.put("/students/{student_id}", response_model=schemas.StudentResponse)
def update_student(student_id: int,
                   data: schemas.StudentUpdate,
                   db: Session = Depends(get_db)):

    student = crud.update_student(db, student_id, data)

    if not student:
        raise HTTPException(404, "Student not found")

    return student


@app.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):

    student = crud.delete_student(db, student_id)

    if not student:
        raise HTTPException(404, "Student not found")

    return {"message": "Student deleted successfully"}
