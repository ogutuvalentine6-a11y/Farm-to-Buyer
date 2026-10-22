from bson import ObjectId
from app.models.message import Message
from app.models.notification import Notification


async def send_message(sender_id: str, data: dict) -> dict:
    m = Message(
        sender_id=ObjectId(sender_id),
        recipient_id=ObjectId(data["recipient_id"]),
        body=data["body"],
    )
    await m.insert()
    await Notification(
        user_id=m.recipient_id, title="New message", body=data["body"]
    ).insert()
    return _to_out_msg(m)


async def list_inbox(user_id: str) -> list[dict]:
    items = await Message.find(Message.recipient_id == ObjectId(user_id)).to_list()
    return [_to_out_msg(i) for i in items]


async def list_notifications(user_id: str) -> list[dict]:
    items = await Notification.find(Notification.user_id == ObjectId(user_id)).to_list()
    return [
        {"id": str(n.id), "title": n.title, "body": n.body, "channel": n.channel, "read": n.read}
        for n in items
    ]


def _to_out_msg(m: Message) -> dict:
    return {
        "id": str(m.id), "sender_id": str(m.sender_id), "recipient_id": str(m.recipient_id),
        "body": m.body, "read": m.read,
    }
