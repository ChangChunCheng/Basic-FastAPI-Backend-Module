import uuid
from pydantic import BaseModel, Field, EmailStr
from uuid import UUID, uuid4
from datetime import datetime


class UserBase(BaseModel):
    id: UUID
    account: str


class UserCreate(UserBase):
    password: str
    name: str

    class Config:
        orm_mode: bool = True


class User(UserBase):
    name: str
    disable: bool
    password: str
    createat: datetime
    updateat: datetime

    class Config:
        orm_mode: bool = True


class UserDelete(UserBase):
    class Config:
        orm_mode: bool = True
