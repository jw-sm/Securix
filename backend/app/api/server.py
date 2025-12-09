from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router as api_router


def get_application():
    app = FastAPI(title="Securix", version="1.0.0")

    # Browser blocks cross-domain API calls by default
    app.add_middleware(
        CORSMiddleware,
        # This allows any website to make request (development use only)
        # in prod, I have to change this to "allow_origins=["https://myfrontend.com"]"
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(api_router, prefix="/api")

    return app


app = get_application()
