from functions import get_and_post_database
def add_student(database,lessons):
    login = input('Введите логин нового студента - ')
    name = input('Введите имя нового студента - ')
    passs = input('Введите пароль для нового студента - ')    
    database['students'][f'{login}'] = {
        'name' : name,
        'pass' : passs,
        'grades' : {
}
    }    
    for key in lessons:
        database['students'][f'{login}']['grades'][key] = 0
    get_and_post_database.update_database(database)