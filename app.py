import streamlit as st
import pickle

# Load model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Title
st.title("📰 Fake News Detection App")

st.write("Enter a news article below and check whether it is Fake or Real.")

# User Input
news = st.text_area("Enter News Text")

if st.button("Check News"):

    if news.strip() == "":
        st.warning("Please enter some news text.")
    else:
        news_vector = vectorizer.transform([news])

        prediction = model.predict(news_vector)

        if prediction[0] == 0:
            st.error("🚨 Fake News")
        else:
            st.success("✅ Real News")