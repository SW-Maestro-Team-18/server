from typing import List

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from models import Comment, MBTI, ShowComment, ShowCount

mbti_router = APIRouter(
    tags=["mbti"]
)

# 일단 DB를 안쓴다고 가정
# mbti: list[MBTI] = [
#     MBTI(
#         type="씨앗방 지박령",
#         summary="쏘마 센터는 내가 지킨다! 씨앗방에 뿌리내린 열혈개발자",
#         description="씨앗방 지박령 캐릭터를 설명하는 설명글입니다. 이 공간에는 짧은 내용의 캐릭터 설명이 들어갑니다.",
#         count=0
#     ),
#     MBTI(
#         type="아이디어 자동생성기",
#         summary="아이디어가 떠오르는 순간, 바로 개발을 시작한다!",
#         description="아이디어 자동생성기 캐릭터를 설명하는 설명글입니다. 이 공간에는 짧은 내용의 캐릭터 설명이 들어갑니다.",
#         count=0
#     )
# ]


mbti: List[ShowCount] = [
    ShowCount(type="씨앗방 지박령", count='1'),
    ShowCount(type="아이디어 자동생성기", count='2'),
    ShowCount(type="고독한 천재개발자", count='3'),
    ShowCount(type="기술스택 스펀지밥", count='4'),
    ShowCount(type="ㅋㅋ인간 레드불", count='5'),
    ShowCount(type="챗봇 커뮤니케이터", count='6'),
    ShowCount(type="얼리버드", count='7'),
    ShowCount(type="고객 독심술사", count='8'),
    ShowCount(type="잔디 개발자", count='9'),
]


# going to be sorted by timestamp
comments: List[Comment] = [
    Comment(type="씨앗방 지박령", text="이 분들 씻고 다니시는 거죠?"),
    Comment(type="씨앗방 지박령", text="냄새나요"),
    Comment(type="씨앗방 지박령", text="꿀단지라도 묻어뒀나봐요"),
    Comment(type="씨앗방 지박령", text="저예요 저!"),
]


@mbti_router.get("/count")
async def get_all_count():
    count = 0
    for i in mbti:
        count += i.count

    return {"detail": count}


@mbti_router.get("/test/rank", response_model=List[ShowCount])
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


# @mbti_router.get("/count")
# async def get_all_count() -> int:
#     count = int
#     for i in mbti:
#         count.value += i.count
#
#     return count


#
# @mbti_router.get("/count_each")
# async def get_all_count() -> int:
#     count_list: List = []
#     for i in mbti:
#         count_list.append(i.count)
#
#     return count_list


# 커뮤니티에 넣을 comment
@mbti_router.get("/get_comment/{type}_{num_of_comments}", response_model=List[ShowComment])
async def get_comment(type: str, num_of_comments: int):
    comment_list = []
    for comment in comments:
        if comment.type == type:
            comment_list.append(comment)
        
        if len(comment_list) >= num_of_comments:
            return comment_list

    return comment_list
