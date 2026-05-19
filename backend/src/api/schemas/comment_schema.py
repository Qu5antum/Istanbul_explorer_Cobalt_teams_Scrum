from pydantic import BaseModel
from datetime import datetime


class CommentCreate(BaseModel):
    title: str


class CommentUserResponse(BaseModel):
    email: str

    class Config:
        from_attributes = True


class CommentResponse(BaseModel):

    title: str
    created_at: datetime

    user: CommentUserResponse

    class Config:
        from_attributes = True
