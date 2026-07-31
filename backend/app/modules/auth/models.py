from datetime import UTC, datetime

from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: int | None = Field(default=None, primary_key=True)

    full_name: str
    email: str = Field(index=True, unique=True)

    hashed_password: str

    is_active: bool = Field(default=True)
    is_verified: bool = Field(default=False)

    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
