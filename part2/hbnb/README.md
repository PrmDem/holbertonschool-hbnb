# HBnB: Implementing Business Layer and API Endpoints

- [HBnB: Implementing Business Layer and API Endpoints](#hbnb-implementing-business-layer-and-api-endpoints)
  - [Context](#context)
  - [How to run](#how-to-run)
  - [Structure](#structure)
    - [hbnb directory](#hbnb-directory)
    - [app subdirectory](#app-subdirectory)
    - [api subdirectory](#api-subdirectory)

## Context
Based on the diagrams we made in part1, we can now implement our business logic layer and our API endpoints. This will be done using __Python__ and __Flask__ (for RESTful API).<br/>
As it is our first time building an application, a structure was provided for the directories and the files they ought to contain. A visual representation and a detailed overview is provided in the following section, [Structure](#structure).<br/>
For the time being, no database has been implemented. It has been replaced by an _in-memory repository_, which will be detailed in the [persistence](#persistence) section of [Structure](#structure).<br/>

## How to run
First, start by cloning the repository using Git clone:
```
git clone git@github.com:PrmDem/holbertonschool-hbnb.git
```
Install the required packages using the requirements file:
```
pip install -r requirements.txt
```
This could lead your code editor to prompt you to create a _virtual environment_, if you haven't already.<br/>
__Make sure to run the app in a venv!__ This way, the packages in our `requirements.txt` file won't encroach on any other project environments you may be using.<br/>

Once your virtual environment is running and all dependencies are installed, you can run the app by simply entering the command `python3 run.py` in your terminal. Enjoy your stay in HBnB !<br/>

## Structure
```
hbnb/
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │       ├── __init__.py
│   │       ├── users.py
│   │       ├── places.py
│   │       ├── reviews.py
│   │       ├── amenities.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── place.py
│   │   ├── review.py
│   │   ├── amenity.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── facade.py
│   ├── persistence/
│       ├── __init__.py
│       ├── repository.py
├── run.py
├── config.py
├── requirements.txt
├── README.md
```
Visual representation of how our directories and files are organised.<br/>

### hbnb directory
It is very obvious that this directory is our main directory and contains the entirety of our code.<br/>
Aside from the `app` subdirectory, `hbnb` contains four files:<br/>
* the [`run.py`](./run.py) file, which is the entrypoint needed by our `Flask` application
* the [`config.py`](./config.py) file used for configuring environment variables and application settings
* the [`requirements.txt`](./requirements.txt) file, which lists the Python packages we used to build our project
* this README, to shed light on how our app is being built and put together
  
All these files are necessary not only for us to launch our app, but for anyone else who may want to give it a try. The `requirements` file will be updated as needed.

### app subdirectory
The major subdirectory `app` contains our api endpoints, organised by version. For now, only the `v1` is available.<br/>
Aside from it, `app` hosts our first `__init__.py` file. There will be several of these, as they allow their directory to be treated as an importable package. Every `__init__` file is different, as they all touch on different components of our app.

### api subdirectory
Just like its parent directory `app`, `api` contains one subdirectory and an `__init__` file.


DOSSIER: HBNB <- Contains _EVERYTHING_ ! \o/
    SOUS-DOSSIER: `app` <- contains our core app code
        SOUS-DOSSIER: `api` <- only contains 1 init.py & api endpoints by version
            SOUS-DOSSIER: `v1` <- contains api files for the four different components
                FICHIER: `__init__.py` 
                FICHIER: `amenities.py` <- handles routes/endpoints for everything amenity-related
                FICHIER: `places.py` <- idem w places
                FICHIER: `reviews.py` <- idem w reviews
                FICHIER: `users.py` <- idem w users
            FICHIER: `__init__.py`
        SOUS-DOSSIER: `models` <- core models w data validation
            FICHIER: `__init__.py`
            FICHIER: `amenity.py` <- subclass of basemodel, sets up amenity name after verif
            FICHIER: `base_model.py` <- attributes shared by all components: UUID, created_at, updated_at
            FICHIER: `place.py` <- subclass basemodel, sets up place attr after verif
            FICHIER: `review.py` <- subclass basemodel, sets up review attr after verif
            FICHIER: `user.py` <- subclass basemodel, sets up user attr after verif
        SOUS-DOSSIER: `persistence` <- has a in-memo repo for now, a DB later
            FICHIER: `__init__.py`
            FICHIER: `repository.py` <- abstract class; in-memory repository & interface implemented there
        SOUS-DOSSIER: `services` <- where we implement facade
            FICHIER: `__init__.py`
            FICHIER: `facade.py` <- handles business logic such as implementation & interactions between the components
        FICHIER: `__init__.py` <- to treat directory as importable package
    FICHIER: `run.py` <- Launches our app
    FICHIER: `config.py` <- used for configuring environment variables and application settings
    FICHIER: `README.md` <- to explain our lil project to the world (za warudo)
    FICHIER: `requirements.txt` <- lists Python packages needed for the project
