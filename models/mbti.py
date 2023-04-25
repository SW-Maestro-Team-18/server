from typing import List
from pydantic import BaseModel


# link count 추가
class MBTI(BaseModel):
    type: str
    description: str
    
    class Config:
        orm_mode = True
        
        schema_extra = {
            "example": {
                "type" : "씨앗방 지박령",
                "description": "설명" 
            }
        }
    

class ShowMBTI(MBTI):
    id: int
    
    
class ShowTestCount(BaseModel):
    id: int
    type: str
    testcount: int
    
    class Config:
        orm_mode = True
        
        schema_extra = {
            "example": {
                "type" : "씨앗방 지박령",
                "testcount": "1"
            }
        }


class ShowShareCount(BaseModel):
    id: int
    type: str
    sharecount: int
    
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
                "choices" : [0,1,0,1,1,0,0,1,1]
            }
        }
    