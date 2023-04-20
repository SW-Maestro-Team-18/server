from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import DbMBTI
from schemas import MBTI


router = APIRouter(
    tags=["mbti"]
)

mbti: list[str] = []


@router.get("/count")
async def get_all_count() -> int:
    count = 0
    for i in mbti:
        count += i.count

    return count




mbti_list = [
    "씨앗방 지박령",
    "아이디어 자동생성기",
    "고독한 천재개발자",
    "파워 기술블로거",
    "기술스택 스펀지밥",
    "인간 레드불",
    "챗봇 커뮤니케이터",
    "얼리버드",
    "고객 독심술사",
    "잔디 개발자"
]
@router.post('/', status_code=status.HTTP_201_CREATED)
def create(
        request: MBTI,
        db: Session = Depends(get_db)
):
    if request.type not in mbti_list:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail='Type of MBTI is not available.'
        )

    new_mbti = DbMBTI(
        type=request.type,
        summary=request.summary,
        description=request.description
    )

    db.add(new_mbti)
    db.commit()
    db.refresh(new_mbti)

    return new_mbti
