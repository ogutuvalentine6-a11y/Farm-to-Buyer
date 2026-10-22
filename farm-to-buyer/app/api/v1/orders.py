from fastapi import APIRouter, Depends
from app.core.dependencies import get_current_user, require_role
from app.models.user import User, Role
from app.schemas.order import OrderCreate, OrderOut
from app.services import order_service

router = APIRouter()


@router.post("/", response_model=OrderOut, status_code=201)
async def place_order(payload: OrderCreate, current: User = Depends(require_role(Role.BUYER))):
    return await order_service.create_order(str(current.id), payload.model_dump())


@router.get("/mine", response_model=list[OrderOut])
async def my_orders(current: User = Depends(get_current_user)):
    return await order_service.list_user_orders(str(current.id))


@router.patch("/{order_id}/confirm", response_model=OrderOut)
async def confirm_order(order_id: str, current: User = Depends(get_current_user)):
    return await order_service.update_status(order_id, "confirmed")
