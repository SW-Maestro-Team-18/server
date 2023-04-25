import uvicorn
from fastapi import FastAPI

from database import Base, engine
from routers import comment_router, mbti_router

description = """
미니 프로젝트 🚀

노션 명세서를 참고하였습니다.  
_<a href="https://www.notion.so/d665a407d3c64728857bbcda2641553f?pvs=4"> 간이 명세서 노션 링크</a>_

## MBTI

 - 모든 유형의 검사횟수를 조회하거나 각 유형의 검사횟수 조회  
 - 검사횟수 결과 mbti count에 따른 순위 반환  
 - 유형별 공유 횟수 조회  
 - 선택지에 따른 MBTI 알고리즘 결과 출력  
 
 ### MBTI table
 
|id|유형|
|:---:|:---:|
|1|씨앗방 지박령|
|2|아이디어 자동생성기|
|3|고독한 천재개발자|
|4|기술스택 스펀지밥|
|5|ㅋㅋ인간 레드불|
|6|챗봇 커뮤니케이터|
|7|얼리버드|
|8|고객 독심술사|
|9|잔디 개발자|

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
