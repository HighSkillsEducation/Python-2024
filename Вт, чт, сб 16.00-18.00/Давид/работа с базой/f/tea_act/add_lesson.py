from база import get_and_pst_database
def add_lesson(database, lessons):
    new_lesson = input("Введите новый урок: ")
    lessons.append(new_lesson)
    database["lessons"] = lessons
    for key in database["students"]:
        database["students"][key]["grades"][lessons[-1]] = 0
    get_and_pst_database.update_database(database)