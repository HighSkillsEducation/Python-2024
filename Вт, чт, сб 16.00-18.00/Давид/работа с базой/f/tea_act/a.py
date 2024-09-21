from база import get_and_pst_database
def a(database, lessons):
    de = input("Введите какой урок хотите удалить: ")
    lessons.remove(de)
    database["lessons"] = lessons
    for key in database["students"]:
       del database["students"][key]["grades"][de]
    get_and_pst_database.update_database(database)