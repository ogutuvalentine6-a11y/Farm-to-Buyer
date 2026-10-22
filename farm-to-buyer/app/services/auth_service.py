from app.core.security import hash_password, verify_password, create_access_token
from app.models.user import User


async def register_user(data: dict) -> User | None:
    if await User.find_one(User.email == data["email"]):
        return None
    data = data.copy()
    data["password_hash"] = hash_password(data.pop("password"))
    user = User(**data)
    await user.insert()
    return user


async def authenticate(email: str, password: str) -> User | None:
    user = await User.find_one(User.email == email)
    if user and verify_password(password, user.password_hash):
        return user
    return None


def issue_token(user: User) -> str:
    return create_access_token({"sub": str(user.id), "role": user.role})
