# modules/news.py
import requests

def fetch_news():
    api_key = "38f1554ad7264d52bfa4401b435e404a"
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(url)
    news_data = response.json()
    if news_data['status'] == "ok":
        articles = news_data['articles'][:3]
        headlines = "\n".join([f"{index + 1}. {article['title']}" for index, article in enumerate(articles)])
        return f"Here are the latest headlines:\n{headlines}"
    else:
        return "Sorry, I couldn't fetch the news at this time."