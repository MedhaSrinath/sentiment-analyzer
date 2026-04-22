import html
import streamlit as st
from mood_ai import analyze_mood

st.set_page_config(page_title="Mood AI Assistant", page_icon="🤖", layout="centered")

st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(180deg, #f6f8fb 0%, #eef2f7 100%);
        }

        .chat-card {
            max-width: 820px;
            margin: 0 auto;
            padding: 24px;
            background: white;
            border: 1px solid #e5e7eb;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(15, 23, 42, 0.08);
        }

        .chat-box {
            height: 62vh;
            overflow-y: auto;
            padding: 16px;
            border: 1px solid #e5e7eb;
            border-radius: 16px;
            background: #f8fafc;
        }

        .msg-row {
            display: flex;
            margin: 12px 0;
            gap: 10px;
            align-items: flex-end;
        }

        .msg-row.user {
            justify-content: flex-end;
        }

        .msg-row.bot {
            justify-content: flex-start;
        }

        .avatar {
            width: 36px;
            height: 36px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 18px;
            flex: 0 0 36px;
        }

        .avatar.user {
            background: #dbeafe;
        }

        .avatar.bot {
            background: #ede9fe;
        }

        .bubble {
            max-width: 72%;
            padding: 12px 14px;
            border-radius: 16px;
            line-height: 1.45;
            font-size: 15px;
            white-space: pre-wrap;
            word-wrap: break-word;
        }

        .bubble.user {
            background: #2563eb;
            color: white;
            border-bottom-right-radius: 6px;
        }

        .bubble.bot {
            background: white;
            color: #111827;
            border: 1px solid #e5e7eb;
            border-bottom-left-radius: 6px;
        }

        .header {
            text-align: center;
            margin-bottom: 16px;
        }

        .header h1 {
            margin-bottom: 6px;
        }

        .header p {
            margin-top: 0;
            color: #6b7280;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="chat-card">
        <div class="header">
            <h1>🤖 Mood AI Assistant</h1>
            <p>Chat style interface with a scrollable conversation</p>
        </div>
    """,
    unsafe_allow_html=True,
)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "bot", "text": "Hi! Tell me about your day and I’ll detect your mood."}
    ]

def bot_reply(text: str) -> str:
    mood, intensity = analyze_mood(text)

    if mood == "happy":
        if intensity == "strong":
            return "You're glowing today! Keep that energy going ✨🔥"
        return "Nice! Glad things are going well 🙂"

    if mood == "sad":
        if intensity == "strong":
            return "That sounds really tough 💙 Take a deep breath, you're not alone."
        return "Hope things get better soon 🌿"

    if mood == "angry":
        return "I can feel that intensity 😤 Try pausing for a moment and breathe."

    if mood == "stressed":
        return "You're carrying a lot. Maybe step away and reset a bit ☕"

    return "Steady and calm 😌 Hope your day stays balanced."

prompt = st.chat_input("Type your message and press Enter")

if prompt:
    st.session_state.messages.append({"role": "user", "text": prompt})
    mood, intensity = analyze_mood(prompt)
    st.session_state.messages.append(
        {"role": "bot", "text": f"Mood detected: {mood} ({intensity})\n\n{bot_reply(prompt)}"}
    )

chat_html = '<div class="chat-box">'
for msg in st.session_state.messages:
    role = msg["role"]
    safe_text = html.escape(msg["text"]).replace("\n", "<br>")

    if role == "user":
        chat_html += f"""
        <div class="msg-row user">
            <div class="bubble user">{safe_text}</div>
            <div class="avatar user">🧑</div>
        </div>
        """
    else:
        chat_html += f"""
        <div class="msg-row bot">
            <div class="avatar bot">🤖</div>
            <div class="bubble bot">{safe_text}</div>
        </div>
        """

chat_html += "</div></div>"

st.markdown(chat_html, unsafe_allow_html=True)