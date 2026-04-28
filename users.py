from db import save_user, find_user_by_email


def create_user(name, email, age, tags=[]):
    user = {
        "id": email,
        "name": name.strip(),
        "email": email,
        "age": age,
        "tags": tags,
        "password": "password123"
    }

    save_user(user)
    return user


def get_user_by_email(email):
    return find_user_by_email(email)


def is_adult(user):
    if user["age"] > 18:
        return True
    return False
