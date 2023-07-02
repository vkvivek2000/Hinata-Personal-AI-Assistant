import requests

def get_news(NEWS_API):
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        headlines = data['articles'][:10]
        return headlines
    else:
        return None
