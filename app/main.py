from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.health import router as health_router
from app.api.auth import router as auth_router
from app.database.database import engine
from app.database.models import Base
from app.api.dashboard import router as dashboard_router
from app.api.files import router as files_router
from app.api.file_info import router as file_info_router
from app.api.download import router as download_router
from app.api.ai import router as ai_router
from app.api.status import router as status_router

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Aslam AI Home Server",
    version="0.1.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)
app.include_router(auth_router)
app.include_router(dashboard_router)
app.include_router(files_router)

app.include_router(file_info_router)
app.include_router(download_router)
app.include_router(ai_router)
app.include_router(status_router)
@app.get("/")
async def root():
    return {
        "project": "Aslam AI Home Server",
        "status": "online",
        "device": "Samsung Galaxy M12"
    }
