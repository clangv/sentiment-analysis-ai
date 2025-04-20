import feedparser

# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-classification", model="ProsusAI/finbert")

print(pipe('Stocks rallied and the British pound gained.'))
