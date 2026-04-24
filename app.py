import html
import streamlit as st
from mood_ai import analyze_mood

st.set_page_config(page_title="Mood AI Assistant", page_icon="🤖", layout="centered")

# 🎨 UI Styling (unchanged)
st.markdown(
    """
    <style>
        .stApp { background: linear-gradient(180deg, #f6f8fb 0%, #eef2f7 100%); }

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

        .msg-row { display: flex; margin: 12px 0; gap: 10px; align-items: flex-end; }
        .msg-row.user { justify-content: flex-end; }
        .msg-row.bot { justify-content: flex-start; }

        .avatar {
            width: 36px; height: 36px; border-radius: 50%;
            display: flex; align-items: center; justify-content: center;
            font-size: 18px;
        }
        .avatar.user { background: #dbeafe; }
        .avatar.bot { background: #ede9fe; }

        .bubble {
            max-width: 72%;
            padding: 12px 14px;
            border-radius: 16px;
            font-size: 15px;
            white-space: pre-wrap;
            word-wrap: break-word;
        }
        .bubble.user {
            background: #2563eb; color: white;
        }
        .bubble.bot {
            background: white; border: 1px solid #e5e7eb;
        }

        .header { text-align: center; margin-bottom: 16px; }
    </style>
    """,
    unsafe_allow_html=True,
)

# 🧠 Initialize memory
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "bot", "text": "Hi! Tell me about your day and I’ll detect your mood."}
    ]

# 💬 Bot response function
def bot_reply(mood, intensity):
    if mood == "happy":
        return "You're glowing today! Keep that energy going ✨🔥" if intensity == "strong" else "Nice! Glad things are going well 🙂"
    if mood == "sad":
        return "That sounds really tough 💙 Take a deep breath, you're not alone." if intensity == "strong" else "Hope things get better soon 🌿"
    if mood == "angry":
        return "I can feel that intensity 😤 Try pausing for a moment and breathe."
    if mood == "stressed":
        return "You're carrying a lot. Maybe step away and reset a bit ☕"
    return "Steady and calm 😌 Hope your day stays balanced."

# 💬 Input
prompt = st.chat_input("Type your message...")

# 🔁 Handle new message
if prompt:
    prompt = prompt.strip()

    if prompt:
        st.session_state.messages.append({"role": "user", "text": prompt})

        mood, intensity = analyze_mood(prompt)

        # Remove "Mood detected: ...", keep only assistant message
        reply = bot_reply(mood, intensity)

        st.session_state.messages.append({"role": "bot", "text": reply})

# 🎨 Render chat
rows = []
for msg in st.session_state.messages:
    role = msg["role"]
    safe_text = html.escape(msg["text"], quote=False).replace("\n", "<br>")
    if role == "user":
        rows.append(f'<div class="msg-row user"><div class="bubble user">{safe_text}</div><div class="avatar user">🧑</div></div>')
    else:
        rows.append(f'<div class="msg-row bot"><div class="avatar bot">🤖</div><div class="bubble bot">{safe_text}</div></div>')

chat_html = f"""<div class="chat-card">
    <div class="header">
        <h1>🤖 Mood AI Assistant</h1>
        <p>Chat style interface</p>
    </div>
    <div class="chat-box">
        {''.join(rows)}
    </div>
</div>"""

# ✅ Correct renderer
st.markdown(chat_html, unsafe_allow_html=True)

