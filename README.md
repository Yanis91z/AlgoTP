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

- Utiliser git bash pour les utilisateurs Windows

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
   ```
   Pour Windows :
   ```bash
   source env/Scripts/activate
   ```
   Sinon :
   ```bash
   source env/bin/activate
   ```
   Ensuite :
   ```bash
   pip install -r requirements.txt
4. Lancer les services avec Docker :
   ```bash
   docker compose up -d
5. Initialiser la base de données :

   Création de la table tweets :
   ```bash
   docker exec -i sentiment_analysis_db mysql -h 127.0.0.1 -u user -ppassword sentiment_analysis < /PATH/AlgoTP/init.sql
   ```
   Création de 1000 tweets :
   ```bash
   python3 src/insert_tweets.py
6. Démarrer l'application (peut être long) :
   ```bash
   python3 src/app.py
7. Tester l'API (Cette requête permet d'envoyer le fichier tweets.json à l'API pour analyser les sentiments des tweets qu'il contient) :
   
   Dans un autre terminal
   ```bash
   cd AlgoTP
   source env/bin/activate
   curl -X POST http://127.0.0.1:5000/analyze -H "Content-Type: application/json" -d @tweets.json
8. Réentraînement du Modèle (manuel) :
   ```bash
   python3 src/retrain_model.py
9. Réentraînement du Modèle tous les lundi à 2h (automatique) pour MacOS & Linux :
   ```bash
   crontab -e
   ```
   Si demandé, utiliser l'éditeur Vim pour suivre les étapes ci-dessous.
   
   Rajouter cette ligne :
   ```bash
   0 2 * * 1 /PATH/AlgoTP/env/bin/python /PATH/AlgoTP/src/retrain_model.py
   ```
   taper :
   ```bash
   :wq
   Puis appuyer sur Entrée pour quitter
   ```
   Si besoin, pour supprimer une ligne il faut se positionner sur la ligne en question et faire :
   ```bash
   dd
   ```
   Sinon vous pouvez utiliser l'éditeur Nano avec les instructions suivantes :
   
   Rajouter cette ligne :
   ```bash
   0 2 * * 1 /PATH/AlgoTP/env/bin/python /PATH/AlgoTP/src/retrain_model.py
   ```
   Pour quitter :
   ```bash
   Ctrl-X
   ```
   Pour visualiser la tâche :
   ```bash
   crontab -l
   
   
