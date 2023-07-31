from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app import Post, CreatePostSchema, UpdatePostSchema


class CRUDPost(CRUDBase[Post, CreatePostSchema, UpdatePostSchema]):
    def create_post(
        self, db: Session, *, obj_in: CreatePostSchema
    ) -> Post:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_owner(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[Post]:
        return (
            db.query(self.model)
            .offset(skip)
            .limit(limit)
            .all()
        )


post_crud = CRUDPost(Post)