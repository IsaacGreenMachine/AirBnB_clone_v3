#must use obj.todict?
from sqlalchemy.sql.functions import mode
from api.v1.views import app_views, modelsDict
from models import storage
import flask



@app_views.route('/states', methods=['GET'])
@app_views.route('/states/<id>', methods=['GET'])
def routeFn(cls, id=None):
    if id is None:
        return flask.jsonify(storage.all(modelsDict['states']))

    try:
        if cls == 'states':
            cls = "State"
            st = storage.all()[cls + '.' + id]
            return flask.jsonify(st.__dict__)

    except Exception:
        flask.abort(404)

