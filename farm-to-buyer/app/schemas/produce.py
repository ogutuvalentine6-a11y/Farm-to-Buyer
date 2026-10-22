from pydantic import BaseModel


class ProduceCreate(BaseModel):
    farm_id: str
    title: str
    category: str
    description: str | None = None
    price: float
    quantity: float
    unit: str = "kg"
    quality_grade: str | None = None
    location: str | None = None
    image_urls: list[str] = []


class ProduceUpdate(BaseModel):
    title: str | None = None
    price: float | None = None
    quantity: float | None = None
    available: bool | None = None


class ProduceOut(ProduceCreate):
    id: str
    farmer_id: str
    available: bool
