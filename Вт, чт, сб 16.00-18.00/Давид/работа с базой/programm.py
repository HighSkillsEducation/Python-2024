from база import get_and_pst_database
from f import login
def programm():
    database = get_and_pst_database.open_database()
    admins = get_and_pst_database.get_users(database, "admins")
    teachers = get_and_pst_database.get_users(database, "teachers")
    students = get_and_pst_database.get_users(database, "students")
    lessons = get_and_pst_database.get_lessons(database)
    users = admins | teachers | students 
    login.login(users, database, lessons)
programm()