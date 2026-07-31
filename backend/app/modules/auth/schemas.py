from pydantic import EmailStr
from sqlmodel import SQLModel


class UserRegister(SQLModel):
    full_name: str
    email: EmailStr
    password: str


class UserLogin(SQLModel):
    email: EmailStr
    password: str


class UserResponse(SQLModel):
    id: int
    full_name: str
    email: EmailStr
    is_active: bool
    is_verified: bool


class Token(SQLModel):
    access_token: str
    token_type: str = "bearer"
