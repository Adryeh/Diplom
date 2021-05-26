from os import access
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json


app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:1111@192.168.1.73:5432/diplom"
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class CompanyModel(db.Model):
    __tablename__ = 'company'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    login = db.Column(db.String())

    def __init__(self, name, login):
        self.name = name
        self.login = login

    def __repr__(self):
        return f"<Company {self.name}>"


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())
    user_type = db.Column(db.String())

    def __init__(self, username, password, user_type):
        self.username = username
        self.password = password
        self.user_type = user_type

    def __repr__(self):
        return f"<User {self.username}>"

with open('data/users.json') as json_file:
    users = json.load(json_file)

with open('data/vacancies.json') as json_file:
    vacancies = json.load(json_file)




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


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json(force=True)
    username = data['username']
    password = data['password']
    if not username or not password:
        return jsonify({"msg":"Missing username/password parameter"}), 400

    user = User.get_or_none(User.username == username, User.password == password)

    if user is None:
        return jsonify({'success': False, 'message': 'Bad username or password'}), 401
    
    access_token = create_access_token(identity=username)
    return jsonify({"success": True, "token": access_token}), 200


if __name__ == '__main__':
    app.run()
