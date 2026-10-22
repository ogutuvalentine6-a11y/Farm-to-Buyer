from datetime import datetime
from beanie import Document, PydanticObjectId


class Notification(Document):
    user_id: PydanticObjectId
    channel: str = "in_app"
    title: str
    body: str
    read: bool = False
    created_at: datetime = datetime.utcnow

    class Settings:
        name = "notifications"
