import uuid
from fastapi import APIRouter, UploadFile, File, HTTPException
from src.core.minio import minio_client, ensure_bucket, MINIO_BUCKET, MINIO_PUBLIC_URL, create_bucket
from PIL import Image
from io import BytesIO

router_upload = APIRouter(prefix="/upload")

ALLOWED_TYPES = [
    "image/jpeg",
    "image/jpg",
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
        part_size=20 * 1024 * 1024,
        content_type=file.content_type
    )

    file_url = f"{MINIO_PUBLIC_URL}/{MINIO_BUCKET}/{object_name}"

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "url": file_url
    }

@router_upload.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    file_bytes = await file.read()
    images = generate_images(file_bytes)

    file_ext = file.filename.split(".")[-1]
    object_name = f"{uuid.uuid4()}.{file_ext}"

    urls = {}
    for name, img in images.items():
        create_bucket(name_ducket=name)
        data = image_to_bytes(img=img, type=file_ext)

        minio_client.put_object(
            bucket_name=name,
            object_name=object_name,
            data=BytesIO(data),
            length=-1,
            part_size=20 * 1024 * 1024,
            content_type=file.content_type
        )
        urls[name] = f"{MINIO_PUBLIC_URL}/{name}/{object_name}"

    return urls



def resize_image(img: Image.Image, scale: int):
    w, h = img.size
    new_size = (w // scale, h // scale)

    return img.resize(new_size, Image.Resampling.LANCZOS)


def generate_images(file_bytes: bytes):
    original = Image.open(BytesIO(file_bytes)).convert("RGB")

    media = resize_image(original, 2)
    small = resize_image(original, 5)
    thumbnail = resize_image(original, 10)

    return {
        "original": original,
        "large": media,
        "medium": small,
        "small": thumbnail
    }

def image_to_bytes(img: Image.Image, type: str) -> bytes:
    buf = BytesIO()
    img.save(buf, format=type, quality=85)
    return buf.getvalue()
