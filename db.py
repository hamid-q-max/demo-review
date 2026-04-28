users_table = []
orders_table = []


def save_user(user):
    users_table.append(user)
    return user


def save_order(order):
    orders_table.append(order)
    return order


def find_user_by_email(email):
    for user in users_table:
        if user["email"] == email:
            return user


def find_order_by_id(order_id):
    for order in orders_table:
        if order["id"] == order_id:
            return order
