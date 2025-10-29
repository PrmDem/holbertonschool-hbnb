# HBnB Part 3: Enhanced Backend with Authentication and Database Integration

- [HBnB Part 3: Enhanced Backend with Authentication and Database Integration](#hbnb-part-3-enhanced-backend-with-authentication-and-database-integration)
  - [Introduction](#introduction)
  - [Authentication](#authentication)
  - [Admin role](#admin-role)
  - [Implementing database](#implementing-database)


## Introduction
So far we had been using an in-memory repository to act as a database for the sake of testing our code. In Part 3 we are replacing this repository with an `SQLite` database, which would be swapped for a larger, more scalable database once we move to a production environment.<br/>
In addition, we will implement the full __CRUD__ methods in relation to the database. This will allow us, in conjunction with __authentication__ and __admin role__ implementation, to give some users permission to interact with user details or amenities without ownership restrictions.<br/>

## Authentication
In order to implement JWT authentication, we use `flask-jwt-extended`. A solid authentication method is fundamental to ensure user login is secure.<br/>
Here, the API will generate tokens upon login and verify them as users try to access specific endpoints – like those that only admins can access. We make this distinction through the use of decorators `@jwt_required()` and `@jwt_optional()`.<br/>

## Admin role
While regular users should not be allowed to modify any information that doesn't belong to them (email, places and amenities), administrators must be granted that privilege. This is to better moderate descriptions to follow the code of conduct and rules of the website, but also to help users should they have trouble accessing their own info.<br/>

## Implementing database
Starting with a `SQLAlchemyRepository`, we will create the `SQLAlchemyRepository` and integrate it into the project for managing database interactions.

``` mermaid
erDiagram
USER {
int id PK
string first_name
string last_name
string email
string password
string is_admin
}

PLACE {
int id PK
string title
string description
float price
float latitude
float longitude
int owner_id FK
}

REVIEW {
int id PK
string text
int rating
int user_id FK
int place_id FK
}

AMENITY {
int id PK
string name
}

PLACE_AMENITY {
int place_id FK
int amenity_id FK
}

USER ||--o{ PLACE : owns
USER ||--o{ REVIEW : writes
PLACE }o--o{ AMENITY : has
PLACE ||--o{ REVIEW : has
PLACE }o--o{ PLACE_AMENITY : allows
AMENITY }o--o{ PLACE_AMENITY : allows
```