from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class DbMBTI(Base):
    """
    
    Args:
        id, type, summary, description, count
    """
    __tablename__ = 'MBTI'

    type = Column(String, primary_key=True, index=True)
    summary = Column(String)
    description = Column(String)
    # count = Column(Integer)

    comments = relationship("DbComment", back_populates="mbti")


class DbComment(Base):
    """

    Args:
        id, mbti_type, text, timestamp
    """
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True, index=True)
    mbti_type = Column(Integer, ForeignKey("MBTI.type"))
    text = Column(String)
    timestamp = Column(DateTime, default=func.now())

    mbti = relationship("DbMBTI", back_populates="comments")
