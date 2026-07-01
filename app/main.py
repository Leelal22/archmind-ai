from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)


@app.get("/")
async def root():
    return {
        "app": settings.app_name,
        "version": settings.app_version,
        "database": settings.database_url.split("@")[-1],
        "message": "Configuration Loaded Successfully 🚀"
    }