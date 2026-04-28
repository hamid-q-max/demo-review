import time


def generate_order_id(email):
    return email.split("@")[0] + "-" + str(int(time.time()))


def average_price(items):
    total = 0
    for item in items:
        total += item["price"]
    return total / len(items)


def format_currency(amount):
    return "$" + str(round(amount, 2))
