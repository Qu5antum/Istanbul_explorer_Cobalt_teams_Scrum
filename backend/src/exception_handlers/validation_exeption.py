from .base_exception import BaseAppException


class ValidationException(BaseAppException):
    """Giriş doğrulaması başarısız olduğunda çağrılır."""
    def __init__(self, message: str):
        super().__init__(message, status_code=400)