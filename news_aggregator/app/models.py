from sqlalchemy import Column, Integer, String, Text, DateTime, Float
from .database import Base
from datetime import datetime

class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(300))
    description = Column(Text)
    source = Column(String(100))
    published_at = Column(DateTime, default=datetime.utcnow)
    content = Column(Text)
    sentiment = Column(String(20))
    sentiment_score = Column(Float)
    keywords = Column(Text)
