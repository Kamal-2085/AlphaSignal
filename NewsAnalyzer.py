from serpapi import GoogleSearch
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import numpy as np

nltk.download("vader_lexicon")

# -----------------------------
# SERP API KEY
# -----------------------------

SERP_API_KEY = "634d579412ea5ba702d111093b7d128bc38174537cd09a5dd209ddf9576a7c7b"

# -----------------------------
# Company name
# -----------------------------

company = "Adani Enterprises"

# -----------------------------
# Fetch News from Google
# -----------------------------

params = {
    "engine": "google_news",
    "q": company,
    "api_key": SERP_API_KEY,
    "num": 5
}

search = GoogleSearch(params)

results = search.get_dict()

news_results = results.get("news_results", [])

# -----------------------------
# Extract headlines
# -----------------------------

headlines = []

for article in news_results[:5]:
    headlines.append(article["title"])

print("\nLatest News Headlines:\n")

for h in headlines:
    print("-", h)

# -----------------------------
# Sentiment Analysis
# -----------------------------

sia = SentimentIntensityAnalyzer()

scores = []

for headline in headlines:

    sentiment = sia.polarity_scores(headline)

    scores.append(sentiment["compound"])

# -----------------------------
# Calculate Score
# -----------------------------

avg_sentiment = np.mean(scores)

# Convert [-1,1] → [1,10]
news_score = (avg_sentiment + 1) * 4.5 + 1

news_score = max(1, min(10, news_score))

print("\nNews Analyzer Score (1-10):", round(news_score,2))