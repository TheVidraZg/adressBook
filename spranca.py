# svi Python importi
import os
import json
import datetime


# navodimo globalne variajble
user_json_from_dict = {}


# Deklaracija svih klasa
class User:
    pass

class Address:
    pass


class Geo:
    pass


class Company:
    pass



# Deklaracije funkcija
def load_from_file():
    pass


def get_user(filter_value, filter_key='id'):
    user_from_file = load_from_file()

    for user in user_from_file:
        for key, value in user.items():
            if value == filter_value and key == filter_key:
                return user

# ...


# Glavni dio programa
user_id = int(input('Upisite ID korisnika kojeg zelite dohvatiti: '))
user = get_user(user_id)

if user != None:
    print(user)
else:
    print(f"Ne postoji zapis pod id brojem {user_id}")

# eventualno mogu koristiti while petlju
