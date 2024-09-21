from база import get_and_pst_database
def add_students(database, lessons):
    login = input("Введите логин нового студента: ")
    name = input("Введите имя нового студента: ")
    pas = input("Введите пароль нового студента: ")
    database["students"][login] = {
        "name": name,
        "pass": pas,
        "grades": {
            
        }
        }
    for key in lessons:
        database["students"][login]["grades"][key] = 0
    get_and_pst_database.update_database(database)