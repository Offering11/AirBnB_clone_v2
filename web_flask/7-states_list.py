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


@app.route('/states_list')
def states_list():
    '''The states_list page.'''
    all_states = list(storage.all(State).values())
    all_states.sort(key=lambda x: x.name)
    ctxt = {
        'states': all_states
    }
    return render_template('7-states_list.html', **ctxt)


@app.teardown_appcontext
def flask_teardown(exc):
    '''The Flask app/request context end event listener.'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
=======
""" a script that starts a Flask web """
from flask import Flask
from flask import render_template
from models import storage, State

app = Flask(__name__)


@app.teardown_appcontext
def remove_session(exception):
    """ After each request, it removes the current SQLAlchemy Session """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def render_states():
    """ displays all states """
    States = storage.all(State).values()
    return render_template("7-states_list.html", States=States)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
>>>>>>> 02f28de52063466cb84066a65ce3db9b06146bc5
