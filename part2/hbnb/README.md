# HBnB: Implementing Business Layer and API Endpoints

- [HBnB: Implementing Business Layer and API Endpoints](#hbnb-implementing-business-layer-and-api-endpoints)
  - [Context](#context)
  - [How to run](#how-to-run)
  - [Structure](#structure)
    - [hbnb directory](#hbnb-directory)
    - [app subdirectory](#app-subdirectory)
    - [api subdirectory](#api-subdirectory)
      - [v1 subdirectory](#v1-subdirectory)
    - [models subdirectory](#models-subdirectory)
  - [TESTING:](#testing)

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
* the [`run.py`](./run.py) file, which is the entrypoint needed by our `Flask` application.
* the [`config.py`](./config.py) file used for configuring environment variables and application settings.
* the [`requirements.txt`](./requirements.txt) file, which lists the Python packages we used to build our project.
* this README, to shed light on how our app is being built and put together.
  
All these files are necessary not only for us to launch our app, but for anyone else who may want to give it a try. The `requirements` file will be updated as needed.

### app subdirectory
The major subdirectory `app` contains our api endpoints, organised by version. For now, only the `v1` is available.<br/>
Aside from it, `app` hosts our first `__init__.py` file. There will be several of these, as they allow their directory to be treated as an importable package. Every `__init__` file is different, as they all touch on different components of our app.

### api subdirectory
Just like its parent directory `app`, `api` contains one subdirectory and an `__init__` file. This file contains the implementation for the _places_ namespace.

#### v1 subdirectory
As explained in the [app subdirectory](#app-subdirectory) section, our API endpoints are organised by version. The `v1` subdirectory holds the following files:
* [`amenities.py`](./app/api/v1/amenities.py) implements `POST`, `GET`, and `PUT` endpoints for the _amenity_ component.
* [`places.py`](./app/api/v1/places.py) implements `POST`, `GET`, and `PUT` endpoints for the _place_ component.
* [`reviews.py`](./app/api/v1/reviews.py) implements `POST`, `GET`, and `PUT` endpoints for the _review_ component.
* [`users.py`](./app/api/v1/users.py) implements `POST`, `GET`, and `PUT` endpoints for the _user_ component.

### models subdirectory
All core models are within this directory. They implement data validation on the various attributes of the component they are related to.<br/>
The parent class `BaseModel` provides a `UUID`, a `creation date` and an `update date`. Every component has its own class but all of these classes inherit from `BaseModel`, as every instance of a component will have a UUID and creation/update dates.<br/>
* [`amenity.py`](./app/models/amenity.py) allows the instantiation of an Amenity object, adding an attribute `name` (string).
* [`place.py`](./app/models/place.py) allows the instantiation of a Place object. The other Place attributes implemented here are:
  * `title`, `description`, `owner_id` (string)
  * `price`, `latitude`, `longitude` (float, of which only price has to be positive)
  * `amenities`, `reviews` (list)
* [`review.py`](./app/models/review.py) allows the instantiation of a Review object with attributes `text`, `rating`, `place_id` and `user_id`.
* [`user.py`](./app/models/user.py) allows the instantiation of a User object. It further implements User attributes such as:
  * `first_name`, `last_name` (string)
  * `is_admin` (bool, defaults to False)
Relationships between models (one-to-many, many-to-many) are represented as relational attributes such as lists, IDs, or linked objects.<br/>
Constraints (length of names, reviews being linked to a place and a user) are enforced during creation or updates.

## TESTING:
To test these models, run the test script related to each model. For instance, from the hbnb directory:
python3 -m unittest app/tests/user_test.py

Also available are [`amenity_test`](./app/tests/amenity_test.py) and [`place_test`](./app/tests/place_test.py).

We ran tests required by the expected return codes of our app, like 201 - correct output or 400 - Bad Request. For instance, we made sure that a user could only input an email that follows a <[]@[].[]> format, where anything between brackets is alphanumeric or a valid special character (notably a period or an underscore).

We ran our tests in Postman, but should you want to 
Each model class should support the following operations: validation, saving, deletion, conversion to dictionary, etc

Relationship integrity (e.g., a review cannot exist without a place or user) should be enforced through validation rules
            FICHIER: `user.py` <- subclass basemodel, sets up user attr after verif
        SOUS-DOSSIER: `persistence` <- has a in-memo repo for now, a DB later
            FICHIER: `__init__.py`
            FICHIER: `repository.py` <- abstract class; in-memory repository & interface implemented there
        SOUS-DOSSIER: `services` <- where we implement facade
            FICHIER: `__init__.py`
            FICHIER: `facade.py` <- handles business logic such as implementation & interactions between the components
        FICHIER: `__init__.py` <- to treat directory as importable package

