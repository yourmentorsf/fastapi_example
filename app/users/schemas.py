from pydantic import BaseModel, Field
from typing import Optional


class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    password: str = Field(json_schema_extra={"example": "Password123!"})


class UserUpdate(UserBase):
    email: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = Field(None, json_schema_extra={"example": "Password123!"})


class UserInDBBase(UserBase):
    id: Optional[int] = None


class User(UserInDBBase):
    pass
