from datetime import datetime


def now_utc() -> datetime:
    return datetime.utcnow()


def to_str_id(value) -> str | None:
    return str(value) if value else None
