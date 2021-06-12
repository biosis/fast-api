from typing import List

from fastapi import APIRouter, Response, status, Depends
from sqlalchemy.orm import Session
from ..repository import blog
from .. import database, oath2, schemas

router = APIRouter(
    prefix='/blog',
    tags=['blogs']
)
get_db = database.get_db


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oath2.get_current_user)):
    return blog.get_all(db)


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def show(id, response: Response, db: Session = Depends(get_db), current_user: schemas.User = Depends(oath2.get_current_user)):
    return blog.show(id, db)


@router.post("", status_code=status.HTTP_201_CREATED, response_model=schemas.ShowBlog)
def create(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oath2.get_current_user)):
    return blog.save(request, db)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oath2.get_current_user)):
    return blog.update(id, request, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(oath2.get_current_user)):
    return blog.destroy(id, db)

