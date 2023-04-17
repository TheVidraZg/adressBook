import requests
import json

from services import save_to_file

def display_user(user: dict) -> None:
    print(f'Ime i prezime: {user["name"]}')
    print(f'Email : {user["email"]}')

while True:
    user_id = int(input('Upisite ID korisnika kojeg zelite dohvatiti: '))
    URL = f'https://jsonplaceholder.typicode.com/users/{user_id}'

    try:
        response = requests.get(URL)

        if response.status_code == 200:
            user_dict = json.loads(response.text)
            display_user(user_dict)
            save_to_file(data=user_dict, user_id=user_id)
        elif response.status_code == 404:
            print('Ne postoji trazeni dokument, greska 404')
        else:
            print(f'Dogodila se greska: {response.status_code}')
    
    except Exception as ex:
        print(f'Dogodila se greska : {ex}')
        
    next_round = input('Zelite li ponoviti upit?')
    if next_round.lower() != 'da':
        break
