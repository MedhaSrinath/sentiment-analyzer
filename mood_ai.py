from textblob import TextBlob

def analyze_mood(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    text_lower = text.lower()

    if any(word in text_lower for word in ["angry", "mad", "furious"]):
        return "angry", "strong"

    elif any(word in text_lower for word in ["tired", "exhausted", "stressed"]):
        return "stressed", "moderate"

    elif polarity > 0.6:
        return "happy", "strong"

    elif polarity > 0.3:
        return "happy", "mild"

    elif polarity < -0.6:
        return "sad", "strong"

    elif polarity < -0.3:
        return "sad", "mild"

    else:
        return "neutral", "neutral"