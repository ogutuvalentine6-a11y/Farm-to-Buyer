from pydantic import BaseModel


class AgrovetCreate(BaseModel):
    shop_name: str
    county: str
    sub_county: str | None = None
    licence_number: str | None = None
    registration_doc_urls: list[str] = []


class AgrovetOut(AgrovetCreate):
    id: str
    owner_id: str
    verification_status: str
