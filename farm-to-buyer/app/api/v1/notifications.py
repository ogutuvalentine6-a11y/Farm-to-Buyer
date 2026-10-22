from fastapi import APIRouter, Depends
from app.core.dependencies import get_current_user
from app.models.user import User
from app.schemas.notification import NotificationOut
from app.services import notification_service

router = APIRouter()


@router.get("/", response_model=list[NotificationOut])
async def my_notifications(current: User = Depends(get_current_user)):
    return await notification_service.list_notifications(str(current.id))
