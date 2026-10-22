from bson import ObjectId
from app.models.order import Order


async def create_order(buyer_id: str, data: dict) -> dict:
    items = data["items"]
    total = sum(i["quantity"] * i["unit_price"] for i in items)
    order = Order(
        buyer_id=ObjectId(buyer_id),
        seller_id=ObjectId(data["seller_id"]),
        items=items,
        total=total,
        delivery_address=data.get("delivery_address"),
        notes=data.get("notes"),
    )
    await order.insert()
    return _to_out(order)


async def list_user_orders(user_id: str) -> list[dict]:
    uid = ObjectId(user_id)
    items = await Order.find({"$or": [{"buyer_id": uid}, {"seller_id": uid}]}).to_list()
    return [_to_out(o) for o in items]


async def update_status(order_id: str, status: str) -> dict | None:
    o = await Order.get(order_id)
    if not o:
        return None
    o.status = status
    await o.save()
    return _to_out(o)


def _to_out(o: Order) -> dict:
    return {
        "id": str(o.id), "buyer_id": str(o.buyer_id), "seller_id": str(o.seller_id),
        "items": o.items, "total": o.total,
        "status": o.status.value if hasattr(o.status, "value") else o.status,
        "delivery_address": o.delivery_address, "notes": o.notes,
    }
