from fastapi import APIRouter
from app.services.system_monitor import get_status

router = APIRouter(
    prefix="/api",
    tags=["System Monitor"]
)

@router.get("/status")
def system_status():
    return get_status()
