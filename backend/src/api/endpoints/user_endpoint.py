from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from src.database.db import AsyncSession
from src.services.auth_service import AuthUserService
from src.api.schemas.user_schema import UserCreate


user_router = APIRouter(
    prefix="/api/user",
    tags=['users']
)

async def get_auth_service(session: AsyncSession):
    return await AuthUserService(session=session)


@user_router.post("/register", status_code=201)
async def register_new_user(
    user: UserCreate,
    auth_service: AuthUserService = Depends(get_auth_service)
):
    return await auth_service.add_new_user(user=user)


@user_router.post("/login", status_code=201)
async def login_user(
    credents: OAuth2PasswordRequestForm = Depends(),
    auth_service: AuthUserService = Depends(get_auth_service)
):
    return await auth_service.auth_user(credents=credents)