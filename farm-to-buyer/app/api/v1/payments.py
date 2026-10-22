from fastapi import APIRouter, Depends
from app.core.dependencies import get_current_user
from app.models.user import User
from app.schemas.payment import PaymentCreate, PaymentOut
from app.services import payment_service

router = APIRouter()


@router.post("/", response_model=PaymentOut, status_code=201)
async def initiate_payment(payload: PaymentCreate, current: User = Depends(get_current_user)):
    return await payment_service.initiate(str(current.id), payload.model_dump())


@router.post("/mpesa/callback")
async def mpesa_callback(body: dict):
    return await payment_service.handle_mpesa_callback(body)
