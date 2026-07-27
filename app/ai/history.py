"""
ZEK Conversation History
Stores the recent conversation in memory.
"""

MAX_MESSAGES = 8


class ConversationHistory:

    def __init__(self):
        self.messages = []

    def add_user(self, text: str):
        self.messages.append({
            "role": "user",
            "content": text
        })
        self.trim()

    def add_assistant(self, text: str):
        self.messages.append({
            "role": "assistant",
            "content": text
        })
        self.trim()

    def trim(self):
        if len(self.messages) > MAX_MESSAGES:
            self.messages = self.messages[-MAX_MESSAGES:]

    def clear(self):
        self.messages.clear()

    def get(self):
        return self.messages.copy()


# Global history object
history = ConversationHistory()
