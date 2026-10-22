from bson import ObjectId
from app.models.farm import Farm


async def create_farm(owner_id: str, data: dict) -> dict:
    farm = Farm(owner_id=ObjectId(owner_id), **data)
    await farm.insert()
    return _to_out(farm)


async def list_farms() -> list[dict]:
    return [_to_out(f) for f in await Farm.find_all().to_list()]


async def get_farm(farm_id: str) -> dict | None:
    f = await Farm.get(farm_id)
    return _to_out(f) if f else None


def _to_out(f: Farm) -> dict:
    return {
        "id": str(f.id), "owner_id": str(f.owner_id), "name": f.name,
        "county": f.county, "sub_county": f.sub_county, "size_acres": f.size_acres,
        "crops": f.crops, "capacity": f.capacity, "harvest_schedule": f.harvest_schedule,
        "evidence_urls": f.evidence_urls, "verification_status": f.verification_status,
    }
