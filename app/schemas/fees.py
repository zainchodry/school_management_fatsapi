from pydantic import BaseModel
from datetime import date

class FeeCreate(BaseModel):
    class_id: int
    amount: float
    due_date: date


class StudentFeeAssign(BaseModel):
    student_id: int
    fee_id: int