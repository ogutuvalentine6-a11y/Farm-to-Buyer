from fastapi import APIRouter, HTTPException, status
from app.schemas.user import UserCreate, UserLogin, Token
from app.services import auth_service

router = APIRouter()


@router.post("/register", response_model=Token, status_code=201)
async def register(payload: UserCreate):
    user = await auth_service.register_user(payload.model_dump())
    if not user:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "Email already exists")
    token = auth_service.issue_token(user)
    return {"access_token": token, "token_type": "bearer"}


@router.post("/login", response_model=Token)
async def login(payload: UserLogin):
    user = await auth_service.authenticate(payload.email, payload.password)
    if not user:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid credentials")
    token = auth_service.issue_token(user)
    return {"access_token": token, "token_type": "bearer"}
