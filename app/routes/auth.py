from fastapi import status, HTTPException, Depends, APIRouter
from app.database import *
from app.models.user import *
from app.schemas.user import *
from sqlalchemy.orm import Session
from app.utils.jwt_handler import *
from app.models.profile import *

router = APIRouter()

@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email Already Registered")

    user_data = user.dict()
    user_data["password"] = hash_password(user_data["password"])

    new_user = User(**user_data)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    profile = Profile(user_id=new_user.id)
    db.add(profile)
    db.commit()

    return new_user
@router.post("/login", response_model=Token)
def login(data: LoginCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data.email).first()
    if not user or not verify_password(data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"access_token": create_access_token({"id": user.id, "role": user.role}), "token_type":"bearer"}

@router.post("/change-password")
def change_password(data: ChangePasswordSchema,
                    db: Session = Depends(get_db),
                    current_user=Depends(get_current_user)):
    if not verify_password(data.old_password, current_user.password):
        raise HTTPException(status_code=400, detail="Wrong password")
    current_user.password = hash_password(data.new_password)
    db.commit()
    return {"msg": "Password changed successfully"}

@router.post("/forgot-password")
def forgot_password(data: ForgotPasswordSchema, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    token = create_access_token({"id": user.id})
    return {"reset_token": token}


@router.post("/reset-password")
def reset_password(data: ResetPasswordSchema, db: Session = Depends(get_db)):
    user = verify_token(data.token, db)
    user.password = hash_password(data.new_password)
    db.commit()
    return {"msg": "Password reset successful"}