from fastapi import FastAPI, Request
from helpers.api_responser import ApiResponser
import cv2
from PIL import Image

async def ocr_f(request: Request):
    return ApiResponser.set_response("This is OCR test",
                                     status_code=200,
                                     status="Success",
                                     message="OCR test",
                                     request=request)
