#!/usr/bin/python3
"""doc"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def remove_sql_session(exec):
    """remove the current SQLAlchemy Session"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """get all states from file storage or DB"""
    return render_template('7-states_list.html', states=storage.all(State))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
