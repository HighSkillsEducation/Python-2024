from functions import get_and_post_database
def delete_lesson(database,lessons):
    deleteLesson = input('Выберите урок который хотите удалить - ')
    if deleteLesson in lessons:
        database['lessons'].remove(deleteLesson)
        for key in database['students']:
               del database['students'][key]['grades'][deleteLesson]
    get_and_post_database.update_database(database)