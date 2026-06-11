import logging

DRINK_MENU = {
    "P1": {"name": "Phin Sữa Đá", "price": 35000},
    "F1": {"name": "Freeze Trà Xanh", "price": 55000},
    "T1": {"name": "Trà Sen Vàng", "price": 45000}
}

current_order = []


class ItemNotFoundError(Exception):
    pass


class InvalidQuantityError(Exception):
    pass


def add_to_order(drink_code, quantity):
    drink_code = drink_code.strip().upper()

    if drink_code not in DRINK_MENU:
        raise ItemNotFoundError(drink_code)

    if quantity <= 0:
        raise InvalidQuantityError(quantity)

    current_order.append({
        "code": drink_code,
        "quantity": quantity
    })

    logging.info(
        f"Added {quantity} of {drink_code} to order"
    )


def calculate_total(order):
    total = 0

    for item in order:
        code = item["code"]
        quantity = item["quantity"]

        total += (
            DRINK_MENU[code]["price"] * quantity
        )

    return total


def clear_order():
    current_order.clear()