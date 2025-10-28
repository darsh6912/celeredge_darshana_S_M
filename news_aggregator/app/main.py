from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import OperationalError
from .database import Base, engine, get_db
from .models import Article
from .analyzer import analyze_sentiment, extract_keywords
from datetime import datetime
import requests
import time
from fastapi.middleware.cors import CORSMiddleware

# Your NewsAPI key
API_KEY = "474afe61653b4611bed72f3b679e47e1"

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="News Aggregator")

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://127.0.0.1:5500"] if using Live Server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ✅ Helper: Fetch from NewsAPI
def fetch_news(api_key: str, query: str = None):
    if not query or query.strip() == "":
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    else:
        url = f"https://newsapi.org/v2/everything?q={query}&language=en&apiKey={api_key}"

    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return data.get("articles", [])
        else:
            print(f"⚠️ Failed to fetch news: {response.status_code}")
            return []
    except Exception as e:
        print(f"⚠️ Error fetching news: {e}")
        return []


@app.get("/")
def root():
    return {"message": "News Aggregator API running"}


# ✅ Route to fetch, analyze, and store
@app.get("/api/fetch")
def fetch_and_store(query: str = "", db: Session = Depends(get_db)):
    articles = fetch_news(API_KEY, query)
    if not articles:
        return {"message": "No articles found"}

    texts = []

    # Add articles to DB
    for a in articles:
        text = f"{a.get('title', '')} {a.get('description') or ''}"
        sentiment, score = analyze_sentiment(text)

        new_article = Article(
            title=a.get("title"),
            description=a.get("description"),
            source=a.get("source", {}).get("name"),
            published_at=datetime.utcnow(),
            content=a.get("content"),
            sentiment=sentiment,
            sentiment_score=score
        )

        db.add(new_article)
        texts.append(text)

    # ✅ Retry DB commit if locked
    for attempt in range(3):
        try:
            db.commit()
            break
        except OperationalError as e:
            if "database is locked" in str(e):
                print("⚠️ Database locked, retrying...")
                time.sleep(1)
                db.rollback()
            else:
                raise e

    # ✅ Extract and save top keywords (done once)
    keywords = extract_keywords(texts)
    for art in db.query(Article).all():
        art.keywords = ", ".join(keywords)

    # Second commit (with same safety)
    for attempt in range(3):
        try:
            db.commit()
            break
        except OperationalError as e:
            if "database is locked" in str(e):
                print("⚠️ Database locked during keyword update, retrying...")
                time.sleep(1)
                db.rollback()
            else:
                raise e

    return {
        "message": f"{len(articles)} articles fetched and analyzed successfully",
        "keywords": keywords,
        "articles": articles
    }
