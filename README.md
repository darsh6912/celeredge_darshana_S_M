# 📰 CelerEdge News Aggregator and Insights Platform

This project is a **FastAPI + JavaScript** based system that aggregates news articles, performs **sentiment analysis**, identifies **top topics**, and compares **news sources**.  
It also includes a **frontend dashboard** visualizing insights using **Chart.js**.

---

## 🏗️ Architecture Overview

### Components

1. **Backend (FastAPI)**  
   - Fetches latest or searched news articles using APIs (like NewsAPI).  
   - Analyzes sentiments using VADER sentiment analyzer.  
   - Extracts key topics and source statistics.  
   - Exposes REST endpoints consumed by the frontend.

2. **Frontend (HTML + CSS + JS)**  
   - Simple dashboard interface.  
   - Displays fetched articles dynamically.  
   - Uses **Chart.js** to visualize:
     - Sentiment distribution  
     - Top topics  
     - Source comparison  

3. **Database (SQLite via SQLAlchemy)**  
   - Stores fetched articles for caching and faster access.  
   - Ensures data persistence across sessions.

4. **Dockerized Deployment**  
   - Backend and frontend are containerized for consistent setup.  
   - Uses `docker-compose` for easy orchestration.

---

## 🔄 Data Flow

1. User searches for a keyword or loads top headlines.  
2. The **frontend** calls `/api/fetch?query=<keyword>` via `fetch()`.  
3. The **FastAPI backend** retrieves articles → runs **sentiment & topic extraction** → stores them in the DB.  
4. The backend returns a structured JSON response to the frontend.  
5. The **frontend dashboard** updates:
   - Article cards  
   - Sentiment pie chart  
   - Topic and source bar charts  

User → JS Fetch → FastAPI (Processing + DB) → JSON → Charts + UI


---

## ⚙️ Setup and Run Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/news-aggregator.git
cd news-aggregator

2. Create Virtual Environment (Optional)
python -m venv venv
source venv/bin/activate   # On Windows use venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Run the Backend
uvicorn app.main:app --reload


Now your FastAPI backend runs at:
➡️ http://127.0.0.1:8000

5. Open Frontend

Open index.html in your browser (or serve via VSCode Live Server / Nginx container).

📡 API Endpoints
Endpoint	Method	Description
/api/fetch?query=<keyword>	GET	Fetch news articles by keyword or top headlines
/api/topics	GET	Retrieve top extracted topics
/api/sentiment-summary	GET	Return sentiment counts (positive, neutral, negative)
/api/source-stats	GET	Compare number of articles by news source
Example Response
{
  "articles": [
    {
      "title": "AI Revolution in Healthcare",
      "description": "How AI is transforming diagnosis.",
      "url": "https://example.com/ai-healthcare",
      "source": "BBC",
      "sentiment": "positive"
    }
  ]
}


🧠 Future Enhancements

Add --> user accounts for personalized feeds.

Implement--> real-time news updates with WebSockets.

Include -->multi-language sentiment support.

Improve ---> topic modeling using transformer-based NLP models.

🐳 Docker Setup (Quick Run)

Build and Run Containers

docker-compose up --build


Access the Application

Backend → http://127.0.0.1:8000

Frontend → http://127.0.0.1:5500

Stop Containers

docker-compose down
