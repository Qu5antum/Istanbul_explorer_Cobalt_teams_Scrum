from typing import Optional, Dict, Any
from datetime import datetime, timedelta, timezone
from jose import jwt

from src.core.config import settings

class JWTHandler:
    
    @staticmethod
    def create_access_token(
        subject: str, 
        role: str, 
        expires_delta: Optional[timedelta] = None
    ) -> str:
        """JWT token oluşruma"""
        if expires_delta: 
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

        to_encode = {
            "sub": str(subject),
            "exp": expire,
            "iat": datetime.now(timezone.utc),
            "role": role,
        }

        encoded_jwt = jwt.encode(
            to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
        )

        return encoded_jwt
    
    @staticmethod
    def decode_token(token: str) -> Dict[str, Any]:
        """Decode JWT token"""
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        return payload
        


