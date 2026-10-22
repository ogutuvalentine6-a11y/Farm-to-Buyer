from datetime import datetime
from beanie import Document, PydanticObjectId


class Farm(Document):
    owner_id: PydanticObjectId
    name: str
    county: str
    sub_county: str | None = None
    size_acres: float | None = None
    crops: list[str] = []
    capacity: str | None = None
    harvest_schedule: str | None = None
    evidence_urls: list[str] = []
    verification_status: str = "pending"
    verification_notes: str | None = None
    created_at: datetime = datetime.utcnow

    class Settings:
        name = "farms"
