import csv

from SuperStore.ClientNotFoundError import ClientNotFoundError
from SuperStore.Laptop import Laptop
from SuperStore.Order import Order
from SuperStore.ShirtNotFoundError import ShirtNotFoundError
from SuperStore.Shirts import Shirts
from SuperStore.Smartphone import Smartphone
from SuperStore.clients import Client
from SuperStore.product import Product


class SuperStore:
    def __init__(self,products,shirts,clients,Orders):
        self.products=products
        self.clients=clients
        self.Orders = Orders
        self.shirts = shirts
        with open(products)  as csvfile:
            read = csv.reader(csvfile)
            all_laptop_products = []
            all_smartphone_products=[]
            next(read)
            for row in read:
                if row[1]== "laptop":
                    product_id = int(row[0])
                    brand = row[2]
                    model = row[3]
                    year = int(row[4])
                    price = float(row[5])
                    CPU = row[6]
                    hard_disk = int(row[7])
                    screen = int(row[8])
                    all_laptop_products.append(Laptop(product_id, brand, model, year, price,CPU,hard_disk,screen))


                if row[1] == "smartphone":
                    product_id = int(row[0])
                    brand = row[2]
                    model = row[3]
                    year = int(row[4])
                    price = float(row[5])
                    cell_net = row[9]
                    num_cores = int(row[10])
                    cam_res = int(row[11])
                    all_smartphone_products.append(Smartphone(product_id,brand,model,year,price,cell_net,num_cores,cam_res))
        with open(shirts) as csvfile1:
            read1 = csv.reader(csvfile1)
            all_shirts_products = []
            next(read1)
            for row in read1:
                product_id = int(row[0])
                product_name = row[1]
                brand = "superstore"
                model ="-"
                year = 2023
                price = float(row[2])
                units_in_stock = int(row[3])
                all_shirts_products.append(Shirts(product_id,product_name,brand,model,year,price,units_in_stock))
        self.shirts= all_shirts_products
        self.products= all_laptop_products + all_smartphone_products + all_shirts_products
        with open(clients) as csvfile1:
            read1 = csv.reader(csvfile1)
            all_clients = []
            next(read1)
            for row in read1:
                client_id = int(row[0])
                name = row[1]
                email = row[2]
                address = row[3]
                phone_number = row[4]
                gender = row[5]
                client=Client(client_id,name,email,address,phone_number,gender)
                all_clients.append(client)
                self.clients=all_clients
                self.products_list=[]
        with open(Orders) as csvfile3:
            read3 = csv.reader(csvfile3)
            all_orders = []
            next(read3)
            for row in read3:
                order_id = int(row[0])
                client_id=int(row[1])
                product_id = int(row[2])
                quantity = int(row[3])
                all_orders.append(Order(order_id,client_id,product_id,quantity))
                self.Orders=all_orders



    def print_products(self):
        for p in self.products:
            print(p)

    def get_product(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product

        return None

    def get_shirt(self, product_id):
        for s in self.products:
            if s.product_id == product_id and type(s) is Shirts:
                return s

        return None

    def is_product_id_exist(self, product_id):
        return self.get_product(product_id) is not None

    def add_product(self, new_product):
        if self.is_product_id_exist(new_product.product_id):
            return False

        self.products.append(new_product)
        return True

    def remove_product(self, product_id):
        for p in self.products:
            if p.product_id == product_id:
                self.products.remove(p)
                return True

        return False

    def get_all_by_brand(self, brand):
        return list(filter(lambda p: p.brand == brand, self.products))


    def get_all_price_under(self, price):
        return list(filter(lambda p: p.price <= price, self.products))

    def get_most_expensive_product(self):
        if len(self.products) == 0:
            return None

        most_expensive = self.products[0]

        for product in self.products:
            if product.price > most_expensive.price:
                most_expensive = product

        return most_expensive

    def print_clients(self):
        for c in self.clients:
            print(c)


    def get_client(self, client_id):
        for client in self.clients:
            if client.client_id == client_id:
                return client

        return None

    def is_client_id_exist(self, client_id):
        return self.get_client(client_id) is not None

    def add_client(self, client):
        if self.is_client_id_exist(client.client_id):
            return False

        self.clients.append(client)
        return True


    def remove_client(self, client_id):
        for client in self.clients:
            if client.client_id == client_id:
                self.clients.remove(client)
                return True

        return False
    def get_all_phones(self):
        return list(filter(lambda p: type(p) == Smartphone, self.products))

    def get_all_laptops(self):
        return list(filter(lambda p: type(p) == Laptop, self.products))

    def phone_average_price(self):
        if len(self.products) == 0:
            return None

        total_prices=0
        count=0
        for s in self.products:
            if type(s) is Smartphone:
                total_prices += s.price
                count+= 1
        return (total_prices/count)

    def get_max_screen(self):
        if len(self.products) == 0:
            return None

        big_screen = 0
        for laptop in self.products:
            if type(laptop) is Laptop:
                if laptop.screen > big_screen:
                    big_screen = laptop.screen

        return big_screen

    def get_common_cam(self):
        all_cam_size=[]
        counter=0
        for s in self.products:
            if type(s) is Smartphone:
                all_cam_size.append(s.cam_res)
        most_common = all_cam_size[0]

        for i in all_cam_size:
            curr_frequency = all_cam_size.count(i)
            if (curr_frequency > counter):
                counter = curr_frequency
                most_common = i
        return most_common

    def list_popular(self):
        popular_list=[]
        for prod in self.products:
            if int(prod.year)>2017 and int(prod.price)<=3000:
                popular_list.append(prod)
        return popular_list

    def __iadd__(self, other):
        if self.is_product_id_exist(other.product_id)==False:
            self.products.append(other)
            return self


    def get_max_order_id(self):
        max_id=0
        for o in self.Orders:
            if o.order_id>max_id:
                max_id=o.order_id
        return (max_id)

    def add_order(self,client_id,product_id,quantity):
        new_order_id= self.get_max_order_id() +1
        all_client_id=[]
        all_product_id = []
        for p in self.products:
            all_product_id.append(p.product_id)
        for c in self.clients:
            all_client_id.append(c.client_id)
        if client_id not in all_client_id:
            raise ClientNotFoundError("client id not exist")
        if product_id not in all_product_id:
            raise ShirtNotFoundError("product id not exist")
        for s in self.shirts:
            if product_id == s.product_id and quantity>s.units_in_stock:
                raise ValueError("not enough units in stock")
        for p in self.products:
            if type(p) is not Shirts and quantity>1 and product_id == p.product_id:
                raise ValueError("not enough units in stock")
        self.Orders.append(Order(new_order_id,client_id,product_id,quantity))
        print("the order has been taken successfully")



    def print_orders(self):
        for o in self.Orders:
            print(o)

    def print_shirts(self):
        for s in self.shirts:
            print(s)













store=SuperStore("products_supply.csv", "Shirts.csv" , "clients.csv" , "orders.csv")

