from .Main import Main
from .Sub import Sub

#------------------------------------------------------------------------------     FLASK 


from flask import Flask, request, jsonify
# from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///src/instance/database.db'
# db = SQLAlchemy(app)


CORS(app)


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)

#------------------------------------------------------------------------------     ^


@app.route('/new-user', methods=['POST'])
def new_user():

    # curl -X POST http://127.0.0.1:5000/user/create/ \
    #  -H "Content-Type: application/json" \
    #  -d '{"name": "John Doe", "email": "johndoe@example.com"}'



    try:
        data = request.get_json()
        app.logger.debug(f"Received data: {data}")
        var_name = data.get('name')
        var_email = data.get('email')

        if not var_name or not var_email:
            raise ValueError('User name and email are required.')

        # Create a new User instance
        new_user = Main.create(var_name, var_email)
        # db.session.add(new_user)  # Add user to the session
        # db.session.commit()       # Commit the transaction to the database

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


@app.route('/user/delete/<int:id>/', methods=['DELETE'])
def del_user(id):
    id = int(id)
    try:
        app.logger.debug(f"Received id: {id} of type {type(id)}")
        
        user = Main.get_by_id(id)
        if not user:
            #bash test: curl -X DELETE http://127.0.0.1:5000/user/delete/your_arg_id_here/
            app.logger.debug(f"User with id {id} not found")
            return jsonify({'error': f'User with id {id} not found!'}), 404
        
        for log in user.get_all_sub():
            log.delete()
        user.delete()

        return jsonify({'message': f'User {id} and their logs deleted successfully!'}), 200
    except Exception as e:
        app.logger.error(f"Error: {str(e)}")
        return jsonify({'error': str(e)}), 500


@app.route('/delete-log/<int:log_id>', methods=['DELETE'])
def del_log(log_id):

    #bash test : curl -X DELETE http://127.0.0.1:5000/delete-log/your_arg_int_here


    try:

        if not isinstance(log_id, int):
            raise TypeError(f'did not receive `int` for argument instead got {type(log_id)}')

        log = Sub.get_by_id(log_id)
        
        if log:

            log.delete()
            return jsonify({'success': f'Log with id {log_id} was deleted'}), 200
        else:

            raise ValueError(f'Log with id {log_id} not found')

    except TypeError as e:

        app.logger.debug(str(e))
        return jsonify({'error': str(e)}), 400

    except ValueError as e:

        app.logger.debug(str(e))
        return jsonify({'error': str(e)}), 404

    except Exception as e:

        app.logger.error(f'Unexpected error: {str(e)}')
        return jsonify({'error': 'Internal Server Error'}), 500


@app.route('/user/update/<int:id>', methods=['PUT'])
def update_user(id):

    # curl -X PUT http://127.0.0.1:5000/user/update/your_arg_id \
    #     -H "Content-Type: application/json" \
    #     -d '{"name": "Jane Doe", "email": "janedoe@example.com"}'

    # Parsing the JSON data from the request body
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    # Fetching the user by ID
    obj = Main.get_by_id(id)

    try:
        if obj:
            # Updating the user's name and email
            obj.name = name
            obj.email = email
            obj.update()  # Assuming update() saves the changes to the DB
            return jsonify({'message': f'User with id {id} was updated successfully'}), 200
        else:
            raise ValueError(f'User with id {id} not found')

    except ValueError as e:
        return jsonify({'error': str(e)}), 404


#-------------------------------------------------------------- UNDER CONSTRUCTION 


@app.route('/update-log/<int:id>', methods=['PUT'])
def update_log(id):
    log_instance = Sub.get_by_id(id)

    data = request.get_json()
    log = data.get('log')

    try:
        if log_instance:
            log_instance.log = log
            log_instance.update()  # Commit the update to the database
            return jsonify({'message': 'Log updated successfully.'}), 200
        else:
            raise ValueError(f'Log with id {id} not found.')

    except ValueError as e:
        return jsonify({'error': str(e)}), 404


@app.route('/user/all-logs/<int:foreign_id>', methods=['GET']) #oops forgot to update route
def all_users_logs(foreign_id):
    
    append_list = []
    try:
        all_logs = Sub.get_all_by_foreign_id(foreign_id)
        if all_logs:
            for log in all_logs:
                append_list.append({"id": log.id ,"log": log.log})
            return jsonify(append_list), 200
        else:
            raise ValueError()
    except ValueError:
        raise ValueError('sorry but could not retrieve user`s logs')

