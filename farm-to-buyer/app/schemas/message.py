from pydantic import BaseModel


class MessageCreate(BaseModel):
    recipient_id: str
    body: str


class MessageOut(MessageCreate):
    id: str
    sender_id: str
    read: bool
