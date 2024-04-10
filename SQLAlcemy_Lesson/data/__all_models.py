from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.sqlite import TEXT, INTEGER
from sqlalchemy.orm import relationship

from .database import Base


class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    title = Column(TEXT, nullable=False)

    teachers = relationship('Teacher', back_populates='subject')


class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    name = Column(TEXT, nullable=False)
    subject_id = Column(INTEGER, ForeignKey('subjects.id'))
    subject = relationship('Subject', back_populates='teachers')
