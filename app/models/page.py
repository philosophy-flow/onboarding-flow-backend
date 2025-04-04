from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship


class ComponentDB(SQLModel, table=True):
    __tablename__: str = "components"
    component_name: str = Field(primary_key=True)
    page_number: Optional[int] = Field()


class PageDB(SQLModel, table=True):
    __tablename__: str = "pages"
    page_number: int = Field(primary_key=True)
    title: Optional[str] = Field(max_length=50)
    components: List[ComponentDB] = Relationship()
