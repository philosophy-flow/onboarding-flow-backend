from sqlmodel import select
from app.models.page import PageDB, ComponentDB


def get_db_pages(db):
    select_pages = select(PageDB)
    return db.exec(select_pages).all()


def get_db_page(db, page_number):
    select_db_page = select(PageDB).where(PageDB.page_number == page_number)
    return db.exec(select_db_page).first()


def get_db_components(db, unused=False):
    if not unused:
        select_db_components = select(ComponentDB)
    else:
        select_db_components = select(ComponentDB).where(
            ComponentDB.page_number == None
        )
    return db.exec(select_db_components).all()
