import asyncio
from app.core.database import init_db, close_db
from app.core.security import hash_password
from app.models import ALL_MODELS
from app.models.user import User, Role


async def main():
    await init_db(ALL_MODELS)
    samples = [
        ("Admin User", "admin@example.com", Role.ADMIN),
        ("Jane Farmer", "farmer@example.com", Role.FARMER),
        ("John Buyer", "buyer@example.com", Role.BUYER),
        ("Agrovet Owner", "agrovet@example.com", Role.AGROVET),
        ("Transporter", "transporter@example.com", Role.TRANSPORTER),
    ]
    for name, email, role in samples:
        if await User.find_one(User.email == email):
            continue
        await User(
            full_name=name, email=email,
            password_hash=hash_password("password123"), role=role,
        ).insert()
        print(f"seeded {email}")
    await close_db()


if __name__ == "__main__":
    asyncio.run(main())
