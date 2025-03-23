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

"https://news.google.com/search?q={company_name}&hl=en

"http://127.0.0.1:5000/fetch_news?company={company_name}"



## Acknowledgment
- Project developed as part of **upGrad** coursework.

## Contributors
- **Bussa Haritha**



