from pydantic import BaseModel


class PaymentCreate(BaseModel):
    order_id: str
    amount: float
    method: str = "mpesa"


class PaymentOut(PaymentCreate):
    id: str
    payer_id: str
    status: str
    provider_ref: str | None = None
