from datetime import datetime
from beanie import Document, PydanticObjectId


class Delivery(Document):
    order_id: PydanticObjectId
    transporter_id: PydanticObjectId | None = None
    pickup_location: str | None = None
    dropoff_location: str | None = None
    status: str = "pending"
    quote: float | None = None
    tracking_notes: str | None = None
    created_at: datetime = datetime.utcnow
    updated_at: datetime = datetime.utcnow

    class Settings:
        name = "deliveries"
