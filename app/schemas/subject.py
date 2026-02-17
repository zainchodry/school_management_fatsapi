from pydantic import BaseModel

class SubjectCreate(BaseModel):
    name: str
    code: str

class SubjectOut(SubjectCreate):
    id: int

    class Config:
        orm_mode = True
