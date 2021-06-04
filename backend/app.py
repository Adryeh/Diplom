from enum import unique
from os import access, name
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, get_jwt_identity, JWTManager, get_jwt)
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, current
from passlib.hash import pbkdf2_sha256 as sha256
import json

from sqlalchemy.orm import backref, relationship


app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:1111@192.168.1.73:5432/diplom"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'



db = SQLAlchemy(app)

app.config['JWT_SECRET_KEY'] = 'Super_Secret_JWT_KEY'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = False



jwt = JWTManager(app)

app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
migrate = Migrate(app, db)


@app.before_first_request
def create_tables():
    db.create_all()


class RevokedTokenModel(db.Model):
    __tablename__ = 'revoked_tokens'
    id = db.Column(db.Integer, primary_key = True)
    jti = db.Column(db.String(120))
    
    def add(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def is_jti_blacklisted(cls, jti):
        query = cls.query.filter_by(jti = jti).first()
        return bool(query)

##
# class Skill(db.Model):
#     __tabelname__ = 'skill'

#     id = db.Column(db.Integer, primary_key = True)
#     name = db.Column(db.String)


# class UserSkill(db.Model):
#     __tablename__ = 'employee_skill'

#     employee_id = db.Column(db.Integer(), db.ForeignKey('employee.id'))
#     skill_id = db.Column(db.Integer(), db.ForeignKey('skill.id'))


# class Position(db.Model):
#     __tablename__ = 'position'

#     id = db.Column(db.Integer, primary_key = True)
#     name = db.Column(db.String)


# class Company(db.Model):
#     __tablename__= 'company'

#     id = db.Column(db.Integer, primary_key = True)
#     name = db.Column(db.String)
#     description = db.Column(db.String)


# # class Employee(db.Model):
# #     __tablename__ = 'employee'

# #     id = db.Column(db.Integer, primary_key = True)
# #     first_name = db.Column(db.String)
# #     last_name = db.Column(db.String)
# #     gender = db.Column(db.String)
# ##

   


class CV(db.Model):
    __tablename__ = "cv"

    id = db.Column(db.Integer(), primary_key=True)
    employee_id = db.Column(db.Integer(), db.ForeignKey('employee.id'))
    description = db.Column(db.String())
    skills = db.Column(db.String())


class Vacancy(db.Model):
    __tablename__ = "vacancy"

    id = db.Column(db.Integer(), primary_key=True)
    company_id = db.Column(db.Integer(), db.ForeignKey('company.id'))
    name = db.Column(db.String())
    requirements = db.Column(db.String())
    salary = db.Column(db.String())


class Employee(db.Model):
    __tablename__ = 'employee'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    education = db.Column(db.String)
    gender = db.Column(db.String)
    age = db.Column(db.Integer)
    citizenship =  db.Column(db.String)


class Company(db.Model):
    __tablename__ = 'company'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    name = db.Column(db.String)
    location = db.Column(db.String)
    number_of_employees = db.Column(db.Integer)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), unique=True)
    password = db.Column(db.String())
    email = db.Column(db.String)
    # user_type = db.Column(db.String)
    # email = db.Column(db.String())
    # first_name = db.Column(db.String())
    # second_name = db.Column(db.String())
    # education = db.Column(db.String())
    # gender = db.Column(db.String())
    # age = db.Column(db.Integer())
    # citizenship = db.Column(db.String())

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f"<User {self.username}>"

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @property
    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email 
        }

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def return_all(cls):
        def to_json(x):
            return {
                'username': x.username,
                'password': x.password
            }
        return {'users': list(map(lambda x: to_json(x), User.query.all()))}

    @classmethod
    def delete_all(cls):
        try:
            num_rows_deleted = db.session.query(cls).delete()
            db.session.commit()
            return {'message': '{} row(s) deleted'.format(num_rows_deleted)}
        except:
            return {'message': 'Something went wrong'}

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)


with open('data/users.json') as json_file:
    users = json.load(json_file)

with open('data/vacancies.json') as json_file:
    vacancies = json.load(json_file)


