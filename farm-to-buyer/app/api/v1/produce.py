from fastapi import APIRouter, Depends
from app.core.dependencies import require_role
from app.models.user import User, Role
from app.schemas.produce import ProduceCreate, ProduceOut
from app.services import marketplace_service

router = APIRouter()


@router.post("/", response_model=ProduceOut, status_code=201)
async def create_listing(payload: ProduceCreate, current: User = Depends(require_role(Role.FARMER))):
    return await marketplace_service.create_produce(str(current.id), payload.model_dump())


@router.get("/", response_model=list[ProduceOut])
async def list_produce(q: str | None = None):
    return await marketplace_service.search_produce(q)
