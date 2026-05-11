from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.exc import IntegrityError
from datetime import timedelta

from src.database.db import AsyncSession
from src.repositories.user_repository import UserRepository
from src.exception_handlers.user_exceptions import UserNotFoundException, UnauthorizedException, UserAlreadyExists
from src.exception_handlers.db_exception import DatabaseException
from src.auth.utils import verify_password, hash_password
from src.core.config import settings
from src.auth.jwt_handler import JWTHandler
from src.api.schemas.user_schema import UserCreate



class AuthUserService:
    def __init__(self, session: AsyncSession, jwt_handler: JWTHandler):
        self.session = session
        self.user_repo = UserRepository(session=session)
        self.jwt_handler = jwt_handler
    
    # login servisi (sonra api ile bağlanılacak)
    async def auth_user(self, credents: OAuth2PasswordRequestForm) -> dict:
        user = await self.user_repo.get_user_with_email(email=credents.username)

        if not user:
            raise UserNotFoundException("Kullanıcı bulunamadı")
        
        if not user.is_active:
            raise UnauthorizedException("Kullanıcının yetkisi yok")
        
        if not verify_password(credents.password, user.password):
            raise UnauthorizedException("Geçersiz kimlik bilgiler")
        
        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

        access_token = self.jwt_handler.create_access_token(
            subject=str(user.id),
            role=user.role,
            expires_delta=access_token_expires
        )

        return {
            "access_token": access_token,
            "token_type": "bearer"
        }
    
    # yeni kullanıcı veritabana ekleme fonksyionu
    async def add_new_user(self, user: UserCreate) -> dict:
        existing_user = await self.user_repo.get_user_with_email(email=user.email)

        if existing_user:
            raise UserAlreadyExists("Kullanıcı zaten mevcut")
        
        hashed_password = hash_password(user.password)

        try:
            new_user = await self.user_repo.create(
                email=user.email,
                password=hashed_password,
                role=user.role
            )
        except IntegrityError:
            raise DatabaseException("Veritaban hatası")
        
        return {"detail": "Kullanıcı başarıyla oluşturuldu"}
