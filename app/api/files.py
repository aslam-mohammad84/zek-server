from fastapi import APIRouter
import os

router = APIRouter(
    prefix="/files",
    tags=["Files"]
)


@router.get("/")
def list_files(path: str = "/storage/emulated/0"):

    if not os.path.exists(path):
        return {
            "error": "Path not found"
        }

    folders = []
    files = []

    for item in os.listdir(path):
        full_path = os.path.join(path, item)

        if os.path.isdir(full_path):
            folders.append(item)
        else:
            files.append(item)

    return {
        "path": path,
        "folders": sorted(folders),
        "files": sorted(files)
    }
