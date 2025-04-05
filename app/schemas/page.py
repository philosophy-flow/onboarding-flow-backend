from typing import List, Optional
from pydantic import BaseModel


class Component(BaseModel):
    component_name: str


class Page(BaseModel):
    page_number: int
    title: Optional[str] = None
    components: List[Component] = []
