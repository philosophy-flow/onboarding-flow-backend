from datetime import date
from typing import Optional
from sqlmodel import Field, SQLModel


class UserDB(SQLModel, table=True):
    __table_args__ = {"schema": "onboarding-flow"}
    __tablename__: str = "users"
    username: str = Field(primary_key=True, max_length=50)
    current_page: int = Field(default=1)
    hashed_pw: str = Field(max_length=255, nullable=False)
    about: Optional[str] = Field(default=None)
    dob: Optional[date] = Field(default=None)
    street: Optional[str] = Field(default=None, max_length=50)
    city: Optional[str] = Field(default=None, max_length=50)
    state: Optional[str] = Field(default=None, max_length=50)
    zip: Optional[str] = Field(default=None)
