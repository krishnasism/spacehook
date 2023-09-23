from fastapi import APIRouter
from .services import requests, settings

router = APIRouter()

router.include_router(requests.router, tags=["requests"])
router.include_router(settings.router, tags=["settings"], prefix="/settings")
