# 📰 Fake News Detection using NLP & Machine Learning

An end-to-end **Machine Learning project** that detects whether a news article is **Fake or Real** using **Natural Language Processing (NLP)** techniques.

This project uses **text preprocessing, TF-IDF feature extraction, and a Logistic Regression classifier** to analyze news content and classify its authenticity. The trained model is deployed through an **interactive Streamlit web application**, allowing users to enter news text and receive instant predictions.

---

## 🚀 Live App

🔗 https://fake-news-detection-nlp-slqcjtmqu7xdrbroybezrf.streamlit.app/

---

## 📌 Project Overview

Fake news spreads rapidly through digital media and can mislead readers. This project aims to **automatically classify news articles as Fake or Real** using machine learning.

The system processes news text, extracts meaningful features using **TF-IDF**, and predicts whether the content is authentic or misleading.

---

## ⚙️ Tech Stack

- Python  
- Pandas  
- NumPy  
- NLTK  
- Scikit-learn  
- TF-IDF Vectorizer  
- Logistic Regression  
- Streamlit  

---

## 🔍 Machine Learning Workflow

Dataset  
      ↓  
Text Preprocessing (NLP)  
      ↓  
TF-IDF Feature Extraction  
      ↓  
Train/Test Split  
      ↓  
Logistic Regression Model  
      ↓  
Model Evaluation  
      ↓  
Prediction System  
      ↓  
Streamlit Web Application  

---

## 📊 Model Performance

The model achieves approximately **99% accuracy** on the test dataset.

Evaluation metrics include:

- Accuracy Score  
- Precision  
- Recall  
- F1 Score  
- Confusion Matrix  

---

## 🧪 Example Inputs & Predictions

### Example 1 — Real News

Input

WASHINGTON (Reuters) - The United States government announced new economic reforms aimed at improving employment opportunities and supporting small businesses across the country.

Expected Output

Prediction: Real News  
Confidence Score: ~95–99%

---

### Example 2 — Real News

Input

LONDON (Reuters) - European leaders met on Thursday to discuss new climate policies and international cooperation aimed at reducing carbon emissions and strengthening economic partnerships.

Expected Output

Prediction: Real News  
Confidence Score: ~94–98%

---

### Example 3 — Fake News

Input

Scientists have discovered a secret government experiment proving that humans can teleport instantly using hidden technology discovered beneath the pyramids in Egypt.

Expected Output

Prediction: Fake News  
Confidence Score: ~90–97%

---

### Example 4 — Fake News

Input

Breaking news reveals that a miracle cure has been discovered that allows people to lose 30 kilograms in just two days without exercise or dieting.

Expected Output

Prediction: Fake News  
Confidence Score: ~88–95%

---

## 📂 Project Structure

fake-news-detection-nlp

│

├── app.py

├── requirements.txt

├── model

│ ├── model.pkl

│ └── vectorizer.pkl

├── notebook

│ └── fake_news_detection.ipynb

└── README.md


---

## 📥 Dataset

Dataset used in this project:

Fake and Real News Dataset

https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset

---

## 💻 Installation & Running Locally

### Clone the repository

git clone https://github.com/bhavyasripasileti/fake-news-detection-nlp.git

### Install dependencies

pip install -r requirements.txt

### Run the Streamlit app

streamlit run app.py

### Open in browser

http://localhost:8501

---

## 🌐 Deployment

This project is deployed using **Streamlit Community Cloud**.

Steps:

1. Push the project to GitHub  
2. Connect the repository to Streamlit Cloud  
3. Deploy `app.py`  

---

## 📈 Future Improvements

- Use deep learning models such as **LSTM or BERT**
- Improve prediction for **short news inputs**
- Add **news URL detection**
- Integrate **real-time news APIs**

---

## 👨‍💻 Author

Bhavya Sri Pasileti  

B.Tech Student | AI & Data Science Enthusiast

---

⭐ If you found this project useful, consider giving it a **star on GitHub**!
