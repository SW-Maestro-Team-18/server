from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from database import get_db
from database.database import DbMBTI
from models import *
from utils import get_mbti

mbti_router = APIRouter()

# 일단 DB를 안쓴다고 가정
mbti: List[MBTI] = [
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


# 링크 공유 관련
@mbti_router.post("/share", status_code=status.HTTP_204_NO_CONTENT, tags=['share'])
async def plus_share_count(
    type_id: int,
    db: Session = Depends(get_db)
):
    db.query(DbMBTI).filter(DbMBTI.id == type_id).update(
                values = {
                    "type": DbMBTI.type,
                    "summary": DbMBTI.summary,
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
            "summary": DbMBTI.summary,
            "description": DbMBTI.description,
            "testcount": DbMBTI.testcount+ 1,
            "sharecount": DbMBTI.sharecount
        }
    )
    db.commit()
    
    return query.first()


@mbti_router.post('/mbti/create', response_model=ShowMBTI, status_code=status.HTTP_201_CREATED, tags=['root'])
async def create_mbti(
    request: MBTI,
    db: Session = Depends(get_db)
):
    new_mbti = DbMBTI(
        type = request.type,
        summary = request.summary,
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
