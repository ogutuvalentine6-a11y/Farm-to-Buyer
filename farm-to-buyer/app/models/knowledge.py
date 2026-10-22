from datetime import datetime
from beanie import Document, PydanticObjectId


class Knowledge(Document):
    contributor_id: PydanticObjectId
    title: str
    category: str
    body: str
    sources: list[str] = []
    is_verified: bool = False
    created_at: datetime = datetime.utcnow
    updated_at: datetime = datetime.utcnow

    class Settings:
        name = "knowledge"
