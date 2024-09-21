from база import get_and_pst_database
def b(database):
    feu =  input("Vvedite dannie studenta kotorogo hotite udalite: ")
    if feu in database["students"]:
        del database["students"][feu]
    get_and_pst_database.update_database(database)