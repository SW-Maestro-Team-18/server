from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database.connection import Base


class DbMBTI(Base):
    __tablename__ = 'mbti'
    
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String)
    summary = Column(String)
    description = Column(String)
    testcount = Column(Integer, default=0)
    sharecount = Column(Integer, default=0)
    
    items = relationship('DbComment', back_populates='mbti')


class DbComment(Base):
    __tablename__ = 'comments'
    
    id = Column(Integer, primary_key=True, index=True)
    mbti_id = Column(String, ForeignKey('mbti.id')) 
    text = Column(String)
    datetime = Column(DateTime, default=func.now())
    
    mbti = relationship('DbMBTI', back_populates='items')
    