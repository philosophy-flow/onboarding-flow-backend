from typing import Optional, Annotated
from fastapi import Depends

from app.db.session import SessionDep
from app.models.user import UserDB
from app.schemas.user import UserResponse, UserRegister, UserUpdate
from app.util import convert_to_schema, get_current_user, hash_password, save_user


def get_user_service(username: str, db: SessionDep):
    db_user: Optional[UserDB] = get_current_user(db, username)
    if not db_user:
        return None

    return convert_to_schema(db_user, UserResponse)


def create_user_service(user_info: UserRegister, db: SessionDep):
    existing_user: Optional[UserDB] = get_current_user(db, user_info.username)
    if existing_user:
        return None

    db_user = UserDB(
        username=user_info.username, hashed_pw=hash_password(user_info.password)
    )
    save_user(db, db_user)

    return convert_to_schema(db_user, UserResponse)


def update_user_service(
    username: str,
    update_data: UserUpdate,
    db: SessionDep,
):
    db_user: Optional[UserDB] = get_current_user(db, username)
    if not db_user:
        return None

    user_attributes = update_data.model_dump(exclude_unset=True)
    for attribute, value in user_attributes.items():
        if hasattr(db_user, attribute):
            setattr(db_user, attribute, value)
    save_user(db, db_user)

    return convert_to_schema(db_user, UserResponse)


# dependencies
GetUserDep = Annotated[Optional[UserResponse], Depends(get_user_service)]
AddUserDep = Annotated[Optional[UserResponse], Depends(create_user_service)]
UpdateUserDep = Annotated[Optional[UserResponse], Depends(update_user_service)]
