from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Extra


class PostResponse(BaseModel):
    """Serializer for Post Response"""

    id: int
    text: str
    date: datetime
    user_id: int
    parent_id: Optional[int]


class PostResponseWithReplies(PostResponse):
    replies: Optional[list['PostResponse']] = None

    class Config:
        orm_mode = True


class PostRequest(BaseModel):
    """Serializer for Post request payload"""

    parent_id: Optional[int]
    text: str

    class Config:
        extra = Extra.allow
        arbitrary_types_allowed = True
