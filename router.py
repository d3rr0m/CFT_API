from fastapi import APIRouter

from api.handlers import router as salary_router

api_router = APIRouter()
api_router.include_router(salary_router)
