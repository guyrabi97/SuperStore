class Product:
    def __init__(self,product_id,brand,model,year,price):
        self.product_id = product_id
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        if len(str(year))!=4:
            self.year="the year should be 4 digits number"

    def print_me(self):
        print(f"----{self.product_id}----\n"
              f"brand:{self.brand}\nmodel:{self.model}\nyear:{self.year}\nprice:{self.price}")

    def __str__(self):
        return (f"{self.product_id},{self.brand},{self.model},{self.year},{self.price}")

    def __repr__(self):
        return str(self)

    def is_popular(self):
        if int(self.year)>2017 and int(self.price)<=3000:
            return True
        else:
            return False


