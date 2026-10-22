from datetime import datetime
from beanie import Document, PydanticObjectId


class Product(Document):
    agrovet_id: PydanticObjectId
    name: str
    category: str
    description: str | None = None
    price: float
    stock: float = 0
    unit: str = "unit"
    manufacturer: str | None = None
    expiry_date: datetime | None = None
    regulated: bool = False
    image_urls: list[str] = []
    created_at: datetime = datetime.utcnow
    updated_at: datetime = datetime.utcnow

    class Settings:
        name = "products"
