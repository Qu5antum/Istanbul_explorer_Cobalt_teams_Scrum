from .base_exception import BaseAppException 


class AccessException(BaseAppException):
    """Hakları kısıtlama hatası"""
    def __init__(self, detail: str):
        super().__init__(detail, status_code=403)