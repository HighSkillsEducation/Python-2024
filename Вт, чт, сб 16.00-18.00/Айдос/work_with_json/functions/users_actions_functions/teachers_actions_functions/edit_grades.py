from functions import get_and_post_database
def edit_grades(database,students):
    choose_Student = input('Введите имя студента - ')
    choose_Lesson = input('Выберите урок для смены оценки - ')
    new_Grade = int(input('Выберите новую оценку для выбранного предмета - '))
    if choose_Student in database['students'] and choose_Lesson in database['students'][choose_Student]['grades']:
        database['students'][choose_Student]['grades'][choose_Lesson] = new_Grade
        get_and_post_database.update_database(database)