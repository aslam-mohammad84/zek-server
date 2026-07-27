"""
ZEK System Monitor

Provides a single snapshot of the server.
"""

from app.ai.tools import (
    server_status,
    cpu_usage,
    memory_usage,
    storage_usage,
    uptime,
    internet_status,
    battery_status
)


def get_status():

    return {
        "server": server_status(),
        "cpu": cpu_usage(),
        "memory": memory_usage(),
        "storage": storage_usage(),
        "uptime": uptime(),
        "internet": internet_status(),
        "battery": battery_status(),
    }


def get_health_summary():

    data = get_status()

    return {
        "online": data["server"]["status"] == "online",
        "cpu": data["cpu"]["cpu_percent"],
        "memory": data["memory"]["percent"],
        "storage_used": data["storage"]["used_gb"],
        "storage_total": data["storage"]["total_gb"],
        "internet": data["internet"]["internet"],
    }
