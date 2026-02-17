from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.class_section import *
from app.models.class_section import *
from app.utils.jwt_handler import require_role

router = APIRouter(prefix="/academics", tags=["Academics"])



@router.post("/classes", dependencies=[Depends(require_role("ADMIN"))])
def create_class(data: ClassCreate, db: Session = Depends(get_db)):
    if db.query(SchoolClass).filter_by(name=data.name).first():
        raise HTTPException(400, "Class already exists")

    cls = SchoolClass(name=data.name)
    db.add(cls)
    db.commit()
    return {"message": "Class created"}


@router.post("/sections", dependencies=[Depends(require_role("ADMIN"))])
def create_section(data: SectionCreate, db: Session = Depends(get_db)):
    if not db.query(SchoolClass).get(data.class_id):
        raise HTTPException(404, "Class not found")

    if db.query(Section).filter_by(class_id=data.class_id, name=data.name).first():
        raise HTTPException(400, "Section already exists")

    sec = Section(**data.dict())
    db.add(sec)
    db.commit()
    return {"message": "Section created"}


@router.post("/subjects", dependencies=[Depends(require_role("ADMIN"))])
def create_subject(data: SubjectCreate, db: Session = Depends(get_db)):
    if db.query(Subject).filter_by(code=data.code).first():
        raise HTTPException(400, "Subject code exists")

    sub = Subject(**data.dict())
    db.add(sub)
    db.commit()
    return {"message": "Subject created"}


@router.post("/assign/class", dependencies=[Depends(require_role("ADMIN"))])
def assign_subject_to_class(data: AssignSubjectSchema, db: Session = Depends(get_db)):
    if not db.query(SchoolClass).get(data.class_id):
        raise HTTPException(404, "Class not found")

    if not db.query(Subject).get(data.subject_id):
        raise HTTPException(404, "Subject not found")

    if db.query(ClassSectionSubject).filter_by(
        class_id=data.class_id,
        subject_id=data.subject_id
    ).first():
        raise HTTPException(400, "Already assigned")

    cs = ClassSectionSubject(class_id=data.class_id, subject_id=data.subject_id)
    db.add(cs)
    db.commit()
    return {"message": "Subject assigned to class"}

@router.post("/assign/section", dependencies=[Depends(require_role("ADMIN"))])
def assign_subject_to_section(data: AssignSubjectSchema, db: Session = Depends(get_db)):
    section = db.query(Section).get(data.section_id)
    if not section:
        raise HTTPException(404, "Section not found")

    if not db.query(Subject).get(data.subject_id):
        raise HTTPException(404, "Subject not found")

    if db.query(ClassSectionSubject).filter_by(
        class_id=data.class_id,
        section_id=data.section_id,
        subject_id=data.subject_id
    ).first():
        raise HTTPException(400, "Already assigned")

    css = ClassSectionSubject(**data.dict())
    db.add(css)
    db.commit()
    return {"message": "Subject assigned to section"}
