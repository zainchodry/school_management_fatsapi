from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from app.database import Base

class SchoolClass(Base):
    __tablename__ = "classes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)

    sections = relationship("Section", back_populates="school_class", cascade="all, delete")

class Section(Base):
    __tablename__ = "sections"

    id = Column(Integer, primary_key=True, index=True)
    class_id = Column(Integer, ForeignKey("classes.id"), nullable=False)
    name = Column(String(20), nullable=False)

    school_class = relationship("SchoolClass", back_populates="sections")
    subjects = relationship("ClassSectionSubject", back_populates="section", cascade="all, delete")

    __table_args__ = (
        UniqueConstraint("class_id", "name", name="uq_class_section"),
    )

class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    code = Column(String(20), unique=True, nullable=False)

    mappings = relationship("ClassSectionSubject", back_populates="subject", cascade="all, delete")

class ClassSectionSubject(Base):
    __tablename__ = "class_section_subjects"

    id = Column(Integer, primary_key=True)
    class_id = Column(Integer, ForeignKey("classes.id"), nullable=False)
    section_id = Column(Integer, ForeignKey("sections.id"), nullable=False)
    subject_id = Column(Integer, ForeignKey("subjects.id"), nullable=False)

    section = relationship("Section", back_populates="subjects")
    subject = relationship("Subject", back_populates="mappings")

    __table_args__ = (
        UniqueConstraint("class_id", "section_id", "subject_id", name="uq_class_section_subject"),
    )
