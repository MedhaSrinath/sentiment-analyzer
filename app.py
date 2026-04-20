import streamlit as st
from textblob import TextBlob

st.title("🧠 AI Sentiment Analyzer")

user_input = st.text_area("Enter your text:")

if st.button("Analyze"):
    blob = TextBlob(user_input)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        st.success("Positive 😊")
    elif polarity < 0:
        st.error("Negative 😡")
    else:
        st.info("Neutral 😐")

    st.write("Score:", polarity)