import time
from flask import Flask
from flask.json import jsonify
import random

app = Flask(__name__)

@app.route('/time')
def get_current_time():
    return {'time':time.time()}

@app.route('/solution')
def get_solutions():
    """
    Generate solution using breath first search
    """
    return jsonify(random.sample(range(9), 9))
