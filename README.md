# Assignment-News-Summarization-and-Text-to-Speech-Application-
# News Summarization and Text-to-Speech Application

## Overview
This project is a web-based application that extracts news articles related to a given company, performs sentiment analysis, conducts comparative analysis, and generates a Hindi text-to-speech (TTS) output. The application allows users to enter a company name and receive a structured sentiment report with an audio summary.

## Features
- **News Extraction:** Fetches and displays the title, summary, and metadata of at least 10 news articles related to the input company.
- **Sentiment Analysis:** Determines the sentiment (Positive, Negative, or Neutral) of each article.
- **Comparative Analysis:** Compares sentiment distribution across articles to highlight differences in news coverage.
- **Topic Extraction:** Identifies key topics mentioned in the articles.
- **Text-to-Speech (TTS):** Converts the summarized sentiment report into Hindi speech.
- **User Interface:** A simple web-based interface using Streamlit.
- **API Support:** Backend communication is handled via APIs.
- **Deployment:** Hosted on Hugging Face Spaces.

## Tech Stack
- **Backend:** Flask, BeautifulSoup, NLTK, spaCy, gTTS
- **Frontend:** Streamlit
- **Deployment:** Hugging Face Spaces

## Installation
```bash
# Clone the repository
git clone <repo-link>
cd news-summarization-tts

# Create and activate a virtual environment
python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the Flask API
python app.py

# Start the Streamlit application
streamlit run app.py
```

## API Endpoints
### 1. Fetch News Articles
**Endpoint:**
```
GET /fetch_news?company=<company_name>
```
**Response:**
```json
{
  "title": "Tesla's New Model Breaks Sales Records",
  "summary": "Tesla's latest EV sees record sales in Q3...",
  "sentiment": "Positive",
  "topics": ["Electric Vehicles", "Stock Market"]
}
```

## Deployment
- The application is deployed on **Hugging Face Spaces**: [Deployment Link](#)

## Usage Guide
1. Open the deployed Streamlit application.
2. Enter a company name in the input field.
3. Click **Analyze News** to fetch and analyze news articles.
4. View the sentiment summary and topic analysis.
5. Click the **Listen (Hindi)** button to hear the audio summary.

## Assumptions & Limitations
- Only non-JS-based web pages can be scraped.
- News extraction depends on Google News availability.
- Sentiment analysis is based on VADER, which may not work perfectly for all contexts.

##import requests
from bs4 import BeautifulSoup
from flask import Flask, request, jsonify
from gtts import gTTS
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import spacy
import streamlit as st

nltk.download("vader_lexicon")
sia = SentimentIntensityAnalyzer()
nlp = spacy.load("en_core_web_sm")

app = Flask(__name__)

def fetch_news(company_name):
    search_url = f"https://news.google.com/search?q={company_name}&hl=en"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    articles = []
    for item in soup.find_all("article")[:10]:
        title = item.find("h3").text if item.find("h3") else "No Title"
        link = item.find("a")["href"] if item.find("a") else "#"
        summary = item.find("p").text if item.find("p") else "No Summary"
        articles.append({"title": title, "summary": summary, "link": link})
    
    return articles

def analyze_sentiment(text):
    score = sia.polarity_scores(text)["compound"]
    return "Positive" if score > 0.05 else "Negative" if score < -0.05 else "Neutral"

def extract_topics(text):
    doc = nlp(text)
    return [token.text for token in doc.ents]

def generate_tts(text, filename="output.mp3"):
    tts = gTTS(text=text, lang="hi")
    tts.save(filename)
    return filename

@app.route("/fetch_news", methods=["GET"])
def get_news():
    company = request.args.get("company")
    articles = fetch_news(company)
    
    for article in articles:
        article["sentiment"] = analyze_sentiment(article["summary"])
        article["topics"] = extract_topics(article["summary"])
    
    return jsonify(articles)

if __name__ == "__main__":
    app.run(debug=True)

# Streamlit Web Interface
st.title("📢 News Summarization & Sentiment Analysis")
company_name = st.text_input("Enter Company Name")

if st.button("Analyze News"):
    response = requests.get(f"http://127.0.0.1:5000/fetch_news?company={company_name}")
    news_data = response.json()

    for article in news_data:
        st.subheader(article["title"])
        st.write(article["summary"])
        st.write(f"🗞 Sentiment: {article['sentiment']}")
        st.write(f"📌 Topics: {', '.join(article['topics'])}")
        
        if st.button(f"🔊 Listen (Hindi) - {article['title']}", key=article["title"]):
            tts_file = generate_tts(article["summary"])
            st.audio(tts_file)


## Acknowledgment
- Project developed as part of **upGrad** coursework.

## Contributors
- **Bussa Haritha**



