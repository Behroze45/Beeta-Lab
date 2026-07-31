from pwdlib import PasswordHash

from app.modules.auth.models import User
from app.modules.auth.repository import UserRepository
from app.modules.auth.schemas import UserRegister

password_hash = PasswordHash.recommended()


class AuthService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def register(self, user_data: UserRegister) -> User:
        existing_user = self.repository.get_by_email(user_data.email)

        if existing_user:
            raise ValueError("Email already registered")

        hashed_password = password_hash.hash(user_data.password)

        user = User(
            full_name=user_data.full_name,
            email=user_data.email,
            hashed_password=hashed_password,
        )

        return self.repository.create(user)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return password_hash.verify(plain_password, hashed_password)

    def login(self, email: str, password: str) -> User | None:
        user = self.repository.get_by_email(email)

        if not user:
            return None

        if not self.verify_password(password, user.hashed_password):
            return None

        return user
