from sqlmodel import select
from app.models.page import PageDB, ComponentDB


def get_db_pages(db):
    select_pages = select(PageDB)
    return db.exec(select_pages).all()


def get_db_page(db, page_number):
    select_db_page = select(PageDB).where(PageDB.page_number == page_number)
    return db.exec(select_db_page).first()


def get_db_components(db):
    select_db_components = select(ComponentDB)
    return db.exec(select_db_components).all()
