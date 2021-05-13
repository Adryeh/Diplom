from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

with open('data/users.json') as json_file:
    users = json.load(json_file)


companies = []

vacancies = [
    {
        'id': 0,
        'summary': 'Junior Python Developer',
        'payment': '10.000',
        'currency': 'RUB',
        'requirements': 'Python, SQL, WEB, Django, Flask',
        'company': 'RosNoU',
        'description': 'Looking for developer'
    }
]


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/users', methods=['GET'])
@cross_origin()
def users_list():
    response = jsonify(message=users)
    # response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route('/user/<int:id>', methods=['GET'])
@cross_origin()
def user_by_id(id):

    user = [user for user in users if user['id'] == id][0]
    response = jsonify(message=user)
    # response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/vacancy', methods=['GET'])
def vacancy():
    return jsonify(vacancies)

if __name__ == '__main__':
    app.run()
