from datetime import datetime

from pydantic import BaseModel


class Comment(BaseModel):
    id: int
    type: str
    text: str
    # time: datetime

    # for documentation
    class Config:
        schema_extra = {
            "example": {
                "id": "123",
                "type": "씨앗방 지박령",
                "text": "밥 먹을 팟 구해요 인스타 아이디 : @git_jisu",
                "password": "1234"
            }
        }
        
        
class ShowComment(BaseModel):
    class Config:
        orm_mode = True
    
    type: str
    text: str
    
    
class CommentCreate(Comment):
    password: str = '1234'
    
    class Config:
        orm_mode = True


class CommentDelete(BaseModel):
    id: int
    password: str
    
    class Config:
        orm_mode = True
        
        schema_extra = {
            "example": {
                "id": "123",
                "password": "1234"
            }
        }
        