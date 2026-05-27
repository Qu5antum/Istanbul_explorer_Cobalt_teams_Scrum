from .base_exception import BaseAppException


class RouteAlreadyExists(BaseAppException):
    def __init__(self, message: str):
        super().__init__(message, status_code=400)


class RouteNotFound(BaseAppException):
    def __init__(self, message: str):
        super().__init__(message, status_code=404)