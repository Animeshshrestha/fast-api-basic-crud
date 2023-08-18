import uuid
from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from app import CreatePostSchema, PostResponse,\
UpdatePostSchema, ListPostResponse
from app.crud import post_crud
from app.databases import get_db

router = APIRouter()


def get_posts(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    post_items = post_crud.get_multi(
        db = db,
        skip = skip,
        limit = limit
    )
    return {'status': 'success', 'results': len(post_items), 'posts': post_items}


def create_post(
    *,
    db: Session = Depends(get_db),
    item_in: CreatePostSchema
) -> Any:
    item = post_crud.create_post(
        db = db,
        obj_in = item_in
    )
    return item


def update_post(
    *,
    db: Session = Depends(get_db),
    id: uuid.UUID,
    item_in: UpdatePostSchema
) -> Any:
    post_item_query = post_crud.get(
        db=db, id=id
    )
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    item = post_crud.update(db=db, db_obj=post_item_query, obj_in=item_in)
    return item


def get_post(
    *,
    db: Session = Depends(get_db),
    id: uuid.UUID,
) -> Any:
    item = post_crud.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


def delete_post(
    *,
    db: Session = Depends(get_db),
    id: uuid.UUID,
) -> Any:
    item = post_crud.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    item = post_crud.remove(db=db, id=id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)