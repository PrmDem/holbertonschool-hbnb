# Holberton School HBnB Project

## 1. Introduction

In this document, we'll show and explain the diagrams for our **HBnB** project, which is a clone of AirBnB made in teams of two people at Holberton School.

Our clone will offer the same basic functionalities as AirBnB:
⦁	Creating a user account
⦁	Registering a place and its amenities
⦁	Searching for a place
⦁	Leaving comments

The diagrams included in this document depict the various layers of our architecture and how we use them to get the various functionalities running.

These layers are:

⦁	High-Level package
⦁	Business logic layer
⦁	API interaction flow, which is an ensemble of four diagrams.

Using this document, we will be able to maintain a clear view of how to build our website.


## 2. High-Level Architecture Diagram


<inclure diagramme ici>

*Diagram 2.0*


This diagram presents the *Presentation*, *Business logic*, and *Persistence* layers.<br/>
((petit topo sur comment elles interagissent ?))



#### 2.1 Presentation layer (UI)

This layer handles user interaction and API endpoints.
From it, users can select various services such as searching or booking places as well as writing and posting reviews.

All requests for a service are directed to the facade, which in turn redirects them to (((the proper ?????))).

The presentation layer then displays the response from (((the API???))) to the user.





#### 2.2 Business logic layer (BLL)

This layer processes and analyses data, making it the intermediate between UI and Database.

As such it dictates what operations can be performed on the application: any request from the user is analysed to ensure it follows the business logic and rules. If it does, the BLL will send it to the database, then process the DB's result. After that, the BLL will send said result to the Presentation layer so that it can be displayed.



On HBnB, a User will create an account.

They can then register a Place to lend, or look for one to book.

Each Place has a list of Amenities that it offers to a User.

After staying at a Place, a User can leave a Review.



The Facade is called everytime a user makes a request. It delegates these requests to the appropriate classes that implement the various functionalities.



See Diagram 3.0 in the (Business logic layer)\[!<insert internal link here] for more details.





#### 2.3 Persistence layer (DAL)

Also known as Data Access layer, it is the layer through which the database is accessed, be it for saving or fetching data.

The persistence layer contains repositories with the Objects(((avec ou sans majuscule?))) that populate ((?? le dire de façon moins bizarre jsp)) our application.





### 3\. Business logic layer



<insérer diagramme ici>

*Diagram 3.0*



#### 3.1 BaseModel

The BaseModel class is the parent class for all future Objects: every instance of BaseModel holds a universally unique identifier (UUID), a timestamp for the creation and update of the instance, and a save() method to save our Objects to the database.



Every class explained below is a subclass of BaseModel.



#### 3.2 User

The User class holds several attributes: an e-mail, password, first name, and last name; all of which are mandatory for registration. These attributes are all *strings*. Then there are two optional attributes: places and reviews. Both are of type `list`.

The 'places' list contains the Place or Places owned by the User, which can be created via the method `create\_place()`.

Meanwhile, the 'reviews' list holds the instances of the Review class that the User has submitted. This is handled by the `write\_review()` method.



#### 3.3 Place

A Place Object is owned by a User. It has the following attributes:

* name (str): the name or title of the Place
* description (str): a description of the Place that makes it attractive to other Users
* number\_rooms (int): the total number of rooms in the Place
* max\_guests (int): how many guests can stay in the Place at the same time
* price\_by\_night (float): how much a one-night stay costs in this Place
* city (str): city where the Place is located
* reviews (list): Reviews written about the Place, if any
* amenities (list): amenities the Place offers



Starting from the number of rooms, those attributes can be used to filter a User's search.

The Place class includes two methods: `add\_review()`, so a User who stayed at the Place can share their opinion after their stay; `add\_amenity()` allows the User who owns the Place to add any amenity available, whether it's upon creating the Place listing or adding a new amenity to an already-listed Place.



#### 3.4 Amenity

