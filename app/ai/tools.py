"""
ZEK Tools

Each function returns structured data that the AI can use.
"""

import os
import shutil
import socket
import subprocess
import time

import psutil


BOOT_TIME = time.time()


def server_status():
    return {
        "status": "online",
        "message": "Server is running."
    }


def cpu_usage():
    return {
        "cpu_percent": psutil.cpu_percent(interval=1)
    }


def memory_usage():
    mem = psutil.virtual_memory()

    return {
        "total_mb": round(mem.total / 1024 / 1024),
        "used_mb": round(mem.used / 1024 / 1024),
        "available_mb": round(mem.available / 1024 / 1024),
        "percent": mem.percent
    }

def storage_usage():
    disk = shutil.disk_usage("/")

    total_gb = round(disk.total / 1024**3, 2)
    used_gb = round(disk.used / 1024**3, 2)
    free_gb = round(disk.free / 1024**3, 2)

    used_percent = round(
        (disk.used / disk.total) * 100, 1
    ) if disk.total else 0

    return {
        "total_gb": total_gb,
        "used_gb": used_gb,
        "free_gb": free_gb,
        "used_percent": used_percent
    }

def uptime():
    seconds = int(time.time() - BOOT_TIME)

    return {
        "uptime_seconds": seconds
    }


def internet_status():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return {"internet": True}
    except Exception:
        return {"internet": False}


def running_services():
    try:
        output = subprocess.check_output(
            ["systemctl", "list-units", "--type=service", "--state=running"],
            text=True
        )

        return {
            "services": output
        }

    except Exception:
        return {
            "services": "systemctl unavailable"
        }

def battery_status():
    try:
        output = subprocess.check_output(
            ["termux-battery-status"],
            text=True,
            timeout=5
        )

        import json
        data = json.loads(output)

        return {
            "available": True,
            "percentage": data.get("percentage"),
            "status": data.get("status"),
            "plugged": data.get("plugged"),
            "health": data.get("health"),
            "temperature": data.get("temperature"),
            "voltage": data.get("voltage"),
            "current": data.get("current"),
        }

    except Exception as e:
        return {
            "available": False,
            "error": str(e)
        }
def list_tools():
    return [
        "server_status",
        "cpu_usage",
        "memory_usage",
        "storage_usage",
        "uptime",
        "internet_status",
        "running_services",
        "battery_status"
    ]
