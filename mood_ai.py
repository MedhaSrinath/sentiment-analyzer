from textblob import TextBlob

print("Mood AI Assistant 🤖")
print("Type 'exit' to stop\n")

while True:
    text = input("Tell me about your day: ")

    if text.lower() == "exit":
        print("Goodbye! Take care! 👋")
        break

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

    print(f"Mood detected: {mood} ({intensity})")

    if mood == "happy":
        if intensity == "strong":
            print("You're glowing today! Keep that energy going ✨🔥")
        else:
            print("Nice! Glad things are going well 🙂")

    elif mood == "sad":
        if intensity == "strong":
            print("That sounds really tough 💙 Take a deep breath, you're not alone.")
        else:
            print("Hope things get better soon 🌿")

    elif mood == "angry":
        print("I can feel that intensity 😤 Try pausing for a moment and breathe.")

    elif mood == "stressed":
        print("You're carrying a lot. Maybe step away and reset a bit ☕")

    else:
        print("Steady and calm 😌 Hope your day stays balanced.")

    print()