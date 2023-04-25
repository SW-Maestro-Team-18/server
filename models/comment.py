from datetime import datetime

from pydantic import BaseModel


class Comment(BaseModel):
    type_id: int
    text: str   
                
        
class ShowComment(BaseModel):
    id: int
    type_id: int
    text: str
    datetime: datetime
    
    class Config:
        orm_mode = True
        
        schema_extra = {
            "example": {
                "id": 1,
                "type_id": "1",
                "text": "밥 먹을 팟 구해요 인스타 아이디 : @git_jisu",
                "datetime": "2023-04-24T13:03:23"
            }
        }
            
    
class CommentCreate(Comment):
    password: str = '1234'
    
    class Config:
        orm_mode = True
        
        schema_extra = {
            "example": {
                "type_id": "1",
                "text": "밥 먹을 팟 구해요 인스타 아이디 : @git_jisu",
                "password": "1234"
            }
        }


class CommentDelete(BaseModel):
    id: int
    password: str
    
    class Config:
        orm_mode = True
        
        schema_extra = {
            "example": {
                "id": "1",
                "password": "1234"
            }
        }
        