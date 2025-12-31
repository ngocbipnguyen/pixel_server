import uuid
from fastapi import APIRouter, UploadFile, File, HTTPException
from src.core.minio import minio_client, ensure_bucket, MINIO_BUCKET, MINIO_PUBLIC_URL

router_upload = APIRouter(prefix="/upload", tags=["Upload"])

ALLOWED_TYPES = [
    "image/jpeg",
    "image/png",
    "image/webp",
    "video/mp4",
    "video/mov"
]

@router_upload.post("/")
async def upload_file(file: UploadFile = File(...)):
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(status_code=400, detail="File type not allowed")

    ensure_bucket()

    file_ext = file.filename.split(".")[-1]
    object_name = f"{uuid.uuid4()}.{file_ext}"

    minio_client.put_object(
        bucket_name=MINIO_BUCKET,
        object_name=object_name,
        data=file.file,
        length=-1,
        part_size=10 * 1024 * 1024,
        content_type=file.content_type
    )

    file_url = f"{MINIO_PUBLIC_URL}/{MINIO_BUCKET}/{object_name}"

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "url": file_url
    }
