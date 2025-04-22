import feedparser

# Use a pipeline as a high-level helper
from transformers import pipeline
import matplotlib.pyplot as plt 

# Ask the user to input a stock ticker and keyword
ticker = input("Enter the stock ticker (e.g., AAPL for Apple): ").upper()
keyword = input("Enter a keyword related to the company (e.g., 'apple'): ").lower()

# ticker = 'GC=F'
# keyword = 'gold'

pipe = pipeline("text-classification", model="ProsusAI/finbert")

rss_url = f'https://finance.yahoo.com//rss/headline?s={ticker}'

feed = feedparser.parse(rss_url)

total_score = 0
num_article = 0
sentiment_count = {"positive": 0, "neutral": 0, "negative": 0}

print(f"\n🔍 Fetching news for {ticker} containing keyword '{keyword}'...\n")

for i, entry in enumerate (feed.entries):
    if keyword.lower() not in entry.summary.lower():
        continue

    print(f'Title: {entry.title}')
    print(f'Link: {entry.link}')
    print(f'Published: {entry.published}')
    print(f'Summary: {entry.summary}')

    sentiment = pipe(entry.summary)[0]
    label = sentiment['label'].lower()
    score = sentiment['score']

    # print(f'Sentiment {sentiment ["label"]}, Score')
    print(f"Sentiment: {label.capitalize()} ({score:.2f})")
    print('-' * 50)

    sentiment_count[label] =+ 1

    # Score calculation
    if label == 'positive':
        total_score += score
        num_article += 1
    elif label == 'negative':
        total_score -= score
        num_article += 1
# Display overall sentiment
if num_article > 0:
    final_score = total_score / num_article
    overall_sentiment = (
        "Positive" if final_score >= 0.15 else
        "Negative" if final_score <= -0.15 else
        "Neutral"
    )
    print(f"\n Overall Sentiment for {ticker}: {overall_sentiment} ({final_score:.2f})")
else:
    print("\n⚠️ No relevant news articles found with that keyword.")

# 🎨 Plotting the sentiment bar chart
labels = list(sentiment_count.keys())
values = list(sentiment_count.values())

plt.figure(figsize=(8, 5))
plt.bar(labels, values, color=["green", "gray", "red"])
plt.title(f"Sentiment Distribution for {ticker}")
plt.xlabel("Sentiment")
plt.ylabel("Number of Articles")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()