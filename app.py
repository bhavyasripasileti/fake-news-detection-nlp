import streamlit as st
import pickle
import re
import nltk
from nltk.corpus import stopwords

# download stopwords if not present
nltk.download('stopwords')

# load model and vectorizer
model = pickle.load(open("model/model.pkl", "rb"))
vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))

stop_words = set(stopwords.words("english"))

# text cleaning function
def clean_text(text):
    text = text.lower()
    text = re.sub('[^a-zA-Z]', ' ', text)
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return " ".join(words)


# ---------------- UI ---------------- #

st.set_page_config(page_title="Fake News Detector", page_icon="📰")

st.title("📰 Fake News Detection App")
st.write(
    "This application uses **Natural Language Processing (NLP)** and "
    "**Machine Learning** to determine whether a news article is **Fake or Real**."
)

st.markdown("---")

news = st.text_area("✍️ Enter News Article Here")

if st.button("🔍 Predict"):

    if news.strip() == "":
        st.warning("Please enter some news text first.")
    else:

        cleaned = clean_text(news)

        vector = vectorizer.transform([cleaned])

        prediction = model.predict(vector)[0]

        probability = model.predict_proba(vector).max()

        st.markdown("---")

        if prediction == 0:
            st.error("⚠️ Prediction: Fake News")
        else:
            st.success("✅ Prediction: Real News")

        st.write(f"Confidence Score: **{probability*100:.2f}%**")

st.markdown("---")
st.caption("Built using NLP, TF-IDF and Logistic Regression")