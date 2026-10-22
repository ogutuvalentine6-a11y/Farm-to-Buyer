from fastapi import APIRouter
from app.api.v1 import (
    auth, users, farms, produce, agrovets, products,
    orders, transport, payments, knowledge, messages,
    notifications, verification, ai_assistant,
)

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(farms.router, prefix="/farms", tags=["farms"])
api_router.include_router(produce.router, prefix="/produce", tags=["produce"])
api_router.include_router(agrovets.router, prefix="/agrovets", tags=["agrovets"])
api_router.include_router(products.router, prefix="/products", tags=["products"])
api_router.include_router(orders.router, prefix="/orders", tags=["orders"])
api_router.include_router(transport.router, prefix="/transport", tags=["transport"])
api_router.include_router(payments.router, prefix="/payments", tags=["payments"])
api_router.include_router(knowledge.router, prefix="/knowledge", tags=["knowledge"])
api_router.include_router(messages.router, prefix="/messages", tags=["messages"])
api_router.include_router(notifications.router, prefix="/notifications", tags=["notifications"])
api_router.include_router(verification.router, prefix="/verification", tags=["verification"])
api_router.include_router(ai_assistant.router, prefix="/ai", tags=["ai"])
