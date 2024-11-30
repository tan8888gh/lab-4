# A model class for Product items
# See https://docs.pydantic.dev/latest/concepts/models/

from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    _id: int
    category_id: int
    title: str
    description: str
    price: float
    stock: int
    thumbnail: str=""
