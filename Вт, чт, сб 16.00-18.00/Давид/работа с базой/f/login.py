
from . import users_actions
def login(database, lessons, students):
    login_input = input('Введите логин: ')
    pass_input = input('Введите пароль: ')
    if login_input in database['teachers'] and pass_input == database['teachers'][login_input]['pass']:
        print(f'Добро пожаловать, {database["teachers"][login_input]["name"]}')
        users_actions.teacher_actions.teacher_actions(database, students, lessons)
    elif login_input in database['students'] and pass_input == database['students'][login_input]['pass']:
        print(f'Добро пожаловать, {database["students"][login_input]["name"]}')
        users_actions.grade.grade(database,login_input)
    elif login_input in database["admins"] and pass_input == database["admins"][login_input]["pass"]:
        print(f'Добро пожаловать, {database["admins"][login_input]["name"]}')
        users_actions.teacher_actions.teacher_actions(database, students, lessons)
        users_actions.c.c(database)
    else:
        print('-- Неверный логин или пароль ')