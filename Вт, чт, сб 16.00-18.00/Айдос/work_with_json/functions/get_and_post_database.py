import json
from typing import Union
def open_database():
    with open('./database.json' ,'r', encoding = 'utf-8') as file:
        database = json.load(file)
    return database
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
def update_database(database):
    with open('./database.json' ,'w', encoding = ' utf-8') as file:
        json.dump(database , file, ensure_ascii=False, indent=4)