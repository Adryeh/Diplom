from flask import Flask, jsonify
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


users = [
    {
        'id': 0,
        'name': 'Andrew',
        'role': 'Employee'
    },
    {
        'id': 1,
        'name': 'Ivan',
        'role': 'Worker'
    }
]

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


@app.route('/user', methods=['GET'])
@cross_origin()
def user():
    response = jsonify(message=users)
    # response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route('/vacancy', methods=['GET'])
def vacancy():
    return jsonify(vacancies)

if __name__ == '__main__':
    app.run()
