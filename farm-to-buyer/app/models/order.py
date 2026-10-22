from datetime import datetime
from enum import Enum
from beanie import Document, PydanticObjectId


class OrderStatus(str, Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    PAID = "paid"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"


class Order(Document):
    buyer_id: PydanticObjectId
    seller_id: PydanticObjectId
    items: list[dict] = []
    total: float = 0.0
    status: OrderStatus = OrderStatus.PENDING
    delivery_address: str | None = None
    notes: str | None = None
    created_at: datetime = datetime.utcnow
    updated_at: datetime = datetime.utcnow

    class Settings:
        name = "orders"
