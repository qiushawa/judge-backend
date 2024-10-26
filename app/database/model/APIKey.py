from sqlalchemy import Column, Integer, String
from app.database.model.Base import Base

class APIKey(Base):
    __tablename__ = 'api_keys'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, unique=True, nullable=False)
    api_key = Column(String, unique=True, nullable=False) # hash


__all__ = ["APIKey"]
