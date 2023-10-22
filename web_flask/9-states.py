#!/usr/bin/python3
"""doc"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def load_all_cities():
    """ load all State """
    states = storage.all(State)
    states = sorted(states.values(), key=lambda x: x.name)
    return render_template('9-states.html', states=states)


@app.route("/states/<id>", strict_slashes=False)
def load_all_city(id=None):
    """ list of City objects linked to the State """
    states = storage.all(State).values()
    for s in states:
        if s.id == id:
            s.cities.sort(key=lambda x: x.name)
            return render_template('9-states.html', state=s)
    return render_template('9-states.html')


@app.teardown_appcontext
def remove_sql_session(exec):
    """remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
