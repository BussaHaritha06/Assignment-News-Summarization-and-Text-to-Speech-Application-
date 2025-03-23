import requests
from bs4 import BeautifulSoup

def fetch_news(company_name):
    search_url = f"https://news.google.com/search?q={company_name}&hl=en"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    articles = []
    for item in soup.find_all("article")[:10]:  # Limit to 10 articles
        title = item.find("h3").text if item.find("h3") else "No Title"
        link = item.find("a")["href"] if item.find("a") else "#"
        summary = item.find("p").text if item.find("p") else "No Summary"
        
        articles.append({"title": title, "summary": summary, "link": link})

    return articles
