from store import Store
from products import Product

store1 = Store('J3print').add_product('Pen',10,'Arts & Crafts').add_product('Ruler',20,'Arts & Crafts').add_product('Eraser',5,"School Supplies")
store1.inflation(5)
store1.sell_product(2)
store1.show_inventory()
store1.set_clearance(5)
store1.show_inventory()