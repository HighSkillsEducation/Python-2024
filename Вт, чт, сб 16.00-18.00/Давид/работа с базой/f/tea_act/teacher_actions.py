from . import add_lesson,add_students,b,a,edict_grades
def teacher_actions(database, students, lessons):
    actions = input('1.Редактировать оценки\n2.Добавить предмет\n3.Добавить студента\n4.Удалить студента\n5.Удалить предмет\nВыберите действие (1-5): ')
    
    if actions == '1':
       edict_grades.edict_grades(database, students)
    elif actions == '2':
        add_lesson.add_lesson(database, lessons,students)
    elif actions == '3':
        add_students.add_students(database, lessons)
    elif actions == '4':
        b.b(database)
    elif actions == '5':
        a.a(database,lessons)