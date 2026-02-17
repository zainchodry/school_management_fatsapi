from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.attendance import *
from app.models.attendance import *
from app.utils.jwt_handler import require_role
from typing import Optional

router = APIRouter(prefix="/attendance", tags=["Attendance"])

@router.post("/mark", dependencies=[Depends(require_role("TEACHER","ADMIN"))])
def mark_attendance(data: AttendanceBulk, db: Session = Depends(get_db)):
    saved = 0

    for item in data.records:
        existing = db.query(Attendance).filter_by(
            student_id=item.student_id,
            date=item.date
        ).first()

        if existing:
            existing.status = item.status
        else:
            att = Attendance(**item.dict())
            db.add(att)
            saved += 1

    db.commit()
    return {"message": f"Attendance marked. New records: {saved}"}

@router.get("/class/{class_id}/section/{section_id}", dependencies=[Depends(require_role("ADMIN","TEACHER"))])
def attendance_by_class_section(
    class_id: int,
    section_id: int,
    date_: Optional[date] = None,
    db: Session = Depends(get_db)
):
    q = db.query(Attendance).filter(
        Attendance.class_id == class_id,
        Attendance.section_id == section_id
    )

    if date_:
        q = q.filter(Attendance.date == date_)

    return q.all()


@router.get("/student/{student_id}", dependencies=[Depends(require_role("STUDENT","ADMIN"))])
def student_attendance(student_id: int, db: Session = Depends(get_db)):
    return db.query(Attendance).filter(Attendance.student_id == student_id).all()