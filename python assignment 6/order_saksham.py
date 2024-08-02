from exceptions_saksham import InvalidMenuItemError, InsufficientQuantityError

class Order:
    def __init__(self):
        self.items = []

    def take_order(self, menu_items):
        while True:
            item_name = input("Enter the item name to order (or 'done' to finish): ")
            if item_name.lower() == 'done':
                break
            if item_name not in menu_items:
                raise InvalidMenuItemError(f"{item_name} is not on the menu.")
            quantity = int(input(f"Enter quantity for {item_name}: "))
            if quantity > menu_items[item_name].quantity:
                raise InsufficientQuantityError(f"Only {menu_items[item_name].quantity} of {item_name} available.")
            self.items.append((menu_items[item_name], quantity))
            menu_items[item_name].quantity -= quantity

    def calculate_total(self):
        return sum(item.price * quantity for item, quantity in self.items)

    def generate_receipt(self):
        print("\nReceipt:")
        for item, quantity in self.items:
            print(f"{item.name}: ${item.price} x {quantity} = ${item.price * quantity}")
        print(f"Total: ${self.calculate_total()}")

def write_orders_to_file(filename, order):
    with open(filename, 'a') as file:
        for item, quantity in order.items:
            file.write(f"{item.name},{item.price},{quantity}\n")
