from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.timetable import *
from app.models.timetable import *
from app.utils.jwt_handler import require_role
from typing import Optional

router = APIRouter(prefix="/timetable", tags=["Timetable"])

@router.post("/add", dependencies=[Depends(require_role("ADMIN"))])
def add_period(data: TimetableCreate, db: Session = Depends(get_db)):
    clash1 = db.query(Timetable).filter_by(
        class_id=data.class_id,
        section_id=data.section_id,
        day=data.day,
        period=data.period
    ).first()

    clash2 = db.query(Timetable).filter_by(
        teacher_id=data.teacher_id,
        day=data.day,
        period=data.period
    ).first()

    if clash1:
        raise HTTPException(400, "Class already has a period at this time")

    if clash2:
        raise HTTPException(400, "Teacher is busy at this time")

    tt = Timetable(**data.dict())
    db.add(tt)
    db.commit()
    return {"message": "Period added successfully"}

@router.get("/class/{class_id}/section/{section_id}",
            dependencies=[Depends(require_role("ADMIN","TEACHER","STUDENT"))])
def class_timetable(class_id: int, section_id: int, db: Session = Depends(get_db)):
    return db.query(Timetable).filter_by(
        class_id=class_id,
        section_id=section_id
    ).all()


@router.get("/teacher/{teacher_id}", dependencies=[Depends(require_role("ADMIN","TEACHER"))])
def teacher_timetable(teacher_id: int, db: Session = Depends(get_db)):
    return db.query(Timetable).filter(
        Timetable.teacher_id == teacher_id
    ).all()