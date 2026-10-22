from fastapi import APIRouter, Depends
from app.core.dependencies import require_role
from app.models.user import User, Role
from app.schemas.agrovet import AgrovetCreate, AgrovetOut
from app.services import agrovet_service

router = APIRouter()


@router.post("/", response_model=AgrovetOut, status_code=201)
async def create_shop(payload: AgrovetCreate, current: User = Depends(require_role(Role.AGROVET))):
    return await agrovet_service.create_agrovet(str(current.id), payload.model_dump())


@router.get("/", response_model=list[AgrovetOut])
async def list_shops():
    return await agrovet_service.list_agrovets()
