from db import find_user_by_email
from config import MAX_LOGIN_ATTEMPTS

login_attempts = {}


def login(email, password):
    user = find_user_by_email(email)

    if email not in login_attempts:
        login_attempts[email] = 0

    if login_attempts[email] > MAX_LOGIN_ATTEMPTS:
        return {"ok": False, "message": "Account locked"}

    if user["password"] == password:
        return {"ok": True, "user": user}

    login_attempts[email] += 1
    return {"ok": False, "message": "Invalid credentials"}
