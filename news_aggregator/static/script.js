const apiBaseUrl = "http://127.0.0.1:8000";
let fetching = false; // Prevent continuous fetching

async function fetchNews(query = "") {
  if (fetching) return; // Stop if already fetching
  fetching = true;

  const container = document.getElementById("newsContainer");
  container.innerHTML = "<p class='loading'>Loading news...</p>";

  try {
    const response = await fetch(`${apiBaseUrl}/api/fetch?query=${encodeURIComponent(query)}`);
    const data = await response.json();

    if (!data.articles || data.articles.length === 0) {
      container.innerHTML = "<p>No news found.</p>";
    } else {
      container.innerHTML = data.articles.map(article => `
        <div class="news-card">
          <img src="${article.urlToImage || 'https://via.placeholder.com/300'}" alt="news image">
          <h3>${article.title}</h3>
          <p>${article.description || ''}</p>
          <a href="${article.url}" target="_blank">Read more</a>
        </div>
      `).join("");

      // 👇 Added: Update charts after displaying news
      updateCharts(data.articles);
    }
  } catch (err) {
    container.innerHTML = "<p>Failed to fetch news. Please check backend.</p>";
    console.error(err);
  } finally {
    fetching = false; // Allow next fetch
  }
}

document.getElementById("searchBtn").addEventListener("click", () => {
  const query = document.getElementById("searchInput").value.trim();
  fetchNews(query);
});

// Load top headlines on page load
window.addEventListener("DOMContentLoaded", () => {
  fetchNews();
});


// -------------------- ADDITIONS BELOW --------------------

// Store chart instances
let sentimentChart, topicChart, sourceChart;

// Simple sentiment analyzer
function analyzeSentiment(text) {
  if (!text) return "Neutral";
  const positiveWords = ["good", "great", "positive", "growth", "happy", "success"];
  const negativeWords = ["bad", "crisis", "decline", "negative", "sad", "fail"];
  text = text.toLowerCase();
  let score = 0;
  positiveWords.forEach(w => { if (text.includes(w)) score++; });
  negativeWords.forEach(w => { if (text.includes(w)) score--; });
  if (score > 0) return "Positive";
  if (score < 0) return "Negative";
  return "Neutral";
}

// Function to update all charts dynamically
function updateCharts(articles) {
  const topics = {};
  const sentiments = { Positive: 0, Negative: 0, Neutral: 0 };
  const sources = {};

  articles.forEach(a => {
    const topic = a.title?.split(" ")[0] || "General";
    topics[topic] = (topics[topic] || 0) + 1;
    const sent = analyzeSentiment(a.description || a.title);
    sentiments[sent]++;
    const source = a.source?.name || "Unknown";
    sources[source] = (sources[source] || 0) + 1;
  });

  const ctxSent = document.getElementById("sentimentChart")?.getContext("2d");
  const ctxTopic = document.getElementById("topicChart")?.getContext("2d");
  const ctxSource = document.getElementById("sourceChart")?.getContext("2d");

  if (!ctxSent || !ctxTopic || !ctxSource) return; // Skip if charts not found

  const sentimentData = {
    labels: Object.keys(sentiments),
    datasets: [{ data: Object.values(sentiments), backgroundColor: ["#4CAF50", "#F44336", "#FFC107"] }]
  };
  const topicData = {
    labels: Object.keys(topics),
    datasets: [{ data: Object.values(topics), backgroundColor: "#2196F3" }]
  };
  const sourceData = {
    labels: Object.keys(sources),
    datasets: [{ data: Object.values(sources), backgroundColor: "#9C27B0" }]
  };

  // Destroy old charts to prevent overlay
  if (sentimentChart) sentimentChart.destroy();
  if (topicChart) topicChart.destroy();
  if (sourceChart) sourceChart.destroy();

  // Draw new charts
  sentimentChart = new Chart(ctxSent, { type: "pie", data: sentimentData });
  topicChart = new Chart(ctxTopic, { type: "bar", data: topicData });
  sourceChart = new Chart(ctxSource, { type: "bar", data: sourceData });
}
