import menu_saksham
import order_saksham
from exceptions_saksham import InvalidMenuItemError, InsufficientQuantityError

def main():
   
    menu_items = menu_saksham.read_menu_from_file('menu.txt')
    current_order = order_saksham.Order()

    while True:
        print("\nWelcome to Restaurant Management System")
        print("1. Display Menu")
        print("2. Add Item to Menu")
        print("3. Update Item in Menu")
        print("4. Delete Item from Menu")
        print("5. Place Order")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            menu_saksham.display_menu(menu_items)

        elif choice == '2':
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            quantity = int(input("Enter item quantity: "))
            try:
                menu_saksham.add_item(menu_items, name, price, quantity)
            except InvalidMenuItemError as e:
                print(f"Error: {e}")

        elif choice == '3':
            name = input("Enter item name to update: ")
            price = float(input("Enter new price: "))
            quantity = int(input("Enter new quantity: "))
            try:
                menu_saksham.update_item(menu_items, name, price, quantity)
            except InvalidMenuItemError as e:
                print(f"Error: {e}")

        elif choice == '4':
            name = input("Enter item name to delete: ")
            try:
                menu_saksham.delete_item(menu_items, name)
            except InvalidMenuItemError as e:
                print(f"Error: {e}")

        elif choice == '5':
            try:
                current_order.take_order(menu_items)
                current_order.calculate_total()
                current_order.generate_receipt()
                menu_saksham.write_menu_to_file('menu.txt', menu_items)
                order_saksham.write_orders_to_file('orders.txt', current_order)
                current_order = order_saksham.Order()  
            except (InvalidMenuItemError, InsufficientQuantityError) as e:
                print(f"Error: {e}")

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
