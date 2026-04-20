from textblob import TextBlob

print("AI Sentiment Analyzer:")
while True:
    user_input = input("Enter something: ")
    if user_input.lower() == "exit":
        print("Goodbye👋")
        break
        
    blob = TextBlob(user_input)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        print("Positive 😊")
    elif polarity < 0:
        print("Negative 😡")
    else:
        print("Neutral 😐")

    print("Score:", polarity)
        