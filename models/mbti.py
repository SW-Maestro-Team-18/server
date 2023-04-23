from typing import List
from pydantic import BaseModel

from models.comment import Comment


# link count 추가
class MBTI(BaseModel):
    type: str
    summary: str
    description: str
    count: int    


class ShowMBTI(MBTI):
    type: str
    summary: str
    description: str
    
    class Config:
        orm_mode = True
        
        schema_extra = {
                "example": {
                    "type" : "씨앗방 지박령",
                    "summary": "쏘마 센터는 내가 지킨다! 씨앗방에 뿌리내린 열혈개발자",
                    "description": "설명"
                }
        }
        
        error_msg_templates = {}
    
    
class ShowTestCount(BaseModel):
    type: str
    count: int
    
    class Config:
        orm_mode = True
        
        schema_extra = {
            "example": {
                "type" : "씨앗방 지박령",
                "testcount": "1"
            }
        }
        
        error_msg_templates = {}


class ShowShareCount(BaseModel):
    type: str
    count: int
    
    class Config:
        orm_mode = True
        
        schema_extra = {
            "example": {
                "type" : "씨앗방 지박령",
                "sharecount": "11"
            }
        }
        
        error_msg_templates = {}


class Choice(BaseModel):
    choices: List[int]
    
    class Config:
        orm_mode = True
        
        schema_extra = {
            "example": {
                "choices" : "[0,1,0,1,1,0,0,1,1]"
            }
        }