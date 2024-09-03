from .Main import Main
from .Sub import Sub

#------------------------------------------------------------------------------     FLASK 

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///src/instance/database.db'    #fixed url
db = SQLAlchemy(app)

CORS(app)


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)

#------------------------------------------------------------------------------     ^


@app.route('/new-user', methods=['POST'])
def new_user():

    try:
        data = request.get_json()
        app.logger.debug(f"Received data: {data}")
        var_name = data.get('name')
        var_email = data.get('email')

        if not var_name or not var_email:
            raise ValueError('User name and email are required.')

        # Create a new User instance
        new_user = Main.create(var_name, var_email)
        db.session.add(new_user)  # Add user to the session
        db.session.commit()       # Commit the transaction to the database

        return jsonify({
            'id': new_user.id,
            'name': new_user.name,
            'email': new_user.email
        }), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/all-users', methods=['GET'])
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


#-------------------------------------------------------------- UNDER CONSTRUCTION 

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


@app.route('/user/<int:id>/all-logs/<int:foreign_id>', methods=['GET'])
def all_users_logs(foreign_id):
    logs = Sub.get_all_by_foreign_id(foreign_id)
    for log in logs:
        print(log.log)

