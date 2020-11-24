from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.utils import get_db
from . import service
from .schemas import PostBase, PostList
from typing import List


router = APIRouter()


@router.get('/', response_model=List[PostList])
def post_list(db: Session = Depends(get_db)):
    posts = service.get_post_list(db)
    return posts


@router.post('/')
def post_create(item: PostBase, db: Session = Depends(get_db)):
    return service.create_post(db=db, item=item)
