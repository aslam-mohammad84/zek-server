from fastapi import APIRouter
import psutil
import socket
import platform
import time

router = APIRouter()

@router.get("/health")
def health():

    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    try:
        battery = psutil.sensors_battery()
        battery_percent = battery.percent if battery else None
        charging = battery.power_plugged if battery else None
    except:
        battery_percent = None
        charging = None

    uptime_seconds = int(time.time() - psutil.boot_time())

    return {

        "status": "online",

        "device": "Samsung Galaxy M12",

        "hostname": socket.gethostname(),

        "ip": socket.gethostbyname(socket.gethostname()),

        "os": platform.system(),

        "cpu_percent": psutil.cpu_percent(),

        "cpu_cores": psutil.cpu_count(),

        "memory": {
            "used_mb": round(memory.used/1024/1024),
            "total_mb": round(memory.total/1024/1024),
            "percent": memory.percent
        },

        "storage": {
            "used_gb": round(disk.used/1024/1024/1024,2),
            "total_gb": round(disk.total/1024/1024/1024,2),
            "percent": disk.percent
        },

        "battery": {
            "percent": battery_percent,
            "charging": charging
        },

        "uptime_seconds": uptime_seconds
    }
