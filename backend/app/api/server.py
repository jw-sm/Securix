from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core import config, tasks

from app.api.routes import router as api_router

def get_application():
    app = FastAPI(
        title=config.PROJECT_NAME, version=config.VERSION, lifespan=tasks.lifespan
    )

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

    # deprecated
    # app.add_event_handler("startup", tasks.create_start_app_handler(app))
    # app.add_event_handler("shutdown", tasks.create_stop_app_handler(app))

    app.include_router(api_router, prefix="/api")

    return app


app = get_application()