# @jwt.user_identity_loader
# def user_identity_lookup(user):
#     print(user)
#     return user.id


# @jwt.user_lookup_loader
# def user_lookup_callback(_jwt_header, jwt_data):
#     identity = jwt_data["sub"]
#     return User.query.filter_by(id=identity).one_or_none()




@jwt.token_in_blocklist_loader
def check_if_token_in_blacklist(jwt_header, decrypted_token):
    jti = decrypted_token['jti']
    return RevokedTokenModel.is_jti_blacklisted(jti)


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/whoami', methods=["GET"])
@jwt_required()
def whoami():
    return jsonify(
        id=current_user.id,
        username=current_user.username
    )

@app.route('/users', methods=['GET', 'DELETE'])
@cross_origin()
def users_list():
    # response = jsonify(message=users)
    # # response.headers.add("Access-Control-Allow-Origin", "*")
    # return response
    if request.method == 'GET':
        return User.return_all()
    elif request.method == 'DELETE':
        return User.delete_all()


@app.route('/user/<int:id>', methods=['GET'])
@cross_origin()
def user_by_id(id):

    user = [user for user in users if user['id'] == id][0]
    response = jsonify(message=user)
    # response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/vacancy', methods=['GET'])
@jwt_required()
def vacancy():
    return jsonify(vacancies)


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    print("debug register data income", data)
    if User.find_by_username(data['username']):
        return {'message': 'User {} already exists'.format(data['username'])}

    new_user = User(
        username=data['username'],
        password=User.generate_hash(data['password']),
        
    )

    try:
        new_user.save_to_db()
        access_token = create_access_token(identity=data['username'])
        refresh_token = create_refresh_token(identity=data['username'])
        return jsonify({'message': 'User {} was created'.format( data['username']),
        'access_token': access_token, 'refresh_token': refresh_token})
    except:
        return {'message': 'Something went wrong'}, 500


@app.route('/register/company', methods=['POST'])
def register_company():
    company_data = request.get_json()
    print('company data', company_data)
    test = Company.query.filter_by(name=company_data['name']).first()
    print('TEST', test)
    if Company.query.filter_by(name=company_data['name']).first():
        return {'message': 'Company {} already exists'.format(company_data['name'])}
    new_company = Company(
        user_id=company_data['user_id'],
        name=company_data['name'],
        location=company_data['location'],
        number_of_employees=company_data['number_of_employees']
    )

    try:
        new_company.save_to_db()
        return {'message': 'Company {} was created'.format(company_data['name'])}
    except:
        return {'message': 'error'}, 500

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    current_user = User.find_by_username(data['username'])
    if not current_user:
        return {'message': 'User {} doesn\'t exist'.format(data['username'])}, 401

    if User.verify_hash(data['password'], current_user.password):
        access_token = create_access_token(identity = data['username'])
        refresh_token = create_refresh_token(identity = data['username'])
        return {'message': 'Logged in as {}'.format(current_user.username), 'access_token': access_token, 'refresh_token': refresh_token, 'username':current_user.username, 'user_object': current_user.serialize}
    else:
        return {'message': 'Wrong credentials'}, 401


@app.route('/refresh_token', methods=['POST'])
@jwt_required(refresh=True)
def refresh_token():
    current_user = get_jwt_identity()
    access_token = create_access_token(identity=current_user)
    return {'access_token': access_token}


@app.route('/logout/access', methods=['POST'])
@jwt_required
def logout_access():
    jti = get_jwt()['jti']
    try:
        revoked_token = RevokedTokenModel(jti = jti)
        revoked_token.add()
        return {'message': 'Access token has been revoked'}
    except:
        return {'message': 'Something went wrong'}, 500


@app.route('/logout/refresh', methods=['POST'])
@jwt_required(refresh=True)
def logout_refresh():
    jti = get_jwt()['jti']
    try:
        revoked_token = RevokedTokenModel(jti = jti)
        revoked_token.add()
        return {'message': 'Refresh token has been revoked'}
    except:
        return {'message': 'Something went wrong'}, 500

if __name__ == '__main__':
    app.run()
