from fastapi import APIRouter, HTTPException

from app.services.user import GetUserDep, AddUserDep, UpdateUserDep
from app.schemas.user import UserResponse


router = APIRouter()


@router.get("/get-user/{username}", response_model=UserResponse)
def get_user(user: GetUserDep):
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    return user


@router.post("/create-user", response_model=UserResponse)
async def create_user(user: AddUserDep):
    if not user:
        raise HTTPException(status_code=400, detail="Unable to create user.")
    return user


@router.patch("/update-user/{username}", response_model=UserResponse)
async def update_user(user: UpdateUserDep):
    if not user:
        raise HTTPException(status_code=400, detail="Unable to update user.")
    return user
