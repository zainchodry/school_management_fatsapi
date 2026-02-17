from sqlalchemy import Column, Integer, String
from app.database import Base

class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    code = Column(String, unique=True)
