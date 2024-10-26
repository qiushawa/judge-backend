from sqlalchemy import Column, Integer, String, ClauseList
from .Base import Base

class User(Base):
    __tablename__ = "users"

    discord_id = Column(Integer, primary_key=True, nullable=False)
    student_id = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    ExP = Column(Integer, nullable=True)

__all__ = ["User"]
