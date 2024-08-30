from .Main import Main
from .Sub import Sub

#-------------------

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' 
CORS(app)
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)   
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
#-------------------

@app.route('/user/new', methods=['POST'])
def new_user(js_input_name, js_input_email):

    var_name = js_input_name
    var_email= js_input_email


    try:
        data        =   request.json
        var_name    = data.get('name')
        var_email   = data.get('email')
        if not var_name or not var_email:
            raise ValueError('user name must be str and or email must abide format')
        new_user    =   Main.create(var_name, var_email)
        db.session.add(new_user) #these are the only two new lines correct ?
        db.commit()             #why am i committing when ive already done this in Main and Sub?
        return jsonify({
            'id':   new_user.id,
            'name': new_user.name,
            'email':new_user.email
        }), 201
    except ValueError:
            return jsonify({'error': str(ValueError)}), 400


@app.route('/user/<int:id>/new-log/', methods=['POST'])
def users_log(foreign_id):
    try:
        data = request.json
        var_log = data.get('log')
        
        if not var_log:
            raise ValueError('var_log must be str and var_foreign_id must be int')
        new_log = Sub.create(var_log, foreign_id)
        return jsonify({
            'log'           : new_log.log,
            'foreign_id'    : new_log.foreign_id
        }), 201
    except ValueError:
        return jsonify({'error': str(ValueError)}), 400


@app.route('/user/delete/<int:id>/', methods=['DELETE'])
def del_user(user):
    for log in user.get_all_sub():
        log.delete()
    user.delete()


@app.route('/user/<int:id>/delete-log/<int:log_id>', methods=['DELETE'])
def del_log(log):
    log.delete()


@app.route('/user/update/<int:id>', methods=['PUT'])
def update_user(user):
    user.name = input('new name')
    user.email = input('new email')
    user.update()


@app.route('/user/<int:id>/update-log/<int:foreign_id>', methods=['PUT'])
def update_log(log_instance):
    log_instance.log = input('edit log:\t')
    log_instance.update()


@app.route('/user/all-users', methods=['GET'])
def all_users():
    try:
        users   = Main.get_all()
        user_list = []

        for user in users:
            user_list.append({
                'id': user.id,
                'name': user.name,
                'email': user.email
            })
        return jsonify(user_list), 200
    except ValueError:
        return jsonify({'error': str(ValueError)}), 500


@app.route('/user/<int:id>/all-logs/<int:foreign_id>', methods=['GET'])
def all_users_logs(foreign_id):
    logs = Sub.get_all_by_foreign_id(foreign_id)
    for log in logs:
        print(log.log)

