from fastapi import APIRouter, HTTPException, Response

from app.services.user import GetUserDep, AddUserDep, UpdateUserDep
from app.schemas.user import UserResponse


router = APIRouter()


@router.get("/get-user/{username}", response_model=UserResponse)
def get_user(user: GetUserDep, response: Response):
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")

    response.set_cookie(
        key="username_token",
        value=user.username,
        httponly=True,
        secure=False,
        samesite="lax",
        max_age=86400,
    )

    return user


@router.post("/create-user", response_model=UserResponse)
async def create_user(user: AddUserDep, response: Response):
    if not user:
        raise HTTPException(status_code=400, detail="Unable to create user.")

    response.set_cookie(
        key="username_token",
        value=user.username,
        httponly=True,
        secure=False,
        samesite="lax",
        max_age=86400,
    )

    return user


@router.patch("/update-user/{username}", response_model=UserResponse)
async def update_user(user: UpdateUserDep):
    if not user:
        raise HTTPException(status_code=400, detail="Unable to update user.")
    return user
