from typing import Union
import json
def open_database():
    with open( './database.json' ,'r', encoding = ' utf-8') as file:
        database = json.load(file)
    return database
def get_dict_data(database: dict,item: Union[dict, list], key_str: str):
    for key,value in database.items():
        if key_str == key:
            create_list_or_dictionary(item, key,value)       
def create_list_or_dictionary(item: Union[list, dict], key, value):
    if isinstance(item, dict):
        item[key] = value
    elif isinstance(item, list):
        for i in value:
            item.append(i)  
def get_users(database, key_str):
    users = {}
    get_dict_data(database, users, key_str)
    return users
def get_lessons(database):
    lessons = []
    get_dict_data(database, lessons, "lessons")
    return lessons
def update_database(database):
     with open( './database.json' ,'w', encoding = ' utf-8') as file:
        json.dump(database,file, ensure_ascii=False, indent=4)