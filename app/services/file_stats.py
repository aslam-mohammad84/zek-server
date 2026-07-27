import os

IMAGE_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".bmp",
    ".webp",
    ".heic"
}

VIDEO_EXTENSIONS = {
    ".mp4",
    ".mkv",
    ".avi",
    ".mov",
    ".3gp",
    ".webm"
}

DOCUMENT_EXTENSIONS = {
    ".pdf",
    ".doc",
    ".docx",
    ".txt",
    ".ppt",
    ".pptx",
    ".xls",
    ".xlsx"
}


def scan_directory(path):

    stats = {
        "files": 0,
        "folders": 0,
        "images": 0,
        "videos": 0,
        "documents": 0
    }

    if not os.path.exists(path):
        return stats

    for root, dirs, files in os.walk(path):

        stats["folders"] += len(dirs)

        for file in files:

            stats["files"] += 1

            ext = os.path.splitext(file)[1].lower()

            if ext in IMAGE_EXTENSIONS:
                stats["images"] += 1

            elif ext in VIDEO_EXTENSIONS:
                stats["videos"] += 1

            elif ext in DOCUMENT_EXTENSIONS:
                stats["documents"] += 1

    return stats
