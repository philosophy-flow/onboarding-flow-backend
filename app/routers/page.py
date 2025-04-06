from fastapi import APIRouter, HTTPException
from typing import List

from app.services.page import GetPagesDep, UpdatePagesDep, UnusedComponentsDep
from app.schemas.page import Page, Component


router = APIRouter()


@router.get("/get-pages", response_model=List[Page])
def get_page(pages: GetPagesDep):
    if not pages:
        raise HTTPException(status_code=500, detail="Unable to retrieve pages.")
    return pages


@router.put("/update-page", response_model=List[Page])
def update_page(updatedPages: UpdatePagesDep):
    if not updatedPages:
        raise HTTPException(status_code=500, detail="Unable to update page.")
    return updatedPages


@router.get("/get-unused-components", response_model=List[Component])
def get_unused_components(components: UnusedComponentsDep):
    return components
