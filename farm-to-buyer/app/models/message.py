from datetime import datetime
from beanie import Document, PydanticObjectId


class Message(Document):
    sender_id: PydanticObjectId
    recipient_id: PydanticObjectId
    body: str
    read: bool = False
    created_at: datetime = datetime.utcnow

    class Settings:
        name = "messages"
