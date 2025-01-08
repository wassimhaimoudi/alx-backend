#!/usr/bin/env python3
""" A simple flask app
"""


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    """ Displays a hello world message
    """
    return render_template('0-index.html')

if __name__ == "__name__":
    app.run(port, host="0.0.0.0", debug=True)
