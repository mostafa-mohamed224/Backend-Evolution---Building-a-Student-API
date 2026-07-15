from sqlalchemy.orm import Session
from models import Student


def get_students(db: Session):
    return db.query(Student).all()


def get_student(db: Session, student_id: int):
    return db.query(Student).filter(Student.id == student_id).first()


def create_student(db: Session, student):
    db_student = Student(
        id=student.id,
        name=student.name,
        age=student.age,
        grade=student.grade
    )

    db.add(db_student)
    db.commit()
    db.refresh(db_student)

    return db_student


def update_student(db: Session, student_id, data):
    student = get_student(db, student_id)

    if student:
        student.name = data.name
        student.age = data.age
        student.grade = data.grade

        db.commit()
        db.refresh(student)

    return student


def delete_student(db: Session, student_id):
    student = get_student(db, student_id)

    if student:
        db.delete(student)
        db.commit()

    return student
