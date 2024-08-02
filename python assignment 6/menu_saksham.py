from exceptions_saksham import InsufficientQuantityError, InvalidMenuItemError


class MenuItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}: ${self.price} ({self.quantity} available)"

def read_menu_from_file(filename):
    menu_items = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, price, quantity = line.strip().split(',')
                menu_items[name] = MenuItem(name, float(price), int(quantity))
    except FileNotFoundError:
        pass
    return menu_items

def write_menu_to_file(filename, menu_items):
    with open(filename, 'w') as file:
        for item in menu_items.values():
            file.write(f"{item.name},{item.price},{item.quantity}\n")

def display_menu(menu_items):
    for item in menu_items.values():
        print(item)

def add_item(menu_items, name, price, quantity):
    if name in menu_items:
        raise InvalidMenuItemError("Item already exists ")
    menu_items[name] = MenuItem(name, price, quantity)

def update_item(menu_items, name, price, quantity):
    if name not in menu_items:
        raise InvalidMenuItemError("Item does not exist ")
    menu_items[name] = MenuItem(name, price, quantity)

def delete_item(menu_items, name):
    if name not in menu_items:
        raise InvalidMenuItemError("Item does not exist ")
    del menu_items[name]
