from datetime import datetime
from typing import List
import uuid
from pydantic import BaseModel, ConfigDict

class PostBaseSchema(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    title: str
    content: str
    category: str
    image: str


class CreatePostSchema(PostBaseSchema):

    pass


class PostResponse(PostBaseSchema):

    id: uuid.UUID
    created_at: datetime
    updated_at: datetime


class UpdatePostSchema(PostBaseSchema):

    pass


class ListPostResponse(BaseModel):
    
    status: str
    results: int
    posts: List[PostResponse]