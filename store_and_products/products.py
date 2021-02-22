class Product:
    product_id = 0
    def __init__(self,name,price,category):
        Product.product_id += 1
        self.name = name
        self.price = price
        self.category = category
        self.id = Product.product_id
    def update_price(self,percentage_change):
        if (percentage_change > 0):
            self.price += ((percentage_change / 100) * self.price)
            return self
        else:
            self.price -= ((percentage_change / -100) * self.price)
            return self
    def print_info(self):
        print(f'ID: {self.id} {self.category}: {self.name} - {self.price}')
print(__name__)

