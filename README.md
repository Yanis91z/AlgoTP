# Sentiment Analysis API

## Description

L'API d'Analyse de Sentiments permet de classifier des textes en fonction de leur tonalité (positive, négative ou neutre). Elle est conçue pour être déployée facilement et inclut un mécanisme de réentraînement du modèle afin d'améliorer sa précision avec le temps.

## Fonctionnalités

Analyse de sentiments en temps réel via une API REST.

Réentraînement du modèle pour une amélioration continue.

Intégration avec une base de données MySQL pour le stockage des données.

## Prérequis

Avant de commencer, assurez-vous d'avoir installé :

- Python 3.x

- Docker

- Git

- Pour obtenir votre PATH :
  ```bash
  pwd

## Installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/Yanis91z/AlgoTP
   cd AlgoTP
2. Configurer l'environnement virtuel :
   ```bash
   python3 -m venv env
   source env/bin/activate
   pip install -r requirements.txt
3. Lancer les services avec Docker :
   ```bash
   docker-compose up -d
4. Initialiser la base de données :
   ```bash
   docker exec -i sentiment_analysis_db mysql -u user -ppassword sentiment_analysis < /PATH/AlgoTP/flask-sentiment-analysis/init.sql
   python3 src/insert_tweets.py
5. Démarrer l'application :
   ```bash
   python3 src/app.py
6. Tester l'API (Cette requête permet d'envoyer le fichier tweets.json à l'API pour analyser les sentiments des tweets qu'il contient) :
   
   Dans un autre terminal
   ```bash
   cd AlgoTP
   source env/bin/activate
   curl -X POST http://127.0.0.1:5000/analyze -H "Content-Type: application/json" -d @tweets.json
7. Réentraînement du Modèle (manuel) :
   ```bash
   python3 src/retrain_model.py
8. Réentraînement du Modèle tous les lundi à 2h (automatique) :
   ```bash
   crontab -e
   ```
   Rajouter cette ligne :
   ```bash
   0 2 * * 1 /PATH/AlgoTP/env/bin/python /PATH/AlgoTP/src/retrain_model.py
   ```
   taper :
   ```bash
   :qa
   Appuyer sur Entrer pour quitter
   ```
