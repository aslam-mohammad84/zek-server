from fastapi import APIRouter
import os
import mimetypes
from datetime import datetime

router = APIRouter(
    prefix="/file",
    tags=["File Information"]
)


@router.get("/info")
def file_info(path: str):

    if not os.path.exists(path):
        return {
            "error": "File not found"
        }

    stat = os.stat(path)

    return {
        "name": os.path.basename(path),
        "path": path,
        "size_bytes": stat.st_size,
        "size_mb": round(stat.st_size / 1024 / 1024, 2),
        "mime_type": mimetypes.guess_type(path)[0],
        "created": datetime.fromtimestamp(stat.st_ctime),
        "modified": datetime.fromtimestamp(stat.st_mtime),
        "is_file": os.path.isfile(path),
        "is_directory": os.path.isdir(path)
    }
