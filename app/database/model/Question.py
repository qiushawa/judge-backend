from sqlalchemy import Column, Integer, String, ClauseList
from .Base import Base

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    SampleInput = Column(String, nullable=False) # Base64
    SampleOutput = Column(String, nullable=False) # Base64
    Input = Column(String, nullable=False) # Base64
    Output = Column(String, nullable=False) # Base64

__all__ = ["Question"]
