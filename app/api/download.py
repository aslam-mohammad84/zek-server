from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
import os

router = APIRouter(
    prefix="/download",
    tags=["Download"]
)


@router.get("/")
def download_file(path: str):

    if not os.path.exists(path):
        raise HTTPException(
            status_code=404,
            detail="File not found"
        )

    if not os.path.isfile(path):
        raise HTTPException(
            status_code=400,
            detail="Not a file"
        )

    return FileResponse(
        path=path,
        filename=os.path.basename(path)
    )
