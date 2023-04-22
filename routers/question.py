from typing import List

from fastapi import APIRouter, HTTPException

from models import Question


question_router = APIRouter(
    tags=['question']
)


question: List[Question] = [
    Question(id=1, text='집보다 씨앗방이 편하신가요?'),
    Question(id=2, text='세 끼니를 모두 센터 주변에서 해결하나요?'),
]


@question_router.get('/test/question/{id}')
async def get_question(
    id:int
):
    for q in question:
        if q.id == id:
            return q
        