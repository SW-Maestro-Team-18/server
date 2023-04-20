from sqlalchemy import Column, Integer, String

from database import Base

class DbMBTI(Base):
    """
        id, type, summary, description, count
    """
    __tablename__ = 'MBTI'

    id: Column(Integer, primary_key=True, index=True)
    type: Column(String)
    summary: Column(String)
    description: Column(String)
    count: Column(Integer)
