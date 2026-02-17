from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.exam import *
from app.models.exam import *
from app.utils.jwt_handler import require_role
from typing import Optional

router = APIRouter(prefix="/exams", tags=["Exams"])

@router.post("/create", dependencies=[Depends(require_role("ADMIN"))])
def create_exam(data: ExamCreate, db: Session = Depends(get_db)):
    exam = Exam(**data.dict())
    db.add(exam)
    db.commit()
    return {"message": "Exam created"}


@router.post("/marks", dependencies=[Depends(require_role("TEACHER"))])
def add_marks(data: MarkCreate, db: Session = Depends(get_db)):
    res = Result(**data.dict())
    db.add(res)
    db.commit()
    return {"message": "Marks added"}


@router.get("/student/{student_id}", dependencies=[Depends(require_role("ADMIN","STUDENT","PARENT"))])
def student_results(student_id: int, db: Session = Depends(get_db)):
    return db.query(Result).filter(Result.student_id == student_id).all()

