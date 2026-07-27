from fastapi import APIRouter
from pydantic import BaseModel

from app.ai.llm import chat
from app.ai.history import history

router = APIRouter(prefix="/ai", tags=["AI"])


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
def ai_chat(request: ChatRequest):
    history.add_user(request.message)

    reply = chat(request.message)

    history.add_assistant(reply)

    return {
        "assistant": "ZEK",
        "reply": reply,
        "history_length": len(history.get())
    }

