import requests
from datetime import datetime

def fetch_news(api_key="474afe61653b4611bed72f3b679e47e1"):
    """
    Fetches top headlines from NewsAPI.org.
    Falls back to mock data if API call fails or returns no results.
    """
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"

    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            articles = response.json().get("articles", [])
        else:
            print(f"API request failed with status code: {response.status_code}")
            articles = []

        # Fallback to mock data if API returns nothing
        if not articles:
            articles = [
                {
                    "title": "AI transforms industry",
                    "description": "AI impacts daily life",
                    "source": {"name": "TechCrunch"},
                    "publishedAt": str(datetime.utcnow()),
                    "content": "Artificial intelligence is booming."
                },
                {
                    "title": "Stock markets rise",
                    "description": "Markets surge after policy news",
                    "source": {"name": "Reuters"},
                    "publishedAt": str(datetime.utcnow()),
                    "content": "Investors are optimistic today."
                },
            ]

        return articles

    except Exception as e:
        print(f"Error fetching news: {e}")
        # Fallback to mock data if exception occurs
        return [
            {
                "title": "AI transforms industry",
                "description": "AI impacts daily life",
                "source": {"name": "TechCrunch"},
                "publishedAt": str(datetime.utcnow()),
                "content": "Artificial intelligence is booming."
            },
            {
                "title": "Stock markets rise",
                "description": "Markets surge after policy news",
                "source": {"name": "Reuters"},
                "publishedAt": str(datetime.utcnow()),
                "content": "Investors are optimistic today."
            },
        ]
