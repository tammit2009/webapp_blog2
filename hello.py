from flask import Flask, render_template

# Create a flask instance
app = Flask(__name__)

# Create a route decorator
# @app.route('/')
# def index():
#     return "<h1>Hello World!</h1>"

'''
Jinja Filters:
--------------
safe: avoiding injecting code when passing html is required by the developer
capitalize
lower
upper
title: capitalize every first letter in every word
trim: remove trailing spaces if necessary
striptags: strips any html tags passed by users which can inject malicious code e.g. javascript
'''

@app.route('/')
def index():
    first_name = "John"
    stuff = "This is <strong>Bold</strong> Text"
    favorite_pizza = ["Pepperoni", "Cheese", "Mushrooms", 41]
    return render_template('index.html', 
                           first_name=first_name,
                           stuff=stuff,
                           favorite_pizza=favorite_pizza)

# localhost:5000/user/John
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', username=name)

# Custom error pages
# - Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# - Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500
