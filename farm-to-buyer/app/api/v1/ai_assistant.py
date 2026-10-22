from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.core.dependencies import get_current_user
from app.models.user import User
from app.services import ai_service

router = APIRouter()


class ChatIn(BaseModel):
    message: str
    context: dict | None = None


@router.post("/chat")
async def chat(payload: ChatIn, current: User = Depends(get_current_user)):
    reply = await ai_service.ask(payload.message, payload.context or {})
    return {"reply": reply}
