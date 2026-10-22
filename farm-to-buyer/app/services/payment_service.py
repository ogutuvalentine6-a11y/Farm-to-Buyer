from bson import ObjectId
from app.models.payment import Payment


async def initiate(payer_id: str, data: dict) -> dict:
    p = Payment(
        payer_id=ObjectId(payer_id),
        order_id=ObjectId(data["order_id"]),
        amount=data["amount"],
        method=data.get("method", "mpesa"),
    )
    await p.insert()
    return _to_out(p)


async def handle_mpesa_callback(body: dict) -> dict:
    return {"received": True, "body": body}


def _to_out(p: Payment) -> dict:
    return {
        "id": str(p.id), "order_id": str(p.order_id), "payer_id": str(p.payer_id),
        "amount": p.amount, "method": p.method, "status": p.status,
        "provider_ref": p.provider_ref,
    }
