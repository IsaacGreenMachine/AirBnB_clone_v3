# must use obj.todict?
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


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def st_post():
    new_st = flask.request.get_json()
    if not new_st:
        flask.abort(404, 'Not a JSON')
    if 'name' not in new_st.keys():
        flask.abort(404, 'Missing name')
    st = modelsDict['states'](**new_st)
    storage.new(st)
    storage.save()
    return flask.make_response(st.to_dict(), 200)
