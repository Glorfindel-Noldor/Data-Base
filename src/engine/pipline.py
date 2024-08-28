from Main import Main
from Sub import Sub

def new_user():
    name    = input('user name')
    email   =   input('users e-mail')
    Main.create(name, email)

def users_log(foreign_id):
    logger = Sub()
    log     = input('...add intel:\t')
    logger.create(log, foreign_id)

def del_user(user):
    for log in user.get_all_sub():
        log.delete()
    user.delete()

def del_log(log):
    log.delete()

def update_user(user):
    user.name = input('new name')
    user.email = input('new email')
    user.update()

def update_log(log_instance):
    log_instance.log = input('edit log:\t')
    log_instance.update()

def all_users():
    for user in Main.get_all():
        print(f'name:\t{user.name}')

def all_users_logs(foreign_id):
    logs = Sub.get_all_by_foreign_id(foreign_id)
    for log in logs:
        print(log.log)
