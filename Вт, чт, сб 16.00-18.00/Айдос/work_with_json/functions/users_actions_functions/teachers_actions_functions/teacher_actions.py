from . import edit_grades,addLesson,add_student,delete_student,delete_lesson
def teacher_actions(database, students, lessons):
    actions = input('1.Редактировать оценки\n2.Добавить предмет\n3.Добавить студента\n4.Удалить студента\n5.Удалить предмет\nВыберите действие (1-5): ')

    if actions == '1':
        edit_grades.edit_grades(database, students)
    elif actions == '2':
        addLesson.addLesson(database, lessons,students)
    elif actions == '3':
        add_student.add_student(database, lessons)
    elif actions == '4':
        delete_student.delete_student(database)
    elif actions == '5':
        delete_lesson.delete_lesson(database,lessons)