# must use obj.todict?
from sqlalchemy.sql.functions import mode
from api.v1.views import app_views, modelsDict
from models import storage
import flask


@app_views.route('/states', methods=['GET'])
@app_views.route('/states/<id>', methods=['GET'])
def st_get(id=None):
    if id is None:
        return flask.jsonify([ob.to_dict() for ob in storage.all(modelsDict['states']).values()])

    try:
        return flask.jsonify(storage.all()['State.' + id].to_dict())
    except Exception:
        flask.abort(404)


@app_views.route('/states/<id>', methods=['DELETE'])
def st_del(id=None):
    if storage.get("State", id):
        storage.get('State', id).delete()
        storage.save()
        return flask.make_response({}, 200)
    else:
        flask.abort(404)
