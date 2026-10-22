import httpx
from app.core.config import settings

SYSTEM_PROMPT = (
    "You are a farming assistant for Kenyan smallholder farmers. "
    "Answer in simple language. Ask clarifying questions when details are missing. "
    "Never claim to replace a veterinarian or extension officer. "
    "For medicines and pesticides, always refer to approved labels and qualified advice. "
    "Do not present unverified traditional remedies as proven treatments."
)


async def ask(message: str, context: dict) -> str:
    if not settings.AI_API_KEY:
        return (
            "AI assistant is not configured yet. Please set AI_API_KEY in the backend "
            "environment. For urgent issues, contact your local extension officer or vet."
        )
    payload = {
        "model": settings.AI_MODEL or "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": message},
        ],
    }
    async with httpx.AsyncClient(timeout=30) as client:
        r = await client.post(
            "https://api.openai.com/v1/chat/completions",
            headers={"Authorization": f"Bearer {settings.AI_API_KEY}"},
            json=payload,
        )
        r.raise_for_status()
        return r.json()["choices"][0]["message"]["content"]
