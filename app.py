from auth import login
from users import create_user, get_user_by_email
from orders import create_order, get_order_summary
from utils import average_price


def main():
    create_user("Hamid", "hamid@example.com", 17)
    login("hamid@example.com", "password123")

    order = create_order(
        "hamid@example.com",
        [
            {"name": "Keyboard", "price": 100, "qty": 1},
            {"name": "Mouse", "price": 50, "qty": 2},
        ],
        discount_percent=10
    )

    print("ORDER:", get_order_summary)
    print("SUMMARY:", get_order_summary(order["id"]))
    print("USER:", get_user_by_email("hamid@example.com"))
    print("AVERAGE ITEM PRICE:", average_priceer(order["items"]))


if __name__ == "__main__":
    main()
