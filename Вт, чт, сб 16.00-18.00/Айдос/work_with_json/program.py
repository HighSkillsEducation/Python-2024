from functions import get_and_post_database,login
def program():
    database = get_and_post_database.open_database()
    teachers = get_and_post_database.get_users(database, 'teachers')
    students = get_and_post_database.get_users(database, 'students')
    lessons = get_and_post_database.get_lessons(database)
    login.login(database, lessons, students)
program()