#!/usr/bin/python3
'''Setup our Flask app'''
from os import getenv
from flask import Flask
from models import storage
from api.v1.views import app_views
"""app module for RESTful interface"""
app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(context):
    """closes the storage on teardown"""
    storage.close()


if __name__ == "__main__":
    hostVal = getenv("HBNB_API_HOST")
    if hostVal is None:
        hostVal = '0.0.0.0'
    portVal = getenv("HBNB_API_PORT")
    if getenv("HBNB_API_PORT") is None:
        portVal = '5000'
    app.run(host=hostVal, port=portVal, threaded=True)
