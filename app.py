from fastapi import FastAPI
from routes.api import router as api_router
from middleware.cors import add_cors_middleware

app = FastAPI()

# Add CORS middleware
add_cors_middleware(app)

# Include the routes from the api router
app.include_router(api_router, prefix="/api")
