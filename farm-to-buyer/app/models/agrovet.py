from datetime import datetime
from beanie import Document, PydanticObjectId


class Agrovet(Document):
    owner_id: PydanticObjectId
    shop_name: str
    county: str
    sub_county: str | None = None
    licence_number: str | None = None
    registration_doc_urls: list[str] = []
    verification_status: str = "pending"
    verification_notes: str | None = None
    created_at: datetime = datetime.utcnow

    class Settings:
        name = "agrovets"
