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
app.config['SQLALCHEMY_ECHO'] = True



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


class CV(db.Model):
    __tablename__ = "cv"

    id = db.Column(db.Integer(), primary_key=True)
    employee_id = db.Column(db.Integer(), db.ForeignKey('employee.id'))
    description = db.Column(db.String())
    skills = db.Column(db.String())


class EmployeeFavoriteVcancies(db.Model):
    __tablename__ = "favorite"

    id = db.Column(db.Integer, primary_key=True)
    vacancy_id = db.Column(db.Integer(), db.ForeignKey('vacancy.id'))
    employee_id = db.Column(db.Integer(), db.ForeignKey('employee.id'))

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @property
    def serialize(self):
        return {
            'id': self.id,
            'vacancy_id': self.vacancy_id,
            'employee_id': self.employee_id
        }


class Vacancy(db.Model):
    __tablename__ = "vacancy"

    id = db.Column(db.Integer(), primary_key=True)
    company_id = db.Column(db.Integer(), db.ForeignKey('company.id'))
    name = db.Column(db.String())
    requirements = db.Column(db.String())
    salary = db.Column(db.String())

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @property
    def serialize(self):
        return {
            'id': self.id,
            'company_id': self.company_id,
            'name': self.name,
            'requirements': self.requirements,
            'salary': self.salary
        }

class EmployeeSkill(db.Model):
    __tablename__ = 'employee_skill'

    id = db.Column(db.Integer, primary_key=True)
    skill_name = db.Column(db.String)
    skill_progress = db.Column(db.Integer)
    employee_id = employee_id = db.Column(db.Integer(), db.ForeignKey('employee.id'))

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @property
    def serialize(self):
        return {
            'id': self.id,
            'skill_name': self.skill_name,
            'skill_progress': self.skill_progress,
            'employee_id': self.employee_id
        }


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
    position =  db.Column(db.String)
    web_site = db.Column(db.String)
    github = db.Column(db.String)
    facebook = db.Column(db.String)
    about = db.Column(db.String)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'education': self.education,
            'gender': self.gender,
            'age': self.age,
            'citizenship': self.citizenship,
            'position': self.position,
            'web_site': self.web_site,
            'github': self.github,
            'facebook': self.facebook
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class Company(db.Model):
    __tablename__ = 'company'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    name = db.Column(db.String)
    location = db.Column(db.String)
    number_of_employees = db.Column(db.Integer)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'name': self.name,
            'location': self.location,
            'number_of_employees': self.number_of_employees
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), unique=True)
    password = db.Column(db.String())
    email = db.Column(db.String)

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

@app.route('/employee', methods=['GET', 'POST'])
@cross_origin()
# @jwt_required()
def employee():
    if request.method == 'GET':
        employee_list = Employee.query.all()
        print([emp.serialize for emp in employee_list])
        return jsonify([emp.serialize for emp in employee_list])
    elif request.method == 'POST':
        employee_data = request.get_json()
        print('TYPE1', type(employee_data))
        print('EMPLOYEE DATA', employee_data)
        if Employee.query.filter_by(user_id=employee_data['user_id']).first():
            return {'message': 'Employee {} already exists'.format(employee_data['first_name'])}
        new_employee = Employee(
            user_id=employee_data['user_id'],
            first_name=employee_data['first_name'],
            last_name=employee_data['last_name'],
            education=employee_data['education'],
            gender=employee_data['gender'],
            age=employee_data['age'],
            citizenship=employee_data['citizenship'],
            position=employee_data['position']
        )
        print('NEW EMPLOYEE', new_employee.first_name)
        try:
            new_employee.save_to_db()
            return {'message': 'Employee {} was created'.format(new_employee.first_name)}, 200
        except Exception as e:
            print(e)
            return {'message': 'error'}, 500


@app.route('/user/<int:id>', methods=['GET'])
@cross_origin()
def user_by_id(id):

    user = [user for user in users if user['id'] == id][0]
    response = jsonify(message=user)
    # response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/vacancy', methods=['GET', 'POST'])
@jwt_required()
def vacancy():
    if request.method == 'GET':
        vacancies_list = Vacancy.query.all()
        return jsonify([vacancy.serialize for vacancy in vacancies_list])
    elif request.method == 'POST':
        vacancy_data = request.get_json()
        new_vacancy = Vacancy(
            company_id=vacancy_data['company_id'],
            name=vacancy_data['name'],
            requirements=vacancy_data['requirements'],
            salary=vacancy_data['salary']
        )
        try:
            new_vacancy.save_to_db()
            return {'message': 'Vacancy created'}
        except:
            return {'message': 'Vacancy not created'}


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


