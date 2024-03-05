# cosc310-final-project
Final project for the UBC Okanagan COSC 310 Software Engineering

## Milestones Folder
Contains information and deliverables regarding milestone progress.

## Scrum Meetings
Contains information about the scrum meetings and sprint progress.

## Requirements Details
Below are the lists of requirements.

### User Requirements:
- Users will be able to view earthquakes displayed on a map.
- Users will be able to filter the data by selecting options such as date, location, size, etc.
- Users will be able to share their results with others (social media sharing options).
- Users will be able to toggle different map views (such as satellite, terrain, etc).
- Users will be able to log into the system with a username and password.
- Users will be able to view and edit their profile.
-Users will be able to receive custom notifications from the system (such as a new earthquake of certain conditions), as well as removing notifications via phone/email
- Users will be able to view earthquake predictions.

### Functional Requirements:

- The application will get data from the USGS earthquake API, and then store the data within a database so that we can minimize the amount of requests from the API and provide quicker results to our users.
- The application will use the data stored in the database to display the data on a global map interactive map.
- The application will provide input fields so that users may filter the data. This will be done converting user input into a database query.
- The database will store a user’s information such as login, password, and other fields.
- The application will provide social media links that will share queried search results (ex: if a user searches for all earthquakes between Feb 2 and Feb 17 2023, they will be able to share the link so that another user can view the same page and map).
- The application will provide data prediction for future events.
- The system will automatically send custom notifications to the users if the conditions (set by the user) have been met.
- An admin will be able to view and delete users and their notifications (for moderation purposes).
- The system will automatically send out password reset emails for users that have forgotten their password/login.
- The system will display the number of API calls and last time the API was called in an administration page.

### Non-functional Requirements:
- The backend programming will be done in python (flask).
- The system will not display any unnecessary data to other users or administration.
- The system should be able to respond to input and refresh in a few seconds.



## Running the app
- first activate your virtual environment in the terminal: on windows: (.venv\Scripts\activate) on mac: (.venv\bin\activate)
- - if you don't have a virtual environment run the following command: python -m venv .venv (make sure ur in the project directory, in this case you should be in the LifeCycle-Thugs directory)
- then run the following command to download/make sure all required dependencies are there: pip install -r requirements.txt
- finally run this command to startup the flask server: flask --app flaskr run --debug (this will startup the development server)
- then click on the link that the previous command generates and the app will start running in your default browser

- Also if you have the line server extension installed you can just open the __init__.py file and then run the extension and it will open your file directory in your browser, from here navigate to the templates folder and click on any of the html pages to get to the app.