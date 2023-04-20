from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session

from .mbti import mbti_list
from database import get_db
from models import DbComment
from schemas import Comment


comment_router = APIRouter(
    tags=["comment"]
)


@comment_router.post('/', status_code=status.HTTP_201_CREATED)
def create(
        request: Comment,
        db: Session = Depends(get_db)
):
    if request.mbti_type not in mbti_list:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail='Type of MBTI is not available.'
        )

    new_comment = DbComment(
        mbti_type=request.mbti_type,
        text=request.text
    )

    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)

    return new_comment


@comment_router.get('/')
def show_all_comment(
        db: Session = Depends(get_db)
):
    return db.query(DbComment).all()
