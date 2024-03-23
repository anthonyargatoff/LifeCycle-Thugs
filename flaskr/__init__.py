# The following code is the sample code setup code given in the flask application setup documentations

import os
import sys

from flask import Flask, render_template, redirect, url_for, request, jsonify


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # root page
    @app.route('/')
    def landing():
        return render_template('index.html')

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    @app.route('/map')
    def map_page():
        return render_template('map.html')
    
    @app.route('/login', methods=['GET', 'POST'])
    def new_login():
        # check for post request
        if request.method == 'POST':
            email = request.form['email']
            pw = request.form['password']
            print(email, pw)
            # need to figure out how to access the remember me checkbox
            # next steps are to incorporate the database and setup credential validation
            # from here redirect to the main page which is search page
            # next steps for the redirect would be to include a payload to dynamically display public user data like their username
            return redirect('/search')
        
        return render_template('login.html')
    
    @app.route('/send_data', methods = ['GET'])
    def send_data():
        return jsonify({'some_data': 'Hello World!'})
    
    @app.route('/search')
    def search():
        return render_template('Search.html')
    
    @app.route('/landing')
    def landing_page():
        return render_template('Landing.html')
    
    @app.route('/admin')
    def admin_page():
        return render_template('Admin.html')
    
    @app.route('/about')
    def about_page():
        return render_template('About.html')
    
    @app.route('/accountmanagement')
    def accountmanager_page():
        return render_template('accountManagement.html')


    return app
