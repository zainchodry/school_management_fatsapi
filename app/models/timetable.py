from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from app.database import Base
from sqlalchemy.orm import relationship

class Timetable(Base):
    __tablename__ = "timetables"

    id = Column(Integer, primary_key=True)
    class_id = Column(Integer, ForeignKey("classes.id"))
    section_id = Column(Integer, ForeignKey("sections.id"))
    subject_id = Column(Integer, ForeignKey("subjects.id"))
    teacher_id = Column(Integer, ForeignKey("users.id"))
    day = Column(String)
    period = Column(Integer)

    __table_args__ = (
        UniqueConstraint("class_id", "section_id", "day", "period",
                         name="unique_class_period"),
        UniqueConstraint("teacher_id", "day", "period",
                         name="unique_teacher_period"),
    )

    class_ = relationship("SchoolClass")
    section = relationship("Section")
    subject = relationship("Subject")
    teacher = relationship("User")