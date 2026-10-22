from fastapi import APIRouter, Depends
from app.core.dependencies import require_role
from app.models.user import User, Role
from app.schemas.farm import FarmCreate, FarmOut
from app.services import farm_service

router = APIRouter()


@router.post("/", response_model=FarmOut, status_code=201)
async def create_farm(payload: FarmCreate, current: User = Depends(require_role(Role.FARMER))):
    return await farm_service.create_farm(str(current.id), payload.model_dump())


@router.get("/", response_model=list[FarmOut])
async def list_farms():
    return await farm_service.list_farms()


@router.get("/{farm_id}", response_model=FarmOut)
async def get_farm(farm_id: str):
    return await farm_service.get_farm(farm_id)
