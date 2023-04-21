from typing import List

from fastapi import APIRouter
from pydantic import BaseModel

from models import MBTI

mbti_router = APIRouter(
    tags=["mbti"]
)

# 일단 DB를 안쓴다고 가정
mbti: list[MBTI] = [
    MBTI(
        type="씨앗방 지박령",
        summary="쏘마 센터는 내가 지킨다! 씨앗방에 뿌리내린 열혈개발자",
        description="씨앗방 지박령 캐릭터를 설명하는 설명글입니다. 이 공간에는 짧은 내용의 캐릭터 설명이 들어갑니다.",
        count=0
    ),
    MBTI(
        type="아이디어 자동생성기",
        summary="아이디어가 떠오르는 순간, 바로 개발을 시작한다!",
        description="아이디어 자동생성기 캐릭터를 설명하는 설명글입니다. 이 공간에는 짧은 내용의 캐릭터 설명이 들어갑니다.",
        count=0
    )
]

class Count(BaseModel):
    value: int

@mbti_router.get("/count")
async def get_all_count() -> int:
    count = Count(count=0)
    for i in mbti:
        count.value += i.count

    return count

@mbti_router.get("/count")
async def get_all_count() -> int:
    count = 0
    for i in mbti:
        count += i.count

    return count

@mbti_router.get("/count_each")
async def get_all_count() -> int:
    count_list: List = []
    for i in mbti:
        count_list.append(i.count)

    return count_list


@mbti_router.get("/get_comment/{type}_{num_of_comments)")
async def get_comment(type: int, num_of_comments: int) -> int:
    comment_list = mbti[type].comment

    return comment_list[:num_of_comments]