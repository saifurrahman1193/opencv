# middleware.py

from fastapi.middleware.cors import CORSMiddleware

def add_cors_middleware(app):
    """
    Add CORS middleware to the FastAPI application.
    """
    # Allow requests from all origins, methods, and headers
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        allow_headers=["*"],
    )
