from flask import Flask, request, jsonify
from engine.Main import Main
from engine.Sub import Sub

app = Flask(__name__)

@app.route('/user/new', methods=['POST'])
def new_user():
    
    name    = input('user name')
    email   =   input('users e-mail')
    Main.create(name, email)


@app.route('/user/<int:id>/new-log/', methods=['POST'])
def users_log(foreign_id):
    logger = Sub()
    log     = input('...add intel:\t')
    logger.create(log, foreign_id)


@app.route('/user/delete/<int:id>/', methods=['DELETE'])
def del_user(user):
    for log in user.get_all_sub():
        log.delete()
    user.delete()



@app.route('/user/<int:id>/delete-log/<int:id>', methods=['DELETE'])
def del_log(log):
    log.delete()


@app.route('/user/update/<int:id>', methods=['PUT'])
def update_user(user):
    user.name = input('new name')
    user.email = input('new email')
    user.update()


@app.rout('/user/<int:id>/update-log/<int:foreign_id>', methods=['PUT'])
def update_log(log_instance):
    log_instance.log = input('edit log:\t')
    log_instance.update()


@app.route('/user/all-users', methods=['GET'])
def all_users():
    for user in Main.get_all():
        print(f'name:\t{user.name}')


@app.route('/user/<int:id>/all-logs/<int:foreign_id>', methods=['GET'])
def all_users_logs(foreign_id):
    logs = Sub.get_all_by_foreign_id(foreign_id)
    for log in logs:
        print(log.log)

