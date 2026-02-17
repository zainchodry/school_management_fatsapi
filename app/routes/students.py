from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.student import StudentCreate
from app.models.student import Student
from app.utils.jwt_handler import *

router = APIRouter(prefix="/students", tags=["Students"])

@router.post("/", dependencies=[Depends(require_role("ADMIN"))])
def create_student(data: StudentCreate, db: Session = Depends(get_db)):
    if db.query(Student).filter(Student.roll_no == data.roll_no).first():
        raise HTTPException(400, "Roll number already exists")

    student = Student(**data.dict())
    db.add(student)
    db.commit()
    return {"message": "Student created successfully"}


@router.get("/", dependencies=[Depends(require_role("ADMIN", "TEACHER"))])
def list_students(db: Session = Depends(get_db)):
    return db.query(Student).all()


@router.get("/me", dependencies=[Depends(require_role("STUDENT"))])
def my_record(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return db.query(Student).filter(Student.user_id == current_user.id).first()
