import re

PHONE_RE = re.compile(r"^\+?254[17]\d{8}$")


def is_kenyan_phone(phone: str) -> bool:
    return bool(PHONE_RE.match(phone))


def normalize_phone(phone: str) -> str:
    phone = phone.strip().replace(" ", "")
    if phone.startswith("0"):
        return "+254" + phone[1:]
    if phone.startswith("254"):
        return "+" + phone
    return phone
