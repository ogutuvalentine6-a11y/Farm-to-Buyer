from fastapi import APIRouter, Depends
from app.core.dependencies import require_role
from app.models.user import User, Role
from app.schemas.product import ProductCreate, ProductOut
from app.services import agrovet_service

router = APIRouter()


@router.post("/", response_model=ProductOut, status_code=201)
async def create_product(payload: ProductCreate, current: User = Depends(require_role(Role.AGROVET))):
    return await agrovet_service.create_product(payload.model_dump())


@router.get("/", response_model=list[ProductOut])
async def list_products(q: str | None = None):
    return await agrovet_service.search_products(q)
