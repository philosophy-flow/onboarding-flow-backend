import uuid
from datetime import date
from typing import Optional
from sqlmodel import Field, SQLModel


class UserDB(SQLModel, table=True):
    __tablename__: str = "users"
    user_id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)
    current_page: int = Field(default=1)
    username: str = Field(unique=True, max_length=50, nullable=False)
    hashed_pw: str = Field(max_length=255, nullable=False)
    about: Optional[str] = Field()
    dob: Optional[date] = Field()
    street: Optional[str] = Field(max_length=50)
    city: Optional[str] = Field(max_length=50)
    state: Optional[str] = Field(max_length=50)
    zip: Optional[int] = Field(max_digits=5)
