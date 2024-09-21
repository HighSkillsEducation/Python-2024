from база import get_and_pst_database
def edict_grades(database):
    choose_student = input("Введите логин студента: ")
    lesson = input("Введите урок по которому хотите изменить оценку: ")
    new_grade = int(input("Введите новую оценку: "))
    if choose_student in database["students"]:
        database["students"][choose_student]["grades"][lesson] = new_grade
        get_and_pst_database.update_database(database)
    else:
        return