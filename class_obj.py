class Shop:

    def __init__(self, name):
        self.name = name
        self.products = []
    
    def add_products(self, name, price):
        product = Product(name, price)
        self.products.append(product)

    def sell(self):
        pass

    def __str__(self):
        return f"This is a shop with name {self.name}"

class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price 
    # def __str__(self):
    #     return self.name

    def __repr__(self):
        return self.name

Bismillah_store = Shop("Bismillah store")

Bismillah_store.add_products("Egg", 500)
Bismillah_store.add_products("mojo", 100)

Super_shop = Shop("Daily Needs")
Super_shop.add_products("Ghee", 150)
Super_shop.add_products("chees", 200)

print(Bismillah_store.name, Bismillah_store.products)
print(Super_shop.name, Super_shop.products)






