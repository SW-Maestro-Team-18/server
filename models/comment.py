from datetime import datetime

from pydantic import BaseModel


class Comment(BaseModel):
    type_id: int
    text: str

    # for documentation
    class Config:        
        schema_extra = {
            "example": {
                "type_id": "1",
                "text": "밥 먹을 팟 구해요 인스타 아이디 : @git_jisu",
                "password": "1234"
            }
        }
        
        
class ShowComment(Comment):
    id: int
    datetime: datetime
    
    class Config:
        orm_mode = True
    
    
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
                "id": "1",
                "password": "1234"
            }
        }
        