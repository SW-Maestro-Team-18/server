from typing import List

from fastapi import APIRouter, HTTPException, status

from models import Comment, CommentCreate, CommentDelete, ShowComment


comment_router = APIRouter(
    prefix='/comment',
    tags=["Comment"]
)


# going to be sorted by timestamp
comments: List[Comment] = [
    Comment(id=1, type="씨앗방 지박령", text="이 분들 씻고 다니시는 거죠?"),
    Comment(id=2, type="씨앗방 지박령", text="냄새나요"),
    Comment(id=3, type="씨앗방 지박령", text="꿀단지라도 묻어뒀나봐요"),
    Comment(id=4, type="씨앗방 지박령", text="저예요 저!"),
]


# 커뮤니티에 넣을 comment
@comment_router.get("/{type}/{num_of_comments}", response_model=List[ShowComment])
async def get_comment_of_type_with_limit_num(type: str, num_of_comments: int):
    comment_list = []
    for comment in comments:
        if comment.type == type:
            comment_list.append(comment)
        
        if len(comment_list) >= num_of_comments:
            return comment_list

    return comment_list


@comment_router.get("/all/{num_of_comments}", response_model=List[ShowComment])
async def get_all_comment_with_limit_num(num_of_comments: int):
    return comments[:num_of_comments]


@comment_router.post('/new', response_model=ShowComment, status_code=status.HTTP_201_CREATED)
async def create_comment(
    request: CommentCreate
):
    new_comment = CommentCreate(
        id = request.id,
        type = request.type,
        text = request.text,
        password = request.password
    )
    
    comments.append(new_comment)
    
    return new_comment


@comment_router.post('/delete', status_code=status.HTTP_204_NO_CONTENT)
async def delete_comment_by_id(
    request: CommentDelete
):
    for idx, comment in enumerate(comments):
        if comment.id == request.id:
            if comment.password != request.password:
                raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Password is wrong")
            
            comments.pop(idx)
            
            return {'detail': 'Done'}
        