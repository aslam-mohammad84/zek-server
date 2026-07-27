import { useState } from "react";

const API = "";

export default function Chat() {
  const [messages, setMessages] = useState([
    {
      role: "assistant",
      content:
        "Hello. I'm ZEK. I can help you manage and understand your home server.",
    },
  ]);

  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    const text = input.trim();

    if (!text || loading) return;

    const userMessage = {
      role: "user",
      content: text,
    };

    // Add user's message
    setMessages((previous) => [...previous, userMessage]);

    setInput("");
    setLoading(true);

    try {
      const response = await fetch(`${API}/ai/chat`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          message: text,
        }),
      });

      if (!response.ok) {
        throw new Error(`Server returned ${response.status}`);
      }

      const data = await response.json();

      const zekMessage = {
        role: "assistant",
        content:
          data.response ||
          data.reply ||
          data.message ||
          "ZEK returned an empty response.",
      };

      // Add ZEK's response
      setMessages((previous) => [
        ...previous,
        zekMessage,
      ]);
    } catch (error) {
      console.error("ZEK chat error:", error);

      setMessages((previous) => [
        ...previous,
        {
          role: "assistant",
          content:
            "I couldn't connect to the ZEK AI backend. Check that FastAPI and the AI server are running.",
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

  const handleKeyDown = (event) => {
    if (event.key === "Enter" && !event.shiftKey) {
      event.preventDefault();
      sendMessage();
    }
  };

  return (
    <div className="chat-page">

      {/* Header */}
      <div className="chat-header">
        <p className="eyebrow">
          PERSONAL AI HOME SERVER
        </p>

        <h1>ZEK AI</h1>

        <p className="subtitle">
          Talk to your server using natural language.
        </p>
      </div>

      {/* Chat messages */}
      <div className="chat-window">

        {messages.map((message, index) => (
          <div
            key={index}
            className={`chat-message ${message.role}`}
          >
            <span className="chat-role">
              {message.role === "user"
                ? "YOU"
                : "ZEK"}
            </span>

            <p>{message.content}</p>
          </div>
        ))}

        {/* Thinking indicator */}
        {loading && (
          <div className="chat-message assistant">
            <span className="chat-role">
              ZEK
            </span>

            <p>Thinking...</p>
          </div>
        )}

      </div>

      {/* Message input */}
      <div className="chat-input-area">

        <textarea
          value={input}
          onChange={(event) =>
            setInput(event.target.value)
          }
          onKeyDown={handleKeyDown}
          placeholder="Ask ZEK about your server..."
          rows={1}
        />

        <button
          type="button"
          onClick={sendMessage}
          disabled={loading || !input.trim()}
        >
          {loading ? "Thinking..." : "Send"}
        </button>

      </div>

    </div>
  );
}
