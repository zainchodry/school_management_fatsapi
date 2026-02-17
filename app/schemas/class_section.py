from pydantic import BaseModel

class ClassCreate(BaseModel):
    name: str


class SectionCreate(BaseModel):
    class_id: int
    name: str


class SubjectCreate(BaseModel):
    name: str
    code: str


class AssignSubjectSchema(BaseModel):
    class_id: int
    section_id: int
    subject_id: int
