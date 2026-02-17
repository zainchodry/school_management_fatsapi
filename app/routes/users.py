from fastapi import status, HTTPException, Depends, APIRouter
from app.database import *
from app.models.user import *
from app.schemas.user import *
from sqlalchemy.orm import Session
from app.utils.jwt_handler import *
from app.models.profile import *

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/")
def create_user(data: UserCreate, db: Session = Depends(get_db)):
    user = User(**data.dict())
    db.add(user)
    db.commit()
    db.refresh(user)

    profile = Profile(user_id=user.id)
    db.add(profile)
    db.commit()
    return user


@router.get("/")
def list_users(db: Session = Depends(get_db)):
    return db.query(User).all()
