
from fastapi import FastAPI, Request
from helpers.api_responser import ApiResponser

async def test_f(request: Request):
    return ApiResponser.set_response("This is test",
                                     status_code=200,
                                     status="Success",
                                     message="Test successful",
                                     request=request)
