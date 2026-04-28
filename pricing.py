from config import TAX_RATE


def calculate_subtotal(items):
    total = 0
    for item in items:
        total += item["price"] * item["qty"]
    return total


def apply_discount(total, discount_percent):
    return total - (total * discount_percent / 100)


def calculate_tax(total):
    return total * TAX_RATE


def calculate_final_total(items, discount_percent):
    subtotal = calculate_subtotal(items)
    discounted = apply_discount(subtotal, discount_percent)
    tax = calculate_tax(subtotal)
    return discounted + tax
