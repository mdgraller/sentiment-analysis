import streamlit as st
from sentiment_pipeline.data_loader import load_reviews
from sentiment_pipeline.preprocessor import clean_text
from sentiment_pipeline.analyzer import analyze_sentiment
from sentiment_pipeline.summarizer import summarize_sentiments

st.title("Review Sentiment Analyzer")

uploaded_file = st.file_uploader("Upload a CSV with 'review' column", type=["csv"])
if uploaded_file:
    reviews = load_reviews(uploaded_file)
    cleaned_reviews = [clean_text(r) for r in reviews]
    results = analyze_sentiment(cleaned_reviews)
    summary = summarize_sentiments(results)

    st.write("## Sentiment Summary")
    st.json(summary)

    st.write("## Detailed Results")
    for review, result in zip(reviews, results):
        st.write(f"**Review:** {review}")
        st.write(f"Sentiment: {result['label']} (score: {result['score']:.2f})")
        st.write("---")
