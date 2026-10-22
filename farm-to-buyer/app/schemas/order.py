from pydantic import BaseModel


class OrderItemIn(BaseModel):
    item_id: str
    kind: str
    quantity: float
    unit_price: float


class OrderCreate(BaseModel):
    seller_id: str
    items: list[OrderItemIn]
    delivery_address: str | None = None
    notes: str | None = None


class OrderOut(OrderCreate):
    id: str
    buyer_id: str
    total: float
    status: str
