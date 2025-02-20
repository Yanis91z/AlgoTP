from textblob import TextBlob

def analyze_sentiments(tweets):
    sentiment_scores = {}
    for tweet in tweets:
        analysis = TextBlob(tweet)
        score = analysis.sentiment.polarity  # Score entre -1 et 1
        sentiment_scores[tweet] = score

    return sentiment_scores