from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.fees import *
from app.models.fees import *
from app.utils.jwt_handler import require_role
from typing import Optional

router = APIRouter(prefix="/fees", tags=["Fees"])

@router.post("/structure", dependencies=[Depends(require_role("ADMIN"))])
def create_fee_structure(data: FeeCreate, db: Session = Depends(get_db)):
    fee = FeeStructure(**data.dict())
    db.add(fee)
    db.commit()
    return {"message": "Fee structure created"}


@router.post("/assign", dependencies=[Depends(require_role("ADMIN"))])
def assign_fee(data: StudentFeeAssign, db: Session = Depends(get_db)):
    sf = StudentFee(**data.dict())
    db.add(sf)
    db.commit()
    return {"message": "Fee assigned to student"}


@router.get("/student/{student_id}", dependencies=[Depends(require_role("ADMIN","STUDENT","PARENT"))])
def view_student_fees(student_id: int, db: Session = Depends(get_db)):
    return db.query(StudentFee).filter(StudentFee.student_id == student_id).all()