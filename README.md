# News Summarization and Text-to-Speech Application

## Overview
This project is a web-based application that extracts news articles related to a given company, performs sentiment analysis, conducts comparative analysis, and generates a Hindi text-to-speech (TTS) output. The application allows users to enter a company name and receive a structured sentiment report with an audio summary.

## Features
- **News Extraction:** Fetches and displays the title, summary, and metadata of at least 10 news articles related to the input company using web scraping.
- **Sentiment Analysis:** Determines the sentiment (Positive, Negative, or Neutral) of each article using NLP techniques.
- **Comparative Analysis:** Compares sentiment distribution across articles to highlight differences in news coverage and trends.
- **Topic Extraction:** Identifies key topics mentioned in the articles using spaCy and NLTK.
- **Text-to-Speech (TTS):** Converts the summarized sentiment report into Hindi speech using gTTS.
- **User Interface:** A simple and interactive web-based interface built using Streamlit.
- **API Support:** Backend communication is handled via Flask-based APIs.
- **Deployment:** Hosted on Hugging Face Spaces for easy accessibility.

## Tech Stack
- **Backend:** Flask, BeautifulSoup, NLTK, spaCy, gTTS
- **Frontend:** Streamlit
- **Deployment:** Hugging Face Spaces, GitHub

## Installation Guide
Follow these steps to set up and run the application locally:
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
python api.py

# Start the Streamlit application
streamlit run app.py
```

## API Endpoints
### 1. Fetch News Articles
**Endpoint:**
```
GET /fetch_news?company=<company_name>
```
**Response Example:**
```json
{
  "articles": [
    {
      "title": "Tesla's New Model Breaks Sales Records",
      "summary": "Tesla's latest EV sees record sales in Q3...",
      "sentiment": "Positive",
      "topics": ["Electric Vehicles", "Stock Market"]
    }
  ]
}
```

### 2. Generate Text-to-Speech (TTS)
**Endpoint:**
```
GET /generate_tts?text=<summary_text>
```
**Response:**
- Returns a Hindi speech audio file.

## Deployment Guide
The application is deployed on **Hugging Face Spaces**:
- **Steps to Deploy on Hugging Face Spaces:**
  1. Create a new Space on Hugging Face.
  2. Choose **Streamlit** as the SDK.
  3. Clone the GitHub repository and push the code.
  4. Set up the `requirements.txt` file.
  5. Deploy and test the application.

## Usage Guide
1. Open the deployed Streamlit application.
2. Enter a company name in the input field.
3. Click **Analyze News** to fetch and analyze news articles.
4. View the sentiment summary, topic analysis, and comparative analysis.
5. Click the **Listen (Hindi)** button to hear the audio summary.

## Assumptions & Limitations
- Only non-JS-based web pages can be scraped effectively.
- News extraction relies on publicly available sources.
- Sentiment analysis is based on VADER, which may not capture complex sentiments accurately.

## Acknowledgment
- Project developed as part of **upGrad** coursework.

## Contributors
- **Bussa Haritha**





