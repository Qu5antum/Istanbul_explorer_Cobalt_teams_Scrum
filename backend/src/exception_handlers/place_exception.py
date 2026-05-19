from .base_exception import BaseAppException


class PlaceNotFoundException(BaseAppException):
    """Konum yoksa hata verir"""
    def __init__(self, message: str):
        super().__init__(message, status_code=404)


class PlaceAlreadyExists(BaseAppException):
    """konum bulunamadığında hata oluşur."""
    def __init__(self, message: str):
        super().__init__(message, status_code=400)


class PlaceAlreadyInFavorite(BaseAppException):
    """Konum zaten favoride hatasi"""
    def __init__(self, message: str):
        super().__init__(message, status_code=400)