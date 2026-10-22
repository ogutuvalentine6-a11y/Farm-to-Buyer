from pydantic import BaseModel


class DeliveryCreate(BaseModel):
    order_id: str
    pickup_location: str | None = None
    dropoff_location: str | None = None
    quote: float | None = None


class DeliveryUpdate(BaseModel):
    transporter_id: str | None = None
    status: str | None = None
    tracking_notes: str | None = None


class DeliveryOut(DeliveryCreate):
    id: str
    status: str
