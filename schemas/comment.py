from pydantic import BaseModel


class Comment(BaseModel):
    mbti_type: str
    text: str

    # for documentation
    class Config:
        schema_extra = {
            "example": {
                "mbti_type" : "씨앗방 지박령",
                "text" : "저랑 너무 잘 맞아요!"
            }
        }
