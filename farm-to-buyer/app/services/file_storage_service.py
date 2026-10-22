import os
import uuid
from fastapi import UploadFile
from app.core.config import settings


async def save_upload(file: UploadFile, subdir: str) -> str:
    target_dir = os.path.join(settings.UPLOAD_DIR, subdir)
    os.makedirs(target_dir, exist_ok=True)
    ext = os.path.splitext(file.filename or "")[1]
    name = f"{uuid.uuid4().hex}{ext}"
    path = os.path.join(target_dir, name)
    contents = await file.read()
    if len(contents) > settings.MAX_UPLOAD_MB * 1024 * 1024:
        raise ValueError("File too large")
    with open(path, "wb") as f:
        f.write(contents)
    return f"/static/uploads/{subdir}/{name}"
