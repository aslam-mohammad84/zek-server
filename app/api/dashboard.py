from app.services.file_stats import scan_directory
from fastapi import APIRouter
import psutil
import platform
import socket

from datetime import datetime

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/")
def dashboard():

    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    boot_time = datetime.fromtimestamp(
        psutil.boot_time()
    )

    try:
        ip = socket.gethostbyname(
            socket.gethostname()
        )
    except Exception:
        ip = "Unavailable"
    home_stats = scan_directory("/storage/emulated/0")
    return {
        "server": {
            "name": "Aslam AI Home Server",
            "device": "Samsung Galaxy M12",
            "status": "Online"
        },

        "system": {
            "hostname": socket.gethostname(),
            "os": platform.system(),
            "cpu_percent": psutil.cpu_percent(interval=0.2),
            "cpu_cores": psutil.cpu_count(),
            "boot_time": boot_time.strftime("%Y-%m-%d %H:%M:%S"),
            "ip_address": ip
        },

        "memory": {
            "used_mb": round(memory.used / 1024 / 1024),
            "total_mb": round(memory.total / 1024 / 1024),
            "percent": memory.percent
        },

        "storage": {
            "used_gb": round(disk.used / 1024 / 1024 / 1024, 2),
            "total_gb": round(disk.total / 1024 / 1024 / 1024, 2),
            "percent": disk.percent
        },
"files": {
    "total_files": home_stats["files"],
    "total_folders": home_stats["folders"],
    "images": home_stats["images"],
    "videos": home_stats["videos"],
    "documents": home_stats["documents"]
}
    }
