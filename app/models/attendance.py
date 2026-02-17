from sqlalchemy import Column, Integer, Boolean, Date, ForeignKey, UniqueConstraint
from app.database import Base
from sqlalchemy.orm import relationship

class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("users.id"))
    class_id = Column(Integer, ForeignKey("classes.id"))
    section_id = Column(Integer, ForeignKey("sections.id"))
    date = Column(Date)
    status = Column(Boolean)

    __table_args__ = (
        UniqueConstraint("student_id", "date", name="unique_student_day"),
    )
    records = relationship("AttendanceRecord", back_populates="attendance",
                       cascade="all, delete")

    student = relationship("User")
    class_ = relationship("SchoolClass")
    section = relationship("Section")

class AttendanceRecord(Base):
    __tablename__ = "attendance_records"

    id = Column(Integer, primary_key=True, index=True)
    attendance_id = Column(Integer, ForeignKey("attendance.id", ondelete="CASCADE"))
    student_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    is_present = Column(Boolean, default=True)

    __table_args__ = (
        UniqueConstraint("attendance_id", "student_id", name="unique_student_attendance"),
    )

    attendance = relationship("Attendance", back_populates="records")