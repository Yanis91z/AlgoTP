import mysql.connector
import random

def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",  # Utiliser localhost car le script est exécuté en dehors du conteneur Docker
        user="user",
        password="password",
        database="sentiment_analysis"
    )
    return connection

def insert_tweets(tweets):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    for tweet in tweets:
        positive = 1 if tweet['sentiment'] == 'positive' else 0
        negative = 1 if tweet['sentiment'] == 'negative' else 0
        cursor.execute(
            "INSERT INTO tweets (text, positive, negative) VALUES (%s, %s, %s)",
            (tweet['text'], positive, negative)
        )
    
    connection.commit()
    cursor.close()
    connection.close()

def generate_sample_tweets(n):
    sample_tweets = []
    for _ in range(n):
        sentiment = random.choice(['positive', 'negative'])
        text = f"This is a {sentiment} tweet."
        sample_tweets.append({'text': text, 'sentiment': sentiment})
    return sample_tweets

if __name__ == "__main__":
    tweets = generate_sample_tweets(1000)  # Générer 1000 tweets
    insert_tweets(tweets)