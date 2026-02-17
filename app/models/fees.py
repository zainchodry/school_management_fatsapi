from sqlalchemy import Column, Integer, ForeignKey, Boolean, Date, Float
from app.database import Base

class FeeStructure(Base):
    __tablename__ = "fee_structures"
    id = Column(Integer, primary_key=True)
    class_id = Column(Integer, ForeignKey("classes.id"))
    amount = Column(Float)
    due_date = Column(Date)


class StudentFee(Base):
    __tablename__ = "student_fees"
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("users.id"))
    fee_id = Column(Integer, ForeignKey("fee_structures.id"))
    is_paid = Column(Boolean, default=False)
    paid_on = Column(Date, nullable=True)