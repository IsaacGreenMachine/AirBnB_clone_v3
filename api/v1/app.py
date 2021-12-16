"""app module for RESTful interface"""
from os import getenv 
from flask import Flask
app = Flask(__name__)
from models import storage
from views import app_views
app.register_blueprint(app_views, url_prefix="/api/v1")

@app.teardown_appcontext
def teardown_db(exception):
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

