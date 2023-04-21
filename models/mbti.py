from typing import List
from pydantic import BaseModel

from models.comment import Comment


class MBTI(BaseModel):
    type: str
    summary: str
    description: str
    count: int
    comments: List[Comment]

    # for documentation
    class Config:
        schema_extra = {
            "example": {
                "type" : "씨앗방 지박령",
                "summary" : "쏘마 센터는 내가 지킨다! 씨앗방에 뿌리내린 열혈개발자",
                "description" : "씨앗방 지박령 캐릭터를 설명하는 설명글입니다. 이 공간에는 짧은 내용의 캐릭터 설명이 들어갑니다.",
                "count" : 1,
                "comments" : []
            }
        }


class ShowCount(BaseModel):
    class Config:
        orm_mode = True

    type: str
    count: int