@app.route('/skill', methods=['POST', 'GET'])
def skill():
    if request.method == 'GET':
        skills = EmployeeSkill.query.all()
        return jsonify([s.serialize for s in skills])
    elif request.method == 'POST':
        skill_data = request.get_json()
        print('skill_data', skill_data)
        new_skill = EmployeeSkill(
            skill_name=skill_data['skill_name'],
            skill_progress=skill_data['skill_progress'],
            employee_id=skill_data['employee_id']
        )
        try:
            new_skill.save_to_db()
            return {'message': 'Skill created'}
        except:
            return {'message': 'Skill creation error'}, 500


@app.route('/favorite', methods=['POST', 'GET', 'DELETE'])
def favorite():
    if request.method == 'GET':
        favs = EmployeeFavoriteVcancies.query.all()
        return jsonify([f.serialize for f in favs])
    elif request.method == 'POST':
        fav = request.get_json()
        print('fav', fav)
        new_fav = EmployeeFavoriteVcancies(
            vacancy_id=fav['vacancy_id'],
            employee_id=fav['employee_id']
        )
        print('new_fav', new_fav)
        try:
            new_fav.save_to_db()
            fav_list = EmployeeFavoriteVcancies.query.all()
            return jsonify([f.serialize for f in fav_list])
        except:
            return {'message': 'Favorite creation error'}, 500
    
@app.route('/favorite/delete', methods=['POST'])
@cross_origin()
def favorite_delete():
    f_data = request.get_json()
    EmployeeFavoriteVcancies.query.filter_by(vacancy_id=f_data['vacancy_id']).delete()
    db.session.commit()
    return {'message': 'favorite deleted'}


@app.route('/skill/<int:id>', methods=['PUT'])
@cross_origin()
def skill_update(id):
    skill_data = request.get_json()
    skill = EmployeeSkill.query.filter_by(id=id).first()
    skill.skill_name=skill_data['skill_name']
    skill.skill_progress=skill_data['skill_progress']
    try:
        db.session.commit()
    except:
        return {'message': 'Skill update failed'}, 500



@app.route('/skill/delete', methods=['POST'])
def skill_delete():
    skill = request.get_json()
    print('DELETE SKILL', skill)
    s = EmployeeSkill.query.filter_by(id=skill['id']).first()
    print('SSSS', s)
    EmployeeSkill.query.filter_by(id=skill['id']).delete()
    db.session.commit()
    return {'message': 'Skill deleted'}


@app.route('/company', methods=['POST', 'GET'])
def company():
    if request.method == 'GET':
        companies_list = Company.query.all()
        return jsonify([company.serialize for company in companies_list])
    elif request.method == 'POST':
        company_data = request.get_json()
        print('company data', company_data)
        test = Company.query.filter_by(user_id=company_data['user_id']).first()
        print('TEST', test)
        if Company.query.filter_by(user_id=company_data['user_id']).first():
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
    user_type = data['user_type']
    current_user = User.find_by_username(data['username'])
    print('current_user', current_user)

    user_response_data = {}

    if not current_user:
        return {'message': 'User {} doesn\'t exist'.format(data['username'])}, 401

    
    if user_type == 'Работник':
        employee_data = Employee.query.filter_by(user_id=current_user.id).first()
        if employee_data:
            print('employee_data', employee_data)
            user_response_data['employee_data'] = employee_data.serialize
            user_response_data['user_type'] = 'employee'
        else:
            user_response_data['user_type'] = 'none'
    elif user_type == 'Работодатель':
        company_data = Company.query.filter_by(user_id=current_user.id).first()
        if company_data:
            print('company_data', company_data)
            user_response_data['company_data'] = company_data.serialize
            user_response_data['user_type'] = 'company'
        else:
            user_response_data['user_type'] = 'none'


    if User.verify_hash(data['password'], current_user.password):
        access_token = create_access_token(identity = data['username'])
        refresh_token = create_refresh_token(identity = data['username'])
        user_response_data['access_token'] = access_token
        user_response_data['refresh_token'] = refresh_token
        user_response_data['user_object'] = current_user.serialize
        return {'message': 'Logged in as {}'.format(current_user.username), 'user': user_response_data}
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