Amenities are provided by a Place. As we previously saw, they are attached to the Place in a list format.

Each amenity has two attributes: `name`, which is the name of the amenity in string format ("washing machine", "wifi"...), and a `description` which is a string that details the amenity ("Washer/drier of XYZ brand", "Password can be found on the box"...).



#### 3.5 Review

A Review is an Object which the User writes and the Place possesses. It is made of the following attributes:

* text (str): the content of the review itself
* rating (int): the rating granted to the Place by the User who rented it
* author: the User who wrote and submitted the Review
* place: the Place the Review is about



The method edit\_review() allows the User who wrote the Review to edit it should the need arise. Another User cannot edit the Review.



### 4\. Sequence Diagrams for API Calls



This section details the base interaction scenarii between user, API, Business logic layer, and Database.

Each sequence diagram illustrates the path of a call to an API, from the user request to the final response.



#### 4.1 create\_place()



<inclure diagramme ici>

*Diagram 4.1*



**Components:**

* **User** : initiates a request
* **API** : receives and formats the request
* **BusinessLogic** : verifies the validity of the request (mandatory fields, expected types...) and orchestrates the operation
* **Database** : saves the Object instantiated from the Place subclass



**Flow :**

* The User sends a request to `Place`
* The API sends that request to the Business Logic Layer
* After validating the request, the BLL sends it to the Database to save
* The Database sends back a confirmation after saving
* The BLL relays that confirmation to the API
* The API returns a success or failure message to the User


Using the Business Logic layer to control and validate requests guarantees the business rules are followed consistently. Without this centralisation, certain checks could be omitted



#### 4.2 write\_review()



<inclure diagramme ici>

*Diagram 4.2*

This diagram shows the workflow of a 'write\_review()' request.


**Components:**

* **User** : initiates a request
* **API** : receives and formats the request
* **BusinessLogic** : ensures the request follows the business rules
* **Database** : saves the Review 



**Flow :**

* The User sends a write\_review() request
* The API sends that request to the Business Logic Layer
* The BLL validates the data provided with the request (Place exists, the body of the Review doesn't break any rules)
* The data from the request is saved on the Database
* The success or failure response is sent back to the User by DB, through BLL, through API.


As the centralised decision-maker of the app, the Business Logic layer ensures the Review can be associated to (added to the 'reviews' list of) an existing Place.



#### 4.3 search\_place()



<inclure diagramme ici>

*Diagram 4.3*

This diagram shows how a User can search for Places, using various filters.





**Components:**

* **User** : initiates a request
* **API** : receives the request and sends it to the appropriate (????)
* **BusinessLogic** : interprets the research criteria and builds an appropriate request
* **Database** : sends back a list of Places that fit the research criteria



**Flow :**

* The User sends a request `GET /places?filters=...`
* The API sends it to the BLL
* The BLL validates the filters and sends the research to the Database
* The Database returns the corresponding Places
* The BLL (((formats??))) the Database's response
* The API sends the links back to the User



The BLL deals with the research filters to avoid giving the User direct access to the Database. Using the BLL allows for easier rule changes and evolutions in the future.





#### 4.4 User API calls



<insert diagram here>

*Diagram 4.4*

This diagram shows the workflow of a User-oriented request (User creation or update)



**Components:**

* **User** : initiates a request
* **API** : receives the request and sends it to the appropriate (????)
* **BusinessLogic** : validates information
* **Database** : saves or updates the User's data



**Flow :**

* The Uuser sends a request `users`/{id}`.
* The API sends it to the BLL
* The BLL validates the information (email, password, uniqueness)
* The Database saves or updates the user with the new data
* Confirmation of a successful or failed save is sent back to the user via the API


Sensitive data is dealt with appropriately by the BLL, which guarantees 


In summary, these sequence diagrams illustrate the way the various layers collaborate to bring together a functional and reliable web application. This architecture allows for easier maintenance and scalability, which makes it an obvious choice for a project such as this one.