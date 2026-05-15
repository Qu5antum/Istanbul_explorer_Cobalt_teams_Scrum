from pydantic import BaseModel


class CommentCreate(BaseModel):
    title: str