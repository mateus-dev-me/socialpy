from fastapi import APIRouter

from .endpoints.auth import router as auth_router
from .endpoints.post import router as post_router
from .endpoints.user import router as user_router

main_router = APIRouter()

main_router.include_router(auth_router, tags=['auth'])
main_router.include_router(user_router, prefix='/user', tags=['user'])
main_router.include_router(post_router, prefix='/post', tags=['post'])
