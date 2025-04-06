from typing import Annotated, List
from fastapi import Depends

from app.db.session import SessionDep
from app.schemas.page import Page
from app.utils.page import get_db_page, get_db_pages, get_db_components


def get_pages_service(db: SessionDep):
    pages = get_db_pages(db)
    return sorted(pages, key=lambda p: p.page_number)


def update_page_service(updated_page: Page, db: SessionDep):
    db_page = get_db_page(db, updated_page.page_number)
    if not db_page:
        return None

    db_page.title = updated_page.title

    updated_component_names = [
        component.component_name for component in updated_page.components
    ]

    db_components = get_db_components(db)
    for component in db_components:
        if (
            component.page_number == updated_page.page_number
            and component.component_name not in updated_component_names
        ):
            component.page_number = None
        elif component.component_name in updated_component_names:
            component.page_number = updated_page.page_number

    db.commit()

    pages = get_db_pages(db)
    return sorted(pages, key=lambda p: p.page_number)


# dependencies

GetPagesDep = Annotated[List[Page], Depends(get_pages_service)]
UpdatePagesDep = Annotated[List[Page], Depends(update_page_service)]
