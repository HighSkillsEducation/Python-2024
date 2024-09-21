import json
from typing import Union
def open_database():
    with open('./database.json' ,'r', encoding = 'utf-8') as file:
        database = json.load(file)
    return database

def program():
    database = open_database()
    teachers = get_users(database, 'teachers')
    students = get_users(database, 'students')
    lessons = get_lessons(database)
    users = teachers | students
    login(database, lessons, students)
def create_list_or_dictionary(item: Union[list, dict], key, value):
    if isinstance(item,dict):
        item[key] = value
    elif isinstance(item,list):
        for j in value:
            item.append(j)

def get_dict_database(database: dict, items: Union[dict, list], key_str = str):
    for key, value in database.items():
        if key_str == key:
            create_list_or_dictionary(items, key, value)

def get_users(database, key_str):
    users = {}
    get_dict_database(database,users, key_str)
    return users

def get_lessons(database):
    lessons = []
    get_dict_database(database, lessons, 'lessons')
    return lessons

def login(database, lessons, students):
    login_input = input('Введите логин: ')
    pass_input = input('Введите пароль: ')
    if login_input in database['teachers'] and pass_input == database['teachers'][login_input]['pass']:
        print(f'Добро пожаловать: {login_input}')
        teacher_actions(database, students, lessons)
    elif login_input in database['students'] and pass_input == database['students'][login_input]['pass']:
        print(f'Добро пожаловать: {login_input}')
        grade()
    else:
        print('-- Неверный логин или пароль --')

def teacher_actions(database, students, lessons):
    actions = input('Выберите действие (1-5) - ')

    if actions == '1':
        edit_grades(database, students)
    elif actions == '2':
        addLesson(database, lessons,students)
    elif actions == '3':
        add_student(database, lessons)
    elif actions == '4':
        delete_student(database)
    elif actions == '5':
        delete_lesson(database,lessons)
def grade(students):
    action = input('Посмотреть оценки? да/нет')
    if action == 'да':
        for key, value in students['grades'].items():
            print(f'{key}: {value}')

def edit_grades(database,students):
    choose_Student = input('Введите имя студента - ')
    choose_Lesson = input('Выберите урок для смены оценки - ')
    new_Grade = int(input('Выберите новую оценку для выбранного предмета - '))
    if choose_Student in database['students'] and choose_Lesson in database['students'][choose_Student]['grades']:
        database['students'][choose_Student]['grades'][choose_Lesson] = new_Grade
        update_database(database)

def addLesson(database, lessons, students):
    add_lesson = input('Введите название нового урока - ')
    lessons.append(add_lesson)
    database['lessons'] = lessons
    for student_dicts in students.values():
        for student in student_dicts.values():
            student['grades'][add_lesson] = 0
    update_database(database)

def delete_lesson(database,lessons):
    deleteLesson = input('Выберите урок который хотите удалить - ')
    if deleteLesson in lessons:
        database['lessons'].remove(deleteLesson)
        for key in database['students']:
               del database['students'][key]['grades'][deleteLesson]
    update_database(database)

def add_student(database,lessons):
    login = input('Введите имя нового студента - ')
    passs = input('Введите пароль для нового студента - ')    
    database['students'][f'{login}'] = {
        'name' : login,
        'pass' : passs,
        'grades' : {
}
    }    
    for key in lessons:
        database['students'][f'{login}']['grades'][key] = 0
    update_database(database)
def delete_student(database):
    deleteStudent = input('Введите имя студента которого хотите удалить - ')
    if deleteStudent in database['students']:
            del database['students'][deleteStudent]
    update_database(database)
def update_database(database):
    with open('./database.json' ,'w', encoding = ' utf-8') as file:
        json.dump(database , file, ensure_ascii=False, indent=4)
program()