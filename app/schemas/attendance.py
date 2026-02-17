from pydantic import BaseModel
from datetime import date
from typing import List

class AttendanceCreate(BaseModel):
    student_id: int
    class_id: int
    section_id: int
    date: date
    status: bool


class AttendanceBulk(BaseModel):
    records: List[AttendanceCreate]


class AttendanceResponse(BaseModel):
    id: int
    student_id: int
    class_id: int
    section_id: int
    date: date
    status: bool

    class Config:
        from_attributes = True