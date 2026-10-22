from datetime import datetime
from enum import Enum
from beanie import Document
from pydantic import EmailStr


class Role(str, Enum):
    FARMER = "farmer"
    BUYER = "buyer"
    AGROVET = "agrovet"
    TRANSPORTER = "transporter"
    CONTRIBUTOR = "contributor"
    VERIFIER = "verifier"
    ADMIN = "admin"


class User(Document):
    full_name: str
    email: EmailStr
    phone: str | None = None
    password_hash: str
    role: Role = Role.FARMER
    is_active: bool = True
    created_at: datetime = datetime.utcnow
    updated_at: datetime = datetime.utcnow

    class Settings:
        name = "users"
        indexes = ["email", "role"]
