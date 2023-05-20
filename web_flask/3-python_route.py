#!/usr/bin/python3
<<<<<<< HEAD
'''A simple Flask web application.
'''
from flask import Flask


app = Flask(__name__)
'''The Flask application instance.'''
app.url_map.strict_slashes = False


@app.route('/')
def index():
    '''The home page.'''
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    '''The hbnb page.'''
    return 'HBNB'


@app.route('/c/<text>')
def c_page(text):
    '''The c page.'''
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/<text>')
@app.route('/python', defaults={'text': 'is cool'})
def python_page(text):
    '''The python page.'''
    return 'Python {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
=======
""" a script that starts a Flask web application """
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ displays Hello HBNB! """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ displays HBNB """
    return "HBNB"


@app.route('/c/<string:text>', strict_slashes=False)
def c_text(text):
    """ displays c + text """
    return "C %s" % text.replace('_', ' ')


@app.route("/python/", defaults={"text": "is cool"})
@app.route('/python/<string:text>', strict_slashes=False)
def python_text(text):
    """ displays Python + text """
    return "Python %s" % text.replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
>>>>>>> 02f28de52063466cb84066a65ce3db9b06146bc5
