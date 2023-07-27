import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download the VADER lexicon and tokenizer from NLTK (do this once)
nltk.download('vader_lexicon')
nltk.download('punkt')

def analyze_sentiment(review):
    sid = SentimentIntensityAnalyzer()
    scores = sid.polarity_scores(review)
    compound_score = scores['compound']

    if compound_score >= 0.05:
        return 'Positive'
    elif compound_score <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

# Sample product reviews
reviews = [
    "I absolutely love this product! It's fantastic.",
    "The quality is terrible. I'm very disappointed.",
    "It's an okay product, nothing special.",
    "This is the worst purchase I've ever made."
]

for review in reviews:
    sentiment = analyze_sentiment(review)
    print(f"Review: '{review}' - Sentiment: {sentiment}")
