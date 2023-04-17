from ..file_services import load_from_file


def get_user(filter_value, filter_key='id'):
    user_from_file = load_from_file()

    for user in user_from_file:
        for key, value in user.items():
            if value == filter_value and key == filter_key:
                return user
