from pydantic import BaseModel

class TeacherCreate(BaseModel):
    user_id: int
    qualification: str
    experience_years: int

class TeacherOut(TeacherCreate):
    id: int

    class Config:
        orm_mode = True
