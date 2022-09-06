from flask import Flask, jsonify, request, Response, json

app = Flask(__name__)


USERS = {}


@app.route('/')
def index():
    return 'Index Page'


@app.route('/users/')
def users():
    resp = jsonify(USERS)
    return resp


@app.route('/users/', methods=['POST'])
def add_user():
    data = json.loads(request.data)
    USERS.update(data)
    return Response(status=201)


@app.route('/users/<string:key>', methods=['PUT'])
def update_user(key):
    if key not in USERS:
        return Response(status=404)
    try:
        data = json.loads(request.data)
        USERS[key] = data
        return Response(status=204)
    except:
        return Response(status=400)


@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    USERS.pop(id)
    return jsonify({'success': 'true'}), 200


@app.route("/users/<username>", methods=['GET'])
def access_users(username):
    if request.method == 'GET':
        user_details = USERS.get(username)
        if user_details:
            return jsonify(user_details)
        else:
            return Response(status=404)


if __name__ == "__main__":
    app.run(debug=True)
