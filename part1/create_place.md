```mermaid
sequenceDiagram
participant User
participant API
participant BusinessLogic
participant Database

User->>API: POST - API Call (Create Place)
API->>BusinessLogic: POST - Validate and Process Request
BusinessLogic->>Database: POST - Save Place components
Database-->>BusinessLogic: Confirm Save
Database-->>BusinessLogic: Return Amenities
BusinessLogic-->>API: Return Validation
API-->>User: GET - Return Success (201) / Failure (400)
```