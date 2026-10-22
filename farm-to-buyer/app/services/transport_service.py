from bson import ObjectId
from app.models.delivery import Delivery


async def create_delivery(data: dict) -> dict:
    payload = {k: v for k, v in data.items() if k != "order_id"}
    d = Delivery(order_id=ObjectId(data["order_id"]), **payload)
    await d.insert()
    return _to_out(d)


async def update_delivery(delivery_id: str, patch: dict) -> dict | None:
    d = await Delivery.get(delivery_id)
    if not d:
        return None
    for k, v in patch.items():
        setattr(d, k, v)
    await d.save()
    return _to_out(d)


def _to_out(d: Delivery) -> dict:
    return {
        "id": str(d.id), "order_id": str(d.order_id),
        "transporter_id": str(d.transporter_id) if d.transporter_id else None,
        "pickup_location": d.pickup_location, "dropoff_location": d.dropoff_location,
        "status": d.status, "quote": d.quote, "tracking_notes": d.tracking_notes,
    }
