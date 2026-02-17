from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.profile import ProfileUpdateSchema
from app.utils.jwt_handler import get_current_user
from app.models.profile import *

router = APIRouter(prefix="/profiles", tags=["Profiles"])


@router.get("/me")
def get_my_profile(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return db.query(Profile).filter(
        Profile.user_id == current_user.id
    ).first()


@router.put("/me")
def update_profile(
    data: ProfileUpdateSchema,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    profile = db.query(Profile).filter(
        Profile.user_id == current_user.id
    ).first()

    for key, value in data.dict(exclude_unset=True).items():
        setattr(profile, key, value)

    db.commit()
    return {"message": "Profile updated successfully"}
