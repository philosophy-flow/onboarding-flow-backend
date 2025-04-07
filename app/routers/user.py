import os
from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException, Response

from app.services.user import GetUserDep, AddUserDep, UpdateUserDep
from app.schemas.user import UserResponse


load_dotenv(override=True)

router = APIRouter()


@router.get("/get-user/{username}", response_model=UserResponse)
def get_user(user: GetUserDep, response: Response):
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")

    secure_cookie = True if os.getenv("ENV") == "production" else False
    response.set_cookie(
        key="username_token",
        value=user.username,
        httponly=True,
        secure=secure_cookie,
        samesite="lax",
        max_age=86400,
    )

    return user


@router.post("/create-user", response_model=UserResponse)
async def create_user(user: AddUserDep, response: Response):
    if not user:
        raise HTTPException(status_code=400, detail="Unable to create user.")

    secure_cookie = True if os.getenv("ENV") == "production" else False
    response.set_cookie(
        key="username_token",
        value=user.username,
        httponly=True,
        secure=secure_cookie,
        samesite="lax",
        max_age=86400,
    )

    return user


@router.patch("/update-user/{username}", response_model=UserResponse)
async def update_user(user: UpdateUserDep):
    if not user:
        raise HTTPException(status_code=400, detail="Unable to update user.")
    return user


@router.post("/logout-user")
async def delete_user(response: Response):
    response.delete_cookie(
        key="username_token",
        httponly=True,
        secure=False,
        samesite="lax",
    )
