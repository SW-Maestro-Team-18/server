from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from passlib.context import CryptContext

from database.hashing import Hash
from database.connection import get_db
from database.database import DbComment
from models import CommentCreate, CommentDelete, ShowComment


comment_router = APIRouter(
    prefix='/comment',
    tags=["Comment"]
)


@comment_router.post('/new', response_model=ShowComment, status_code=status.HTTP_201_CREATED)
async def create_comment(
    request: CommentCreate,
    db: Session = Depends(get_db)
):
    hashed_password = Hash.bcrypt(request.password)
    
    new_comment = DbComment(
        type_id = request.type_id,
        text = request.text,
        password = hashed_password
    )
    
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    
    return new_comment


@comment_router.delete('/delete', status_code=status.HTTP_204_NO_CONTENT)
async def delete_comment_by_id(
    request: CommentDelete,
    db: Session = Depends(get_db)
):
    q = db.query(DbComment).filter(DbComment.id == request.id)
    if not q.first():
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail='No requested comment.')
    
    hashed = q.first().password
    if not Hash.verify(request.password, hashed):
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail='Wrong password.')
    
    q.delete()
    db.commit()


@comment_router.get('/all', response_model=List[ShowComment])
async def get_comment_all_with_limit_num(
    num_of_comments: int = 5,
    db: Session = Depends(get_db)
):
    return db.query(DbComment).order_by(DbComment.datetime.desc()).all()[:num_of_comments]


@comment_router.get("/{type_id}", response_model=List[ShowComment])
async def get_comment_of_type_with_limit_num(
    type_id: int, 
    num_of_comments: int = 3,
    db: Session = Depends(get_db)
):
    return db.query(DbComment).filter(DbComment.type_id == type_id) \
        .order_by(DbComment.datetime.desc()).all()[:num_of_comments]