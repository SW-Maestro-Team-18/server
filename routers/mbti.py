from typing import List

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from models import Comment, MBTI, ShowComment, ShowShareCount, ShowTestCount
from models.choices import Choice
from utils import get_mbti
from models import MBTI, ShowShareCount, ShowTestCount

mbti_router = APIRouter(
    tags=["mbti"]
)

# 일단 DB를 안쓴다고 가정
mbti: list[MBTI] = [
    MBTI(
        type="씨앗방 지박령",
        summary="쏘마 센터는 내가 지킨다! 씨앗방에 뿌리내린 열혈개발자",
        description="씨앗방 지박령 캐릭터를 설명하는 설명글입니다. 이 공간에는 짧은 내용의 캐릭터 설명이 들어갑니다.",
        count=2
    ),
    MBTI(
        type="아이디어 자동생성기",
        summary="아이디어가 떠오르는 순간, 바로 개발을 시작한다!",
        description="아이디어 자동생성기 캐릭터를 설명하는 설명글입니다. 이 공간에는 짧은 내용의 캐릭터 설명이 들어갑니다.",
        count=3
    ),
    MBTI(
        type="씨앗방 지박령",
        summary="쏘마 센터는 내가 지킨다! 씨앗방에 뿌리내린 열혈개발자",
        description="씨앗방 지박령 캐릭터를 설명하는 설명글입니다. 이 공간에는 짧은 내용의 캐릭터 설명이 들어갑니다.",
        count=2
    ),
    MBTI(
        type="아이디어 자동생성기",
        summary="아이디어가 떠오르는 순간, 바로 개발을 시작한다!",
        description="아이디어 자동생성기 캐릭터를 설명하는 설명글입니다. 이 공간에는 짧은 내용의 캐릭터 설명이 들어갑니다.",
        count=3
    ),
    MBTI(
        type="씨앗방 지박령",
        summary="쏘마 센터는 내가 지킨다! 씨앗방에 뿌리내린 열혈개발자",
        description="씨앗방 지박령 캐릭터를 설명하는 설명글입니다. 이 공간에는 짧은 내용의 캐릭터 설명이 들어갑니다.",
        count=2
    ),
    MBTI(
        type="아이디어 자동생성기",
        summary="아이디어가 떠오르는 순간, 바로 개발을 시작한다!",
        description="아이디어 자동생성기 캐릭터를 설명하는 설명글입니다. 이 공간에는 짧은 내용의 캐릭터 설명이 들어갑니다.",
        count=3
    ),
    MBTI(
        type="아이디어 자동생성기",
        summary="아이디어가 떠오르는 순간, 바로 개발을 시작한다!",
        description="아이디어 자동생성기 캐릭터를 설명하는 설명글입니다. 이 공간에는 짧은 내용의 캐릭터 설명이 들어갑니다.",
        count=3
    ),
    MBTI(
        type="씨앗방 지박령",
        summary="쏘마 센터는 내가 지킨다! 씨앗방에 뿌리내린 열혈개발자",
        description="씨앗방 지박령 캐릭터를 설명하는 설명글입니다. 이 공간에는 짧은 내용의 캐릭터 설명이 들어갑니다.",
        count=2
    ),
    MBTI(
        type="아이디어 자동생성기",
        summary="아이디어가 떠오르는 순간, 바로 개발을 시작한다!",
        description="아이디어 자동생성기 캐릭터를 설명하는 설명글입니다. 이 공간에는 짧은 내용의 캐릭터 설명이 들어갑니다.",
        count=3
    ),
]


# mbti link count
share_list: List[ShowShareCount] = [
    ShowShareCount(type="씨앗방 지박령", count='11'),
    ShowShareCount(type="아이디어 자동생성기", count='22'),
    ShowShareCount(type="고독한 천재개발자", count='33'),
    ShowShareCount(type="기술스택 스펀지밥", count='44'),
    ShowShareCount(type="ㅋㅋ인간 레드불", count='55'),
    ShowShareCount(type="챗봇 커뮤니케이터", count='66'),
    ShowShareCount(type="얼리버드", count='77'),
    ShowShareCount(type="고객 독심술사", count='88'),
    ShowShareCount(type="잔디 개발자", count='99'),
]


@mbti_router.get("/count")
async def get_all_count():
    count = 0
    for i in mbti:
        count += i.count

    return {"detail": count}


@mbti_router.get("/test/rank", response_model=List[ShowTestCount])
async def get_rank():
    count_list: List = []
    for i in mbti:
        count_list.append(i)

    count_list.sort(key=lambda mbti: mbti.count, reverse=True)
    return count_list


@mbti_router.get("/test/count/{type}")
async def get_count_of_mbti(type: str):
    for i in mbti:
        if i.type == type:
            return {"detail": i.count}


# 링크 공유 관련
@mbti_router.post("/share")
async def plus_link_count(
    type: str
):
    for share in share_list:
        if share.type == type:
            share.count += 1
            return {'datail': 'Done'}


@mbti_router.get("/share/{type}")
async def link_count(
    type: str
):
    for share in share_list:
        if share.type == type:
            return {"detail": share.count}


@mbti_router.post("/test/result", response_model=MBTI)
async def mbti_result(choice: Choice):
    return mbti[get_mbti(choice.choices)]
