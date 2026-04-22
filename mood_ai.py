from textblob import TextBlob

def analyze_mood(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    text_lower = text.lower()

    # 🎭 Detect mood with intensity
    if any(word in text_lower for word in ["angry", "mad", "furious"]):
        mood = "angry"
        intensity = "strong"

    elif any(word in text_lower for word in ["tired", "exhausted", "stressed"]):
        mood = "stressed"
        intensity = "moderate"

    elif polarity > 0.6:
        mood = "happy"
        intensity = "strong"

    elif polarity > 0.3:
        mood = "happy"
        intensity = "mild"

    elif polarity < -0.6:
        mood = "sad"
        intensity = "strong"

    elif polarity < -0.3:
        mood = "sad"
        intensity = "mild"

    else:
        mood = "neutral"
        intensity = "neutral"

    return mood, intensity