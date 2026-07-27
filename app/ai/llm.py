import requests

from app.ai.context_builder import build_context
from app.ai.config import *

from app.ai.tools import (
    server_status,
    cpu_usage,
    memory_usage,
    storage_usage,
    uptime,
    internet_status,
    battery_status,
)


# ============================================================
# ZEK TOOL REGISTRY
# ============================================================

TOOLS = {
    "server_status": server_status,
    "cpu_usage": cpu_usage,
    "memory_usage": memory_usage,
    "storage_usage": storage_usage,
    "uptime": uptime,
    "internet_status": internet_status,
    "battery_status": battery_status,
}


# ============================================================
# DETECT RELEVANT LIVE SERVER DATA
# ============================================================

def get_live_context(message: str):
    """
    Detect whether live server information may help answer the
    user's question.

    Important:
    This function DOES NOT generate the answer.

    It only collects real server data and passes it to the AI.
    Qwen/ZEK always generates the final natural-language reply.
    """

    msg = message.lower().strip()

    data = {}

    # General server questions
    general_server_terms = [
        "server",
        "system status",
        "system health",
        "server health",
        "how is my server",
        "how's my server",
    ]

    if any(term in msg for term in general_server_terms):

        for name, tool in TOOLS.items():
            try:
                data[name] = tool()
            except Exception as error:
                print(f"[ZEK] Tool {name} failed: {error}")

        return data if data else None

    # CPU
    if any(word in msg for word in [
        "cpu",
        "processor",
    ]):
        try:
            data["cpu"] = cpu_usage()
        except Exception as error:
            print(f"[ZEK] CPU tool failed: {error}")

    # Memory
    if any(word in msg for word in [
        "ram",
        "memory",
    ]):
        try:
            data["memory"] = memory_usage()
        except Exception as error:
            print(f"[ZEK] Memory tool failed: {error}")

    # Storage
    if any(word in msg for word in [
        "storage",
        "disk",
        "free space",
    ]):
        try:
            data["storage"] = storage_usage()
        except Exception as error:
            print(f"[ZEK] Storage tool failed: {error}")

    # Uptime
    if any(word in msg for word in [
        "uptime",
        "running time",
    ]):
        try:
            data["uptime"] = uptime()
        except Exception as error:
            print(f"[ZEK] Uptime tool failed: {error}")

    # Internet
    if any(word in msg for word in [
        "internet",
        "network",
        "wifi",
        "wi-fi",
        "connection",
    ]):
        try:
            data["internet"] = internet_status()
        except Exception as error:
            print(f"[ZEK] Internet tool failed: {error}")

    # Battery
    if any(word in msg for word in [
        "battery",
        "charge",
        "charging",
        "temperature",
        "temp",
        "heat",
        "hot",
    ]):
        try:
            data["battery"] = battery_status()
        except Exception as error:
            print(f"[ZEK] Battery tool failed: {error}")

    return data if data else None


# ============================================================
# MAIN ZEK CHAT
# ============================================================

def chat(message: str):

    message = message.strip()

    if not message:
        return "Please enter a message."

    # --------------------------------------------------------
    # 1. BUILD ZEK AI CONTEXT
    # --------------------------------------------------------

    messages = build_context(message)

    # --------------------------------------------------------
    # 2. COLLECT LIVE SERVER DATA IF RELEVANT
    # --------------------------------------------------------

    live_data = get_live_context(message)

    if live_data:

        live_message = {
            "role": "system",
            "content": (
                "LIVE DATA FROM THE ZEK HOME SERVER:\n"
                f"{live_data}\n\n"
                "Use this information if it is relevant to the "
                "user's question.\n"
                "Explain the information naturally as ZEK.\n"
                "Do not dump raw dictionaries unless explicitly asked.\n"
                "Do not invent missing values.\n"
                "This data is current live telemetry from the server."
            ),
        }

        # Insert before the latest user message
        insert_position = max(
            len(messages) - 1,
            1,
        )

        messages.insert(
            insert_position,
            live_message,
        )

    # --------------------------------------------------------
    # 3. SEND EVERYTHING TO QWEN
    # --------------------------------------------------------

    try:

        response = requests.post(
            f"{LLAMA_SERVER_URL}/v1/chat/completions",

            json={
                "messages": messages,

                # Enough for natural answers while keeping
                # generation manageable on the Galaxy M12.
                "max_tokens": 120,

                "temperature": 0.5,

                "top_p": 0.9,

                "stream": False,
            },

            timeout=REQUEST_TIMEOUT,
        )

        response.raise_for_status()

        data = response.json()

        choices = data.get(
            "choices",
            [],
        )

        if not choices:

            return (
                "I couldn't generate a response."
            )

        content = (
            choices[0]
            .get("message", {})
            .get("content", "")
            .strip()
        )

        if not content:

            return (
                "I couldn't generate a response."
            )

        return content

    # --------------------------------------------------------
    # TIMEOUT
    # --------------------------------------------------------

    except requests.exceptions.Timeout:

        print(
            "[ZEK] Qwen request timed out."
        )

        return (
            "My local AI model took too long to respond. "
            "Please try again."
        )

    # --------------------------------------------------------
    # CONNECTION ERROR
    # --------------------------------------------------------

    except requests.exceptions.ConnectionError:

        print(
            "[ZEK] Cannot connect to llama.cpp."
        )

        return (
            "I can't reach my local AI model right now. "
            "Check that the llama.cpp server is running."
        )

    # --------------------------------------------------------
    # HTTP / REQUEST ERROR
    # --------------------------------------------------------

    except requests.exceptions.RequestException as error:

        print(
            f"[ZEK] LLM request error: {error}"
        )

        return (
            "I encountered an error while communicating "
            "with my local AI model."
        )

    # --------------------------------------------------------
    # UNKNOWN ERROR
    # --------------------------------------------------------

    except Exception as error:

        print(
            f"[ZEK] Unexpected AI error: {error}"
        )

        return (
            "I encountered an unexpected error."
        )
