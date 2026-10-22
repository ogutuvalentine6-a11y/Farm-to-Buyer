from bson import ObjectId
from app.models.agrovet import Agrovet
from app.models.product import Product


async def create_agrovet(owner_id: str, data: dict) -> dict:
    a = Agrovet(owner_id=ObjectId(owner_id), **data)
    await a.insert()
    return _to_out_agrovet(a)


async def list_agrovets() -> list[dict]:
    return [_to_out_agrovet(a) for a in await Agrovet.find_all().to_list()]


async def create_product(data: dict) -> dict:
    data = data.copy()
    data["agrovet_id"] = ObjectId(data["agrovet_id"])
    p = Product(**data)
    await p.insert()
    return _to_out_product(p)


async def search_products(q: str | None = None) -> list[dict]:
    items = await Product.find_all().to_list()
    if q:
        items = [i for i in items if q.lower() in i.name.lower()]
    return [_to_out_product(i) for i in items]


def _to_out_agrovet(a: Agrovet) -> dict:
    return {
        "id": str(a.id), "owner_id": str(a.owner_id), "shop_name": a.shop_name,
        "county": a.county, "sub_county": a.sub_county,
        "licence_number": a.licence_number, "registration_doc_urls": a.registration_doc_urls,
        "verification_status": a.verification_status,
    }


def _to_out_product(p: Product) -> dict:
    return {
        "id": str(p.id), "agrovet_id": str(p.agrovet_id), "name": p.name,
        "category": p.category, "description": p.description, "price": p.price,
        "stock": p.stock, "unit": p.unit, "manufacturer": p.manufacturer,
        "regulated": p.regulated, "image_urls": p.image_urls,
    }
