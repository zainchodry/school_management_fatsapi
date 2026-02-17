from pydantic import BaseModel
from datetime import date

class ExamCreate(BaseModel):
    name: str
    class_id: int


class MarkCreate(BaseModel):
    exam_id: int
    student_id: int
    subject_id: int
    marks: float