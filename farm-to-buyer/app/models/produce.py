from datetime import datetime
from beanie import Document, PydanticObjectId


class Produce(Document):
    farm_id: PydanticObjectId
    farmer_id: PydanticObjectId
    title: str
    category: str
    description: str | None = None
    price: float
    quantity: float
    unit: str = "kg"
    quality_grade: str | None = None
    location: str | None = None
    available: bool = True
    image_urls: list[str] = []
    created_at: datetime = datetime.utcnow
    updated_at: datetime = datetime.utcnow

    class Settings:
        name = "produce"
