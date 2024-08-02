import datetime

class Product:
    def __init__(self, name, category, price, quantity, expiry):
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity
        self.expiry = expiry

    def expired(self):
        return self.expiry < datetime.date.today()

class Inventory:
    def __init__(self):
        self.products = []

    def addProduct(self, product):
        self.products.append(product)

    def removeProduct(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                return
        raise ValueError("Product not found")

    def searchProduct(self, search_term):
        return [product for product in self.products if search_term in product.name]

    def listProduct(self):
        for product in self.products:
            print(f"Name: {product.name}, Category: {product.category}, Price: {product.price}, Quantity: {product.quantity}, Expiry date: {product.expiry}")

    def categorize(self):
        categories = {}
        for product in self.products:
            if product.category not in categories:
                categories[product.category] = []
            categories[product.category].append(product)
        return categories

    
    def check_expiry(self):
        expiredProducts = [product for product in self.products if product.expired()]
        if expiredProducts:
            print("Expired products:")
            for product in expiredProducts:
                print(f"Name: {product.name}, Category: {product.category}, Expiry date: {product.expiry}")
        else:
            print("No expired products found")
    def saveFile(self, filename):
        f = open(filename, "w")
        for product in self.products:
            f.write(f"{product.name}, {product.category},{product.price},{product.quantity},{product.expiry}\n ")

    def loadFile(self, filename):
        try:
            f = open(filename, "r")
            for line in f:
                name, category, price, quantity, expiration_date = line.strip().split(",")
                product = Product(name, category, float(price), int(quantity), datetime.date.fromisoformat(expiration_date))
                self.addProduct(product)
        except FileNotFoundError:
            print("File not found")

Inventory = Inventory()
Inventory.loadFile("Inventory.txt")

while True:
    print("1. Add Product")
    print("2. Remove Product")
    print("3. Search Product")
    print("4. List Products")
    print("5. Categorize Products")
    print("6. Check Expiry Date")
    print("7. Save and Exit")
    ch = input("Choose an option(1-7):")

    if ch == '1':
        name = input("Enter product name:")
        category = input("Enter product category:")
        price = float(input("Enter product price:"))
        quantity = int(input("Enter product quantity:"))
        expiry = datetime.date.fromisoformat(input("Enter product expiration date (YYYY-MM-DD):"))
        item = Product(name, category, price, quantity, expiry)
        Inventory.addProduct(item)

    elif ch == '2':
        product_name = input("Enter product name to be removed:")
        Inventory.removeProduct(product_name)

    elif ch == '3':
        search_term = input("Enter product to be searched:")
        search = Inventory.searchProduct(search_term)
        for item in search:
            print(f"Name: {item.name}, Category: {item.category}, Price: {item.price}")

    elif ch == '4':
        Inventory.listProduct()

    elif ch == '5':
        categories = Inventory.categorize()
        for category, products in categories.items():
            print(f"Category: {category}")
            for product in products:
                print(f"Name: {product.name}, Price: {product.price}")

    elif ch == '6':
        Inventory.check_expiry()

    elif ch == '7':
        Inventory.saveFile("Inventory.txt")
        break

    else:
        print("Invalid choice")
    
