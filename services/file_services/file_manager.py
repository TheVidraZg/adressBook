from json import dump as json_dump
from json import load as json_load

from data import (user_json_from_dict,
                  user_json_from_list)
# Ovaj dio koda je za deklaraciju i NE pokrece se ovdje
# pokrece se tek kod poziva funkcije

def save_to_file():
    try:
    #with open('data/json_files/user_id_1.json', 'w') as file_writer:
        with open('data/json_files/users.json', 'w') as file_writer:
        #file_writer.write(user_json_from_dict)
        #file_writer.write(str(user_json_from_dict))
        #json_dump(user_json_from_dict, file_writer)
        #json_dump(user_json_from_dict, file_writer, indent=4)
            json_dump(user_json_from_list, file_writer, indent=4)

    except Exception as ex:
        print(f'Dogodila se greska: {ex}')
    

def load_from_file():
    try:
         #with open('data/json_files/user_id_1.json', 'r') as file_reader:
        with open('data/json_files/users.json', 'r') as file_reader:
        #user_dict_from_json = json_load(file_reader)
             user_list_from_json = json_load(file_reader)

    except Exception as ex:
        print(f'Dogodila se greska: {ex}')

