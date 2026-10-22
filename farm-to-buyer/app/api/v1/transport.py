from fastapi import APIRouter, Depends
from app.core.dependencies import require_role
from app.models.user import User, Role
from app.schemas.delivery import DeliveryCreate, DeliveryOut, DeliveryUpdate
from app.services import transport_service

router = APIRouter()


@router.post("/", response_model=DeliveryOut, status_code=201)
async def request_delivery(payload: DeliveryCreate, current: User = Depends(require_role(Role.BUYER, Role.FARMER))):
    return await transport_service.create_delivery(payload.model_dump())


@router.patch("/{delivery_id}", response_model=DeliveryOut)
async def update_delivery(delivery_id: str, payload: DeliveryUpdate, current: User = Depends(require_role(Role.TRANSPORTER))):
    return await transport_service.update_delivery(delivery_id, payload.model_dump(exclude_unset=True))
