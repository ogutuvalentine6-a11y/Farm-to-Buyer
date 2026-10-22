from fastapi import APIRouter, Depends
from app.core.dependencies import require_role
from app.models.user import User, Role
from app.services import verification_service

router = APIRouter()


@router.post("/farms/{farm_id}")
async def verify_farm(farm_id: str, status: str, notes: str = "", current: User = Depends(require_role(Role.VERIFIER))):
    return await verification_service.verify_farm(farm_id, status, notes)


@router.post("/agrovets/{agrovet_id}")
async def verify_agrovet(agrovet_id: str, status: str, notes: str = "", current: User = Depends(require_role(Role.VERIFIER))):
    return await verification_service.verify_agrovet(agrovet_id, status, notes)
