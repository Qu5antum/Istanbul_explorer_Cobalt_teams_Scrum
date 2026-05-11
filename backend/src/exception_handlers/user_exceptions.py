from .base_exception import BaseAppException


class UserNotFoundException(BaseAppException):
    """Kullanıcı bulunamadığında hata oluşur."""
    def __init__(self, message: str):
        super().__init__(message, status_code=404)


class UnauthorizedException(BaseAppException):
    """Kullanıcının yetkisi olmadığında çağrılır"""
    def __init__(self, message: str):
        super().__init__(message, status_code=401)


class UserAlreadyExists(BaseAppException):
    """Kullanıcı zaten mevcutsa çağrılır."""
    def __init__(self, message: str):
        super().__init__(message, status_code=400)