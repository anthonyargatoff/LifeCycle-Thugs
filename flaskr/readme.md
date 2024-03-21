# Flask Application Setup and Management Guide

## Introduction
Welcome to the Flask application setup and management guide. This document will walk you through the necessary steps to install, start, view, and close the Flask application.

## Prerequisites
Before proceeding, ensure you have the following installed:
- Python 3.x
- Pip (Python package manager)

## Installation
1. Clone the repository to your local machine:
git clone <repository_url>

2. setup virtual environment:
initially when you don't have a virtual environment
run this command to create one: python -m venv .venv

3. after/if you have a virtual environment run the following command to activate the virtual environment: on windows: .venv\Scripts\activate, on max/linux: source .venv/bin/activate

4. Install dependencies using pip: pip install -r requirements.txt


## Starting the Application
1. Navigate to the Flask directory if you're not already there.
2. Run the Flask application using the following command: flask --app flaskr run --debug

3. The Flask application should now be running. You should see output similar to:
 Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)



## Viewing the Application
1. Open a web browser.
2. Enter the following URL in the address bar: http://127.0.0.1:5000/

3. Press Enter.
4. The Flask application interface should now be visible in your web browser.

## Closing the Application
To stop the Flask application, follow these steps:
1. Navigate to the terminal where the Flask application is running.
2. Press `CTRL + C`.
3. Confirm the termination if prompted.


