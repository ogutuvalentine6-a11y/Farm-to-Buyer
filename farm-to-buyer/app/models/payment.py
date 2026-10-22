from datetime import datetime
from beanie import Document, PydanticObjectId


class Payment(Document):
    order_id: PydanticObjectId
    payer_id: PydanticObjectId
    amount: float
    method: str = "mpesa"
    status: str = "pending"
    provider_ref: str | None = None
    receipt_url: str | None = None
    created_at: datetime = datetime.utcnow

    class Settings:
        name = "payments"
