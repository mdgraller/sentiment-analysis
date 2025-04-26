from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline
import torch

# Load model and tokenizer
model_name = "cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Create sentiment pipeline
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model=model,
    tokenizer=tokenizer,
    device=0 if torch.cuda.is_available() else -1
)

# Define label mapping
label_mapping = {
    "LABEL_0": "Negative",
    "LABEL_1": "Neutral",
    "LABEL_2": "Positive"
}

def analyze_sentiment(texts):
    raw_results = sentiment_pipeline(texts)
    # Map labels to human-readable form
    mapped_results = []
    for result in raw_results:
        readable_label = label_mapping.get(result['label'], result['label'])
        mapped_results.append({
            'label': readable_label,
            'score': round(result['score'] * 100, 2)
        })
    return mapped_results