from app.models.farm import Farm
from app.models.agrovet import Agrovet


async def verify_farm(farm_id: str, status: str, notes: str = "") -> dict:
    farm = await Farm.get(farm_id)
    if not farm:
        return {"error": "not found"}
    farm.verification_status = status
    farm.verification_notes = notes
    await farm.save()
    return {"id": farm_id, "status": status}


async def verify_agrovet(agrovet_id: str, status: str, notes: str = "") -> dict:
    a = await Agrovet.get(agrovet_id)
    if not a:
        return {"error": "not found"}
    a.verification_status = status
    a.verification_notes = notes
    await a.save()
    return {"id": agrovet_id, "status": status}
