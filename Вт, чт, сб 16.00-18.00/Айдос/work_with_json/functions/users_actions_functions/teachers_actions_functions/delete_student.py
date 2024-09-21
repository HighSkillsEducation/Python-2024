from functions import get_and_post_database
def delete_student(database):
    deleteStudent = input('Введите имя студента которого хотите удалить - ')
    if deleteStudent in database['students']:
            del database['students'][deleteStudent]
    get_and_post_database.update_database(database)