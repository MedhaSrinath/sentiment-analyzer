import streamlit as st
from sentiment import analyze_sentiment

st.title("🧠 AI Sentiment Analyzer")

user_input = st.text_area("Enter your text:")

if user_input:
    result, score = analyze_sentiment(user_input)

    if "Positive" in result:
        st.success(result)
    elif "Negative" in result:
        st.error(result)
    else:
        st.info(result)

    st.write("Score:", score)