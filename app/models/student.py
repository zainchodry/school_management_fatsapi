from sqlalchemy import Column, Integer, String, ForeignKey, Date
from app.database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    roll_no = Column(String, unique=True)
    class_name = Column(String)
    section = Column(String)
    admission_date = Column(Date)
