from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_sentiment(texts):
    results = sentiment_pipeline(texts)
    return results
