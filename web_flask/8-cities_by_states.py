#!/usr/bin/python3
<<<<<<< HEAD
'''A simple Flask web application.
'''
from flask import Flask, render_template

from models import storage
from models.state import State


app = Flask(__name__)
'''The Flask application instance.'''
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def cities_by_states():
    '''The cities_by_states page.'''
    all_states = list(storage.all(State).values())
    all_states.sort(key=lambda x: x.name)
    for state in all_states:
        state.cities.sort(key=lambda x: x.name)
    ctxt = {
        'states': all_states
    }
    return render_template('8-cities_by_states.html', **ctxt)


@app.teardown_appcontext
def flask_teardown(exc):
    '''The Flask app/request context end event listener.'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
=======
""" a script that starts a Flask app """
from flask import Flask
from flask import render_template
from models import storage, State

app = Flask(__name__)


@app.teardown_appcontext
def remove_session(exception):
    """ After each request, it removes the current SQLAlchemy Session """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def render_state_cities():
    """ displays all states and their cities """
    States = storage.all(State).values()
    return render_template("8-cities_by_states.html", States=States)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
>>>>>>> 02f28de52063466cb84066a65ce3db9b06146bc5
