from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from app.db.session import get_session
from app.modules.auth.repository import UserRepository
from app.modules.auth.schemas import (
    UserLogin,
    UserRegister,
    UserResponse,
)
from app.modules.auth.service import AuthService

router = APIRouter()


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    responses={
        400: {
            "description": "Email already registered",
        },
    },
)
def register(
    user_data: UserRegister,
    session: Session = Depends(get_session),
):
    repository = UserRepository(session)
    service = AuthService(repository)

    try:
        user = service.register(user_data)
        return user
    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error),
        ) from error


@router.post("/login")
def login(
    credentials: UserLogin,
    session: Session = Depends(get_session),
):
    repository = UserRepository(session)
    service = AuthService(repository)

    user = service.login(
        credentials.email,
        credentials.password,
    )

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password",
        )

    return {
        "message": "Login successful",
        "user": user.full_name,
    }
