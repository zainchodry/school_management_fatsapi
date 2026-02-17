from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    qualification = Column(String)
    experience_years = Column(Integer)
