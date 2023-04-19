from datetime import datetime

from pydantic import BaseModel


class Comment(BaseModel):
    text: str
    time: datetime

    # for documentation
    class Config:
        schema_extra = {
            "example": {
                "text": "밥 먹을 팟 구해요 인스타 아이디 : @git_jisu",
                "time": datetime(2023, 4, 19, 20, 45)
            }
        }
