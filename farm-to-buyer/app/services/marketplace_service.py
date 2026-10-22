from bson import ObjectId
from app.models.produce import Produce


async def create_produce(farmer_id: str, data: dict) -> dict:
    data = data.copy()
    data["farm_id"] = ObjectId(data["farm_id"])
    data["farmer_id"] = ObjectId(farmer_id)
    p = Produce(**data)
    await p.insert()
    return _to_out(p)


async def search_produce(q: str | None = None) -> list[dict]:
    items = await Produce.find(Produce.available == True).to_list()  # noqa: E712
    if q:
        items = [i for i in items if q.lower() in i.title.lower()]
    return [_to_out(i) for i in items]


def _to_out(p: Produce) -> dict:
    return {
        "id": str(p.id), "farm_id": str(p.farm_id), "farmer_id": str(p.farmer_id),
        "title": p.title, "category": p.category, "description": p.description,
        "price": p.price, "quantity": p.quantity, "unit": p.unit,
        "quality_grade": p.quality_grade, "location": p.location,
        "available": p.available, "image_urls": p.image_urls,
    }
