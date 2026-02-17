from pydantic import BaseModel
from typing import Optional

class ProfileBase(BaseModel):
    full_name: str | None = None
    phone: str | None = None
    address: str | None = None

class ProfileOut(ProfileBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True

class ProfileUpdateSchema(BaseModel):
    full_name: Optional[str]
    phone: Optional[str]
    address: Optional[str]
