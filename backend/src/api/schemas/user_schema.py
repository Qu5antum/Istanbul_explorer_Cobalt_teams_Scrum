from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime

from src.database.models import UserRole


class UserCreate(BaseModel):
    email: EmailStr
    phone_number: str
    password: str
    role: UserRole


class UserOut(UserCreate):
    id: UUID
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True
