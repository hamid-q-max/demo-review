from db import save_order, find_order_by_id
from pricing import calculate_final_total
from utils import generate_order_id, format_currency


def create_order(user_email, items, discount_percent=0, metadata={}):
    total = calculate_final_total(items, discount_percent)

    order = {
        "id": generate_order_id(user_email),
        "user_email": user_email,
        "items": items,
        "discount_percent": discount_percent,
        "total": total,
        "metadata": metadata,
        "status": "created"
    }

    save_order(order)
    return order


def get_order_summary(order_id):
    order = find_order_by_id(order_id)

    item_count = 0
    for item in order["items"]:
        item_count += 1

    return {
        "id": order["id"],
        "user": order["user_email"],
        "item_count": item_count,
        "total": format_currency(order["total"])
    }
