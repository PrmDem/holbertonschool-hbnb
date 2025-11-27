# holbertonschool-hbnb
AirBnB clone project conducted in pairs.<br/>
The required MVP allows a authenticated user to browse a list of places, see a detailed information page about the selected place, as well as read and write reviews.<br/>

## Why HBnB ?
It is the leading project of our second trimester. In order to build this web application we learned to use API, databases, secure authentication, and finally set up a front-end.<br/>This project took us through the basis of app-making, meaning that we can now build up on the skills we learned to create anything we'd like.

## Languages and tools
Our application relies on the following technologies:
* Python as primary programming language
* Flask for RESTful API
* SQLAlchemy and SQLite for the database
* JWT for secure authentication and administrator-specific endpoints
* JavaScript to link our back- and front-ends nicely
* HTML and CSS for the front-end: no templating, no framework

## How to use:
Clone this repository using the `git clone` command on your code editor, then cd to part4. Install the requirements from the .txt file using the command:
```
pip install -r requirements.txt
```
You can then activate the venv that's already here (named `p4_env`) or toss it and create your own.<br/>
From there, cd to the `hbnb` directory. Because the HBnB will look terribly empty without the pre-registered users, comments, and places, use the `hbnb_dump.sql` file to recreate its database:<br/>

```
sqlite3 hbnb_data.db < hbnb_dump.sql
```
Of course you can name the new database whatever you want.<br/><br/>

With this done, you can launch the app using these two commands for the back- and front-end respectively:
```
~/holbertonschool-hbnb/part3/hbnb$ python3 run.py
~/holbertonschool-hbnb/part4/hbnb/front$ python3 -m http.server 5501
```
Make sure to launch the front-end from the `/front` directory. If you don't, you'll have to navigate to it from your browser.<br/>


And you're in!


If you want to look around and leave reviews, you can log in as any ready-made user by entering their email and password in the 'login' page of the website. The passwords are hashed in the database, but they all follow the same format.<br/>
* [first_name] is 4 letters or less: use '[first_name]pass'
* [first_name] is longer than 4 letters: use '[first 4 letters of first_name]pass'.
Passwords are in lowercase. Special cases:
* Admin -> adminpass
* N°234 -> magepass

Obviously, now that you have the database, you can add users, places, and amenities however you like!<br/>
Should you want to keep the Final Fantasy IX theme going, make sure to __check out the credits__ page for links to useful resources. And if you don't care for the theme, please still check out the credits anyway, as my front-end job would have been a lot more difficult without the work of the people listed there!

## What's next?
Future features:
* Page to create a new user
* Page to create a new place
* Buttons to edit reviews (admins can edit all, users can only edit their own)
* User profiles
* Modifying one's own profile, or any if signed in as Admin

## Extras:
* The UML diagrams we created at the beginning of the project are explained in [this pdf](https://drive.google.com/file/d/1ySKytHLdLGM8RetUAj1mNLjp5UdQAaaO/view).

* README for part 2: [Part 2 README](./part2/hbnb/README.md)
* README for part 3: [Part 3 README](./part3/README.md)
* README for part 4: [Part 4 README](./part4/README.md)


### Authors:
Christophe Saniez ([GitHub profile](https://github.com/Saniez-l))<br/>
Priam Demailly (it's me!)