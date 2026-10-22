from pydantic import BaseModel


class ProductCreate(BaseModel):
    agrovet_id: str
    name: str
    category: str
    description: str | None = None
    price: float
    stock: float = 0
    unit: str = "unit"
    manufacturer: str | None = None
    regulated: bool = False
    image_urls: list[str] = []


class ProductOut(ProductCreate):
    id: str
