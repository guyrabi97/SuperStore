from SuperStore.product import Product


class Shirts(Product):
    def __init__(self, product_id, product_name , brand, model, year, price, units_in_stock):
        super().__init__(product_id, brand, model, year, price)
        self.product_name = product_name
        self.units_in_stock = units_in_stock

    def __str__(self):
        return f"{self.product_id},{self.product_name},{self.brand},{self.model},{self.year},{self.price},{self.units_in_stock}"