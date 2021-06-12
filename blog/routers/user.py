from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from ..repository import user
from .. import database, schemas

router = APIRouter(
    prefix='/user',
    tags=['users']
)
get_db = database.get_db


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.save(request, db)


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.get(id, db)
