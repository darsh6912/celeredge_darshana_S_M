# 🧠 News Aggregator System

## 📝 Project Overview

The **News Aggregator System** is a **FastAPI-based web application** that automatically fetches, analyzes, and visualizes trending news data from **NewsAPI.org**.  
It integrates **Natural Language Processing (NLP)** for **sentiment analysis** and **keyword extraction**, providing users with meaningful insights through **interactive Chart.js visualizations** on the frontend.

---

## ⚙️ Tech Stack

### 🔹 Backend

- **FastAPI** – Lightweight, asynchronous Python web framework for building RESTful APIs.  
- **SQLAlchemy** – ORM (Object Relational Mapper) for database management.  
- **SQLite** – Local relational database used to store fetched articles.  
- **NLTK (VADER)** – NLP library for sentiment scoring and polarity classification.  
- **Scikit-learn (TF-IDF)** – Used for keyword extraction from text data.  
- **Uvicorn** – ASGI server used to serve the FastAPI app efficiently.

### 🔹 Frontend

- **HTML, CSS, JavaScript** – For building the user interface and enabling interactivity.  
- **Chart.js (CDN)** – Used for creating dynamic visualizations of sentiment, topic, and source analytics.

### 🔹 Deployment / Containerization

- **Docker** – Packages the backend application and its dependencies into a portable container.  
- **Docker Compose** – Defines and manages multiple containers and services in a single configuration.

---

## 🧩 Implementation Details

### 📰 News Fetching

- Fetches **live news articles** from **NewsAPI.org** using the `requests` library.  
- Implements **fallback mock data** to ensure reliability if API limits are reached or an error occurs.

### 💬 Sentiment Analysis

- Utilizes **NLTK’s VADER model** for sentiment polarity scoring.  
- Classifies articles into **Positive**, **Negative**, or **Neutral** categories using compound scores.

### 🏷️ Keyword Extraction

- Implements **TF-IDF Vectorization** (via Scikit-learn) to extract the most relevant terms.  
- Highlights **key phrases** representing the core topics in the news batch.

### 💾 Database Management

- Articles, sentiments, and keywords are stored in **SQLite** through **SQLAlchemy models**.  
- Includes handling for **concurrency issues** by retrying commits when database locks occur.

### 📊 Visualization (Frontend)

- **Chart.js** dynamically updates visual charts in real-time:  
  - Sentiment Distribution  
  - Topic Frequency  
  - Source Breakdown  

### 🔐 CORS Middleware

- Enables **secure communication** between the **FastAPI backend** and the **frontend**, even when hosted on different origins.

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

## 🚀 Advantages

✅ **Automated Workflow** – Fetches, analyzes, and visualizes news without manual intervention.  
✅ **Lightweight & Fast** – Combination of FastAPI and Uvicorn ensures high performance.  
✅ **Interactive Visualization** – Real-time, responsive charts enhance user experience.  
✅ **Portable via Docker** – Runs identically across development, testing, and production environments.  
✅ **Reliable Fallbacks** – Operates smoothly even when API requests fail or limits are reached.

---

## ⚡ Efficiency & Usefulness

### 🕒 Time Efficiency
Automates sentiment and keyword extraction, significantly reducing manual analysis time.

### 📈 Data-Driven Decisions
Ideal for **journalists**, **analysts**, and **policy researchers** to assess **public mood** or **trending topics** quickly.

### 💻 Low Resource Usage
The **SQLite + FastAPI** combination ensures low computational cost, making it optimal for lightweight or prototype projects.

### 🔁 Extendability
Easily scalable to **PostgreSQL**, or integrable with **AI-based summarization** or **topic clustering models** for future enhancements.

---

## 🧩 Summary

> The News Aggregator System combines **data fetching**, **NLP-based analysis**, and **interactive visualization** into a single automated pipeline, delivering a highly efficient, reliable, and insightful platform for real-time news intelligence.

---
