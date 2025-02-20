from flask import Flask, request, jsonify
from sentiment_analysis import analyze_sentiments
import mysql.connector
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from textblob import TextBlob
import joblib
import os

app = Flask(__name__)

def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="user",
        password="password",
        database="sentiment_analysis"
    )
    return connection

def fetch_training_data():
    connection = get_db_connection()
    query = "SELECT text, positive, negative FROM tweets"
    df = pd.read_sql(query, connection)
    connection.close()
    return df

def train_model():
    df = fetch_training_data()
    df['sentiment'] = df['positive'] - df['negative']
    X = df['text'].apply(lambda x: TextBlob(x).sentiment.polarity).values.reshape(-1, 1)
    y = df['sentiment']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    # Matrice de confusion pour les prédictions positives
    cm_positive = confusion_matrix(y_test > 0, y_pred > 0)
    print("Confusion Matrix (Positive):\n", cm_positive)
    
    # Matrice de confusion pour les prédictions négatives
    cm_negative = confusion_matrix(y_test < 0, y_pred < 0)
    print("Confusion Matrix (Negative):\n", cm_negative)
    
    # Calcul des métriques de performance
    precision_positive = precision_score(y_test > 0, y_pred > 0)
    recall_positive = recall_score(y_test > 0, y_pred > 0)
    f1_positive = f1_score(y_test > 0, y_pred > 0)
    
    precision_negative = precision_score(y_test < 0, y_pred < 0)
    recall_negative = recall_score(y_test < 0, y_pred < 0)
    f1_negative = f1_score(y_test < 0, y_pred < 0)
    
    print("Performance Metrics (Positive):")
    print("Precision:", precision_positive)
    print("Recall:", recall_positive)
    print("F1 Score:", f1_positive)
    
    print("Performance Metrics (Negative):")
    print("Precision:", precision_negative)
    print("Recall:", recall_negative)
    print("F1 Score:", f1_negative)
    
    # Sauvegarder le modèle entraîné
    joblib.dump(model, 'model.pkl')
    
    return model

def retrain_model():
    global model
    model = train_model()
    print("Model retrained successfully.")

# Charger le modèle au démarrage de l'application
model = joblib.load('model.pkl') if os.path.exists('model.pkl') else train_model()

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    tweets = data.get('tweets', [])
    
    if not isinstance(tweets, list):
        return jsonify({"error": "Invalid input, expected a list of tweets."}), 400
    
    results = analyze_sentiments(tweets)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)