from textblob import TextBlob

print("Mood AI Assistant 🤖")

text = input("How are you feeling today? ")

blob = TextBlob(text)
polarity = blob.sentiment.polarity

if polarity > 0.3:
    mood = "happy"
elif polarity < -0.3:
    mood = "sad"
else:
    mood = "neutral"

print("Mood detected:", mood)

if mood == "happy":
    print("That's amazing! Keep enjoying your day ✨")
if mood == "sad":
    print("I'm sorry you're feeling this way 💙 Maybe take a break or talk to someone.")
else:
    print("Hope your day gets even better! 🌿")
    
print("Polarity:",polarity)