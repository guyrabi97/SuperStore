from SuperStore.product import Product


class Smartphone(Product):
    def __init__(self, product_id, brand, model, year, price,cell_net , num_cores , cam_res):
        super().__init__(product_id, brand, model, year, price)
        self.cell_net = cell_net
        self.num_cores = num_cores
        self.cam_res = cam_res

    def print_me(self):
        super().print_me()
        print(f"cell net:{self.cell_net}\nnumber of cores:{self.num_cores}\ncamera resolution:{self.cam_res}")

    def __str__(self):
        return super().__str__()+f"{self.cell_net},{self.num_cores},{self.cam_res}. "

    def __repr__(self):
        return str(self)


