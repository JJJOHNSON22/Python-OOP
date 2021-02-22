import products
class Store:
    def __init__(self,name):
        self.name = name
        self.product_list = []

    def add_product(self, new_product,price,category):
        self.product_list.append(products.Product(new_product,price,category))
        return self

    def sell_product(self,id):
        del self.product_list[id]
        
    def show_inventory(self):
        for item in enumerate(self.product_list):
            x = 0
            self.product_list[item[x]].print_info()
            x += 1
    
    def inflation(self, percentage_change):
        for item in enumerate(self.product_list):
            x = 0
            self.product_list[item[x]].print_info()
            self.product_list[item[x]].update_price(percentage_change)
            x += 1
    
    def set_clearance(self, percentage_change):
        for item in enumerate(self.product_list):
            percentage_change *= -1
            x = 0
            self.product_list[item[x]].print_info()
            self.product_list[item[x]].update_price(percentage_change)
            x += 1




