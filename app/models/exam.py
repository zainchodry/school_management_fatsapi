from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float
from app.database import Base

class Exam(Base):
    __tablename__ = "exams"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    class_id = Column(Integer, ForeignKey("classes.id"))


class Result(Base):
    __tablename__ = "results"
    id = Column(Integer, primary_key=True)
    exam_id = Column(Integer, ForeignKey("exams.id"))
    student_id = Column(Integer, ForeignKey("users.id"))
    subject_id = Column(Integer, ForeignKey("subjects.id"))
    marks = Column(Float)