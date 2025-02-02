from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings

app = FastAPI()
print(settings.PROJECT_NAME)
print(settings.BACKEND_CORS_ORIGINS)
print(settings.POSTGRES_SERVER)
print(settings.DATABASE_URI)

def get_application():
    from .router import router

    _app = FastAPI(title=settings.PROJECT_NAME)

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            str(origin) for origin in settings.BACKEND_CORS_ORIGINS
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    _app.include_router(router, prefix="")

    return _app


app = get_application()