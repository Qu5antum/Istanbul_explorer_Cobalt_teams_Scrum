from .base_exception import BaseAppException


class CategoryNotFoundException(BaseAppException):
    """Konum yoksa hata verir"""
    def __init__(self, message: str):
        super().__init__(message, status_code=404)


class CategoryAlreadyExists(BaseAppException):
    """konum bulunamadığında hata oluşur."""
    def __init__(self, message: str):
        super().__init__(message, status_code=400)


class SomeCategoryNotFound(BaseAppException):
    def __init__(self, message: str):
        super().__init__(message, status_code=404)