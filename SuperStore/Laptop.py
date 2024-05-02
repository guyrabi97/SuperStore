from SuperStore.product import Product


class Laptop(Product):
    def __init__(self, product_id, brand, model, year, price,CPU,hard_disk,screen):
        super().__init__(product_id, brand, model, year, price)
        self.CPU = CPU
        self.hard_disk = hard_disk
        self.screen = screen

    def print_me(self):
        super().print_me()
        print(f"CPU:{self.CPU}\nhard_disk:{self.hard_disk}g\nscreen:{self.screen}(inch)")

    def __str__(self):
        return super().__str__()+f"{self.CPU},{self.hard_disk},{self.screen}. "

    def __repr__(self):
        return str(self)


