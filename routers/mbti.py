from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from database import get_db
from database.database import DbMBTI
from models import *
from utils import get_mbti

mbti_router = APIRouter()


@mbti_router.get("/count", tags=['count'])
async def get_all_testcount_sum(db: Session = Depends(get_db)):
    return {'detail': db.query(func.sum(DbMBTI.testcount)).first()[0]}


@mbti_router.get("/test/rank", response_model=List[ShowTestCount], tags=['count'])
async def get_rank_of_mbti(
    db: Session = Depends(get_db)
):  
    return db.query(DbMBTI).order_by(DbMBTI.testcount.desc()).all()


@mbti_router.get("/test/count/{type_id}", response_model=ShowTestCount, tags=['count'])
async def get_testcount_of_mbti(
    type_id: int,
    db: Session = Depends(get_db)
):
    return db.query(DbMBTI).filter(DbMBTI.id == type_id).first()


@mbti_router.post("/test/result", response_model=ShowMBTI, status_code=status.HTTP_201_CREATED, tags=['mbti'])
async def mbti_result(
    request: Choice,
    db: Session = Depends(get_db)
):
    type_id = get_mbti(request.choices)
    query = db.query(DbMBTI).filter(DbMBTI.id == type_id)
    
    query.update(
        values = {
            "type": DbMBTI.type,
            "description": DbMBTI.description,
            "testcount": DbMBTI.testcount+ 1,
            "sharecount": DbMBTI.sharecount
        }
    )
    db.commit()
    
    return query.first()


# 링크 공유 관련
@mbti_router.put("/share", status_code=status.HTTP_204_NO_CONTENT, tags=['share'])
async def plus_share_count(
    type_id: int,
    db: Session = Depends(get_db)
):
    db.query(DbMBTI).filter(DbMBTI.id == type_id).update(
                values = {
                    "type": DbMBTI.type,
                    "description": DbMBTI.description,
                    "testcount": DbMBTI.testcount,
                    "sharecount": DbMBTI.sharecount + 1
                }
    )
    db.commit()
    
    return 


@mbti_router.get("/share/{type}", response_model=ShowShareCount, tags=['share'])
async def get_sharecount(
    type_id: int,
    db: Session = Depends(get_db)
):
    return db.query(DbMBTI).filter(DbMBTI.id == type_id).first()


@mbti_router.post('/mbti/create', response_model=ShowMBTI, status_code=status.HTTP_201_CREATED, tags=['Staff Only'])
async def create_mbti(
    request: MBTI,
    db: Session = Depends(get_db)
):
    new_mbti = DbMBTI(
        type = request.type,
        description = request.description
    )
    
    db.add(new_mbti)
    db.commit()
    db.refresh(new_mbti)
    
    return new_mbti


@mbti_router.get('/mbti', response_model=List[ShowMBTI], tags=['mbti'])
async def show_all_mbti(
    db: Session = Depends(get_db)
):
    return db.query(DbMBTI).all()
