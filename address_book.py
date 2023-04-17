from services import (save_to_file,
                      load_from_file,
                      get_user)




#save_to_file()
#user_dict_from_json = load_from_file(single=True)
#user_dict_from_json = load_from_file(True)
#user_list_from_json = load_from_file()

# for key, value in user_dict_from_json.items():
#     print(f'KEY {key}\tVALUE {value}')

# print()
# print()

# for user in user_list_from_json:
#     for key, value in user.items():
#         print(f'KEY {key}\tVALUE {value}')

user_id = int(input('Upisite ID korisnika kojeg zelite dohvatiti: '))
user = get_user(user_id)

if user != None:
    print(user)
else:
    print(f"Ne postoji zapis pod id brojem {user_id}")
