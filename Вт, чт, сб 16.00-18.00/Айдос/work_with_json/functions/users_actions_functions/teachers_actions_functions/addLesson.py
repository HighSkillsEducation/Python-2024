from functions import get_and_post_database
def addLesson(database, lessons, students):
    add_lesson = input('Введите название нового урока - ')
    lessons.append(add_lesson)
    database['lessons'] = lessons
    for student_dicts in students.values():
        for student in student_dicts.values():
            student['grades'][add_lesson] = 0
    get_and_post_database.update_database(database)