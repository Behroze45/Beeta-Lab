from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import api_router
from app.core.config import settings
from app.core.exceptions import register_exception_handlers
from app.core.logging import logger
from app.db.session import create_db_and_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting Beeta Lab API...")

    create_db_and_tables()

    logger.info("SQLite database initialized.")

    yield

    logger.info("Stopping Beeta Lab API...")


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    lifespan=lifespan,
)

register_exception_handlers(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_url],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)


@app.get("/")
async def root():
    return {
        "message": "Welcome to Beeta Lab API",
    }
