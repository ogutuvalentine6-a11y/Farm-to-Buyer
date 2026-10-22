from fastapi import APIRouter, Depends
from app.core.dependencies import get_current_user
from app.models.user import User
from app.schemas.user import UserOut

router = APIRouter()


@router.get("/me", response_model=UserOut)
async def me(current: User = Depends(get_current_user)):
    return {
        "id": str(current.id),
        "full_name": current.full_name,
        "email": current.email,
        "role": current.role,
        "is_active": current.is_active,
    }
