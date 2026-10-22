import asyncio
import getpass
from app.core.database import init_db, close_db
from app.core.security import hash_password
from app.models import ALL_MODELS
from app.models.user import User, Role


async def main():
    await init_db(ALL_MODELS)
    email = input("Admin email: ").strip()
    password = getpass.getpass("Password: ")
    if await User.find_one(User.email == email):
        print("User already exists")
    else:
        await User(
            full_name="Administrator", email=email,
            password_hash=hash_password(password), role=Role.ADMIN,
        ).insert()
        print(f"Admin {email} created")
    await close_db()


if __name__ == "__main__":
    asyncio.run(main())
