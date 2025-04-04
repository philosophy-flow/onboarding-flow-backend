from typing import Optional
from sqlmodel import select
from passlib.context import CryptContext

from app.models.user import UserDB


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(plain_pw):
    return pwd_context.hash(plain_pw)


def convert_to_schema(model, Schema):
    model_dict = {
        key: value
        for key, value in model.__dict__.items()
        if not key.startswith("_") and key in Schema.__annotations__
    }

    return Schema(**model_dict)


def get_current_user(db, username) -> Optional[UserDB]:
    select_user = select(UserDB).where(UserDB.username == username)
    user: UserDB = db.exec(select_user).first()

    if not user:
        return None

    return user


def save_user(db, user):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
