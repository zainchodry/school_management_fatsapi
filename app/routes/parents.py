from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.attendance import *
from app.models.attendance import *
from app.utils.jwt_handler import require_role
from typing import Optional
from app.models.attendance import AttendanceRecord
from app.models.fees import StudentFee
from app.models.exam import Result

router = APIRouter(prefix="/parents", tags=["Parents"])

class ParentStudent(Base):
    __tablename__ = "parent_students"
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey("users.id"))
    student_id = Column(Integer, ForeignKey("users.id"))


@router.get("/children", dependencies=[Depends(require_role("PARENT"))])
def my_children(user=Depends(require_role("PARENT")), db: Session = Depends(get_db)):
    return db.query(ParentStudent).filter(
        ParentStudent.parent_id == user.id
    ).all()

@router.get("/attendance/{student_id}", dependencies=[Depends(require_role("PARENT"))])
def child_attendance(student_id: int, db: Session = Depends(get_db)):
    return db.query(AttendanceRecord).filter(
        AttendanceRecord.student_id == student_id
    ).all()


@router.get("/fees/{student_id}", dependencies=[Depends(require_role("PARENT"))])
def child_fees(student_id: int, db: Session = Depends(get_db)):
    return db.query(StudentFee).filter(
        StudentFee.student_id == student_id
    ).all()


@router.get("/results/{student_id}", dependencies=[Depends(require_role("PARENT"))])
def child_results(student_id: int, db: Session = Depends(get_db)):
    return db.query(Result).filter(
        Result.student_id == student_id
    ).all()
