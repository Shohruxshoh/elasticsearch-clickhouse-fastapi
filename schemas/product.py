from pydantic import BaseModel
from typing import Optional


class ProductCreate(BaseModel):
    title: str
    description: Optional[str] = None
    price: float
    category_id: Optional[int] = None


class ProductResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    price: float
    is_active: bool

    model_config = {
        "from_attributes": True
    }
