from fastapi import APIRouter, File, UploadFile, Depends
from PIL import Image
from io import BytesIO

from app.services.caption import generate_caption
from app.services.translation import translate_en_to_fr
from app.auth.basic_auth import authenticate

router = APIRouter()

@router.post("/generate-alt-post-upload")
async def generate_alt(image: UploadFile = File(...), user: str = Depends(authenticate)):
    contents = await image.read()
    image = Image.open(BytesIO(contents)).convert("RGB")

    en_caption = generate_caption(image)
    fr_caption = translate_en_to_fr(en_caption)

    return {
        "en-desc": en_caption,
        "fr-desc": fr_caption
    }
