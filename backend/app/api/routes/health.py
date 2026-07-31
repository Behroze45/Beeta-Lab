from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.api.deps import get_session

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get("/")
async def health_check(
    db: Session = Depends(get_session),
):
    return {
        "status": "ok",
        "message": "Beeta Lab API is running",
        "version": "0.1.0",
        "database": "connected",
    }
