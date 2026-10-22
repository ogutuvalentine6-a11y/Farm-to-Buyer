from pydantic import BaseModel


class FarmCreate(BaseModel):
    name: str
    county: str
    sub_county: str | None = None
    size_acres: float | None = None
    crops: list[str] = []
    capacity: str | None = None
    harvest_schedule: str | None = None
    evidence_urls: list[str] = []


class FarmUpdate(BaseModel):
    name: str | None = None
    county: str | None = None
    crops: list[str] | None = None
    capacity: str | None = None


class FarmOut(FarmCreate):
    id: str
    owner_id: str
    verification_status: str
