from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ✅ SQLite connection URL
DATABASE_URL = "sqlite:///./news.db"

# ✅ Configure engine to reduce lock issues
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False, "timeout": 30},  # wait 30s instead of locking immediately
    pool_pre_ping=True,
    pool_size=1,             # keep only 1 connection at a time (SQLite prefers this)
    max_overflow=0           # don't allow overflow connections
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
