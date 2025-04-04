from fastapi import APIRouter


router = APIRouter()


@router.get("/get-user")
def get_user():
    # query db with user id
    # return user
    return None


@router.post("/add-user")
async def add_user():
    # query db with provided username
    # verify username does not already exist

    # hash password
    # add user to db (username, hashed_pw, current_page)
    # return success message
    return None


@router.patch("/edit-user")
async def edit_user():
    # query db with user id
    # make patch query with updated info
    # return updated user
    return None
