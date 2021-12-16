#!/usr/bin/python3
from api.v1.views import app_views
import json


@app_views.route('/status')
def okayThen():
    return json.dumps({"status": "OK"})
