version: "3"  # Version du format docker-compose

services:  # Définition des services à lancer (conteneurs)

api:  # Service pour l'application Flask (API HBNB)
build: .  # Construire l'image Docker à partir du Dockerfile à la racine du projet
ports:

"5000:5000"  # Map le port 5000 du conteneur au port 5000 de ta machine
environment:  # Variables d'environnement pour le conteneur
FLASK_ENV=development  # Mode développement pour Flask
depends_on:  # Dépendances : l'API ne démarre qu'après la base de données
db

"""db:  # Service pour la base de données MySQL
image: mysql:8.0  # Utilise l'image officielle MySQL version 8.0
environment:  # Variables d'environnement pour MySQL
MYSQL_ROOT_PASSWORD: root  # Mot de passe root pour MySQL
MYSQL_DATABASE: hbnb_dev   # Nom de la base de données à créer automatiquement
ports:
"""

"3306:3306"  # Map le port MySQL du conteneur au port 3306 de la machine
volumes:
db_data:/var/lib/mysql  # Persistance des données dans un volume nommé "db_data"

Déclaration des volumes pour la persistance des données
volumes:
db_data:  # Volume Docker pour stocker les données MySQL de manière persistante