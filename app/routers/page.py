from fastapi import APIRouter


router = APIRouter()


@router.put("/update-page")
def update_page():
    # query db with page number to get row
    # use body payload to repopulate entire row
    return None
