from fastapi import FastAPI, Request
from helpers.api_responser import ApiResponser

async def ocr_f(request: Request):
    return ApiResponser.set_response("hello world",
                                     status_code=200,
                                     status="Success",
                                     details="Item created successfully",
                                     request=request)
