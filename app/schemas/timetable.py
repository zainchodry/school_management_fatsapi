from pydantic import BaseModel

class TimetableCreate(BaseModel):
    class_id: int
    section_id: int
    subject_id: int
    teacher_id: int
    day: str
    period: int


class TimetableResponse(TimetableCreate):
    id: int

    class Config:
        from_attributes = True
