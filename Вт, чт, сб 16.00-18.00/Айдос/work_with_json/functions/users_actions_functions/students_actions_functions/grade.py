def grade(database,login_input):
    action = input('Посмотреть оценки? да/нет ')
    if action == 'да':
        for lesson, grade in database["students"][login_input]["grades"].items():
            print(f"{lesson}: {grade} балла/баллов")
