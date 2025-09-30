%% HBnB - 3 Layer Architecture with Facade
```mermaid
classDiagram
    %% --- Packages ---
    class PresentationLayer {
        <<Package>>
        +API Endpoints
        +Services (User, Place...)
    }

    class BusinessLogicLayer {
        <<Package>>
        +User
        +Place
        +Review
        +Amenity
        +Facade
    }

    class PersistenceLayer {
        <<Package>>
        +Repositories (User, Place...)
        +Database Access
    }

    %% --- Relations ---
    PresentationLayer --> BusinessLogicLayer : via Facade
    BusinessLogicLayer --> PersistenceLayer : Database Operations
```
