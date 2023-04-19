import uvicorn
from fastapi import FastAPI
from routers import mbti_router

app = FastAPI()

app.include_router(prefix="/mbti", router=mbti_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)