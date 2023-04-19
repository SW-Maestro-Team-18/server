from typing import List

from fastapi import APIRouter

from models import MBTI

mbti_router = APIRouter(
    tags=["mbti"]
)

# 일단 DB를 안쓴다고 가정
mbti: List[MBTI] = []


@mbti_router.get("/count")
async def get_all_count() -> int:
    count = 0
    for i in mbti:
        count += i.count

    return count
