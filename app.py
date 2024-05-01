from fastapi import FastAPI
from routes.api import router as api_router

app = FastAPI()

# Include the routes from the api router
app.include_router(api_router, prefix="/api")
