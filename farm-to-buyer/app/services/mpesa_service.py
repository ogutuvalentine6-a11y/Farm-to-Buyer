import base64
from datetime import datetime
import httpx
from app.core.config import settings

SANDBOX = "https://sandbox.safaricom.co.ke"
PROD = "https://api.safaricom.co.ke"


def _base() -> str:
    return SANDBOX if settings.MPESA_ENV == "sandbox" else PROD


async def get_access_token() -> str:
    auth = base64.b64encode(
        f"{settings.MPESA_CONSUMER_KEY}:{settings.MPESA_CONSUMER_SECRET}".encode()
    ).decode()
    async with httpx.AsyncClient() as client:
        r = await client.get(
            f"{_base()}/oauth/v1/generate?grant_type=client_credentials",
            headers={"Authorization": f"Basic {auth}"},
        )
        r.raise_for_status()
        return r.json()["access_token"]


async def stk_push(phone: str, amount: float, account_ref: str) -> dict:
    token = await get_access_token()
    ts = datetime.now().strftime("%Y%m%d%H%M%S")
    password = base64.b64encode(
        f"{settings.MPESA_SHORTCODE}{settings.MPESA_PASSKEY}{ts}".encode()
    ).decode()
    payload = {
        "BusinessShortCode": settings.MPESA_SHORTCODE,
        "Password": password,
        "Timestamp": ts,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": int(amount),
        "PartyA": phone,
        "PartyB": settings.MPESA_SHORTCODE,
        "PhoneNumber": phone,
        "CallBackURL": settings.MPESA_CALLBACK_URL,
        "AccountReference": account_ref,
        "TransactionDesc": "Farm-to-Buyer order",
    }
    async with httpx.AsyncClient() as client:
        r = await client.post(
            f"{_base()}/mpesa/stkpush/v1/processrequest",
            json=payload,
            headers={"Authorization": f"Bearer {token}"},
        )
        r.raise_for_status()
        return r.json()
