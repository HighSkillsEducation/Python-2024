from база import get_and_pst_database
def c(database):
    login = input("Введите логин нового учителя: ")
    name = input("Введите имя нового учителя: ")
    pas = input("Введите пароль нового учителя: ")
    database["teachers"][login] = {
        "name": name,
        "pass": pas,
        "teacher": True,
        "admin": False
        }
    get_and_pst_database.update_database(database)