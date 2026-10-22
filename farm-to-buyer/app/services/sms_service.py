from app.core.config import settings


async def send_sms(phone: str, message: str) -> dict:
    # Integration point — plug in your SMS provider (Africa's Talking, Twilio, etc.)
    return {"to": phone, "message": message, "provider": settings.SMS_PROVIDER, "status": "queued"}
