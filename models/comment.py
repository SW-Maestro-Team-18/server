from sqlalchemy import Column, DateTime,Integer, String
from sqlalchemy.sql import func

from database import Base


class Comment(Base):
    __tablename__ = 'comments'

    id: Column(Integer, primary_key=True, index=True)
    mbti_type: Column(String)
    text: Column(String)
    timestamp: Column(DateTime, default=func.now())
