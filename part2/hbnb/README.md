# Implementation of Business Logic and API Endpoints
## Context
In this second part of the HBnB project, we created its Project Directory Structure based on the design we developed in part 1. The app will use Python and Flask to implement business logic and API endpoints.<br/>

## Structure
DOSSIER: HBNB <- Contains _EVERYTHING_ ! \o/
    SOUS-DOSSIER: `app`
        SOUS-DOSSIER: `api`
            SOUS-DOSSIER: `v1`
                FICHIER: `__init__.py`
                FICHIER: `amenities.py`
                FICHIER: `places.py`
                FICHIER: `reviews.py`
                FICHIER: `users.py`
            FICHIER: `__init__.py`
        SOUS-DOSSIER: `models`
            FICHIER: `__init__.py`
            FICHIER: `amenity.py`
            FICHIER: `base_model.py`
            FICHIER: `place.py`
            FICHIER: `review.py`
            FICHIER: `user.py`
        SOUS-DOSSIER: `persistence`
            FICHIER: `__init__.py`
            FICHIER: `repository.py`
        SOUS-DOSSIER: `services`
            FICHIER: `__init__.py`
            FICHIER: `facade.py`
        FICHIER: `__init__.py`
    FICHIER: `run.py` <- Launches our app
    FICHIER: `config.py` <- 
    FICHIER: `README.md`
    FICHIER: `requirements.txt`
