from fastapi import APIRouter, Depends
from app.core.dependencies import get_current_user
from app.models.user import User
from app.schemas.message import MessageCreate, MessageOut
from app.services import notification_service

router = APIRouter()


@router.post("/", response_model=MessageOut, status_code=201)
async def send_message(payload: MessageCreate, current: User = Depends(get_current_user)):
    return await notification_service.send_message(str(current.id), payload.model_dump())


@router.get("/inbox", response_model=list[MessageOut])
async def inbox(current: User = Depends(get_current_user)):
    return await notification_service.list_inbox(str(current.id))
