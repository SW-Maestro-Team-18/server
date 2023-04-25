import uvicorn
from fastapi import FastAPI

from database import Base, engine
from routers import comment_router, mbti_router

description = """
미니 프로젝트 🚀

## MBTI

 - 모든 유형의 검사횟수를 조회하거나 각 유형의 검사횟수 조회  
 - 검사횟수 결과 mbti count에 따른 순위 반환  
 - 유형별 공유 횟수 조회  
 - 선택지에 따른 MBTI 알고리즘 결과 출력  
 
 ### MBTI table
 
<img src='https://user-images.githubusercontent.com/103489171/234359816-42d46360-a9f0-450e-bd42-e80f15ae37a2.png'>

## Comment

 - 유형별 댓글 조회, 최대 출력 개수(num of comment)
 - 모든 댓글 조회, 최대 출력 개수(num of comment)
 - 댓글 생성 및 삭제(삭제는 입력 시 기입했던 password를 통해 확인)
"""

app = FastAPI(
    description=description
)
 

app.include_router(router=mbti_router)
app.include_router(router=comment_router)


Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
