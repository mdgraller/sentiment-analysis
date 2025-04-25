import pandas as pd

def load_reviews(filepath):
    df = pd.read_csv(filepath)
    return df['review'].tolist()
