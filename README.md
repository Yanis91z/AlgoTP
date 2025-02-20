# Sentiment Analysis API

## Description

L'API d'Analyse de Sentiments permet de classifier des textes en fonction de leur tonalité (positive, négative ou neutre). Elle est conçue pour être déployée facilement et inclut un mécanisme de réentraînement du modèle afin d'améliorer sa précision avec le temps.

## Fonctionnalités

Analyse de sentiments en temps réel via une API REST.

Réentraînement du modèle pour une amélioration continue.

Intégration avec une base de données MySQL pour le stockage des données.

Déploiement via Docker et gestion automatique des dépendances.

## Prérequis

Avant de commencer, assurez-vous d'avoir installé :

- Python 3.x

- Docker

- Git

## Installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/Yanis91z/AlgoTP
   cd sentiment-analysis-api
   ```bash
2. Configurer l'environnement virtuel :
   ```bash
   python3 -m venv env
   source env/bin/activate
   pip install -r requirements.txt
   ```bash
3. Lancer les services avec Docker :
   ```bash
   docker-compose up -d
   ```bash
4. Initialiser la base de données :
   mysql -u root -p sentiment_analysis < init.sql
   exit
   python3 src/insert_tweets.py
   ```bash
5. Démarrer l'application :
   ```bash
   python3 src/app.py
   ```bash
7. Tester l'API :
   ```bash
   curl -X POST http://127.0.0.1:5000/analyze -H "Content-Type: application/json" -d @tweets.json
   ```bash
8. Réentraînement du Modèle :
   ```bash
   python3 src/retrain_model.py
   ```bash
9. Réentraînement du Modèle tous les lundi à 2h :
   ```bash
   crontab -e
   0 2 * * 1 /path/flask-sentiment-analysis/env/bin/python /path/flask-sentiment-analysis/src/retrain_model.py
   taper ":wq" & press enter pour quitter
   ```bash
