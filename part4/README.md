# Part 4 - Simple Web Client
In part 4, we focus on the front-end development of our application using __HTML5__, __CSS3__, and __JavaScript ES6__.<br/>
Based on the back-end services developped in the previous parts, we will design and implement an interactive user interface.

## Objectives
* Develop a user-friendly interface following provided design specifications
* Implement client-side functionality to interact with the back-end API
* Ensure secure and efficient data handling using JavaScript
* Apply modern web development practices to create a dynamic web application

## Tasks Overview
#### 1. Design
With HTML and CSS base files provided, complete the design following specifications where given.<br/>
Pages must be created for _Login_, _List of Places_, _Place Details_, and _Add Review_.<br/>

#### 2. Login
Implement login functionality using the back-end API, storing the JWT token it returns for session management.<br/>

#### 3. List of Places
Implement the main page to display a list of all places if the user is authenticated. If not, they will be redirected to the login page.<br/>
The 'places' data will be fetched from the API. Client-side filtering will be implemented based on country selection.<br/>

#### 4. Place Details
Implement the detailed view of a place, fetching its details from the API using the place ID.<br/>
If the user is authenticated, provide access to the 'add review' form.

#### 5. Add Review
Implement the form to add a review for a place.<br/>
Ensure it is accessible only to authenticated users, redirecting others to the index page.