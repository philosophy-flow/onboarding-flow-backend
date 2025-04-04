import os
from dotenv import load_dotenv
from typing import Annotated
from fastapi import Depends
from sqlmodel import Session, create_engine


load_dotenv(override=True)

DB_URL = os.getenv("DB_URL", "")
engine = create_engine(DB_URL)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
