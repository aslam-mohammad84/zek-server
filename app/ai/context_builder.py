from app.ai.history import history
from app.ai.prompts import SYSTEM_PROMPT


def build_context(user_message: str):
    """
    Build the conversation context sent to the local Qwen model.

    This function handles:
    - ZEK identity/personality through SYSTEM_PROMPT
    - Conversation history
    - Current user message

    Live server telemetry is injected separately by llm.py
    only when it is relevant.
    """

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        }
    ]

    # Add previous conversation history
    previous_messages = history.get()

    if previous_messages:
        messages.extend(previous_messages)

    # Add current user message
    messages.append(
        {
            "role": "user",
            "content": user_message,
        }
    )

    return messages
