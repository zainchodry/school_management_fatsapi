from pydantic import BaseModel
from datetime import date

class StudentCreate(BaseModel):
    user_id: int
    roll_no: str
    class_name: str
    section: str

class StudentOut(StudentCreate):
    id: int
    admission_date: date

    class Config:
        orm_mode = True
