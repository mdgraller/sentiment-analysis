from collections import Counter

def summarize_sentiments(results):
    labels = [r['label'] for r in results]
    counts = Counter(labels)
    total = sum(counts.values())
    summary = {label: f"{(count/total)*100:.2f}%" for label, count in counts.items()}
    return summary
