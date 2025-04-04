from typing import Optional
from datetime import date
from pydantic import BaseModel


class UserRegister(BaseModel):
    username: str
    password: str


class UserResponse(BaseModel):
    username: str
    current_page: int
    about: Optional[str] = None
    dob: Optional[date] = None
    street: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip: Optional[str] = None


class UserUpdate(BaseModel):
    current_page: Optional[int] = None
    about: Optional[str] = None
    dob: Optional[date] = None
    street: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip: Optional[str] = None
