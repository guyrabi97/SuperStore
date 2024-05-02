from SuperStore.ClientNotFoundError import ClientNotFoundError
from SuperStore.Laptop import Laptop
from SuperStore.ShirtNotFoundError import ShirtNotFoundError
from SuperStore.Smartphone import Smartphone
from SuperStore.clients import Client
from SuperStore.product import Product
from SuperStore.superstore import SuperStore

store=SuperStore("products_supply.csv", "Shirts.csv" , "clients.csv" , "orders.csv")

def print_products():
    store.print_products()


def print_clients():
    store.print_clients()


def add_product(store):
    product_id1 = int(input("insert product id to check if the product already in the store"))
    if store.is_product_id_exist(product_id1) != False:
        print("the product already exist in the store")
    else:
        l_or_s=int(input("the product does not exist\nif you want to insert a Laptop choose 1\nif you want to insert a smartphone choose 2\n what is your choice?"))
        if l_or_s == 1:
            l_product_id = product_id1
            l_brand = input("insert product brand:")
            l_model = input("insert product model:")
            l_year = int(input("insert product year:"))
            l_price = float(input("insert product price:"))
            l_CPU = input("insert product CPU")
            l_hard_disk = int(input("insert product hard disk"))
            l_screen = int(input("insert screen size"))
            l = Laptop(l_product_id, l_brand, l_model, l_year, l_price , l_CPU , l_hard_disk , l_screen)
            # store.add_product(l)
            store+= l
            print("the product added to the store")
        elif l_or_s == 2:
            s_product_id = product_id1
            s_brand = input("insert product brand:")
            s_model = input("insert product model:")
            s_year = int(input("insert product year:"))
            s_price = float(input("insert product price:"))
            s_cell_net = input("insert cellular network")
            s_num_cores = int(input("insert number of cores"))
            s_cum_res = int(input("insert camera resolution"))
            s = Smartphone(s_product_id,s_brand,s_model,s_year,s_price,s_cell_net,s_num_cores,s_cum_res)
            # store.add_product(s)
            store += s
            print("the product added to the store")

def add_client(store):
    client_id1 = int(input("insert client id to check if the client is already in the store"))
    if store.is_client_id_exist(client_id1) != False:
        print("the client already exist in the store")
    else:
        print("client does not exist")
        c_client_id = client_id1
        c_name = input("insert client name:")
        c_email = input("insert client email:")
        c_address = input("insert client address:")
        c_phone = input("insert client phone number:")
        c_gender = input("insert client gender (M/F):")
        c = Client(c_client_id, c_name, c_email, c_address, c_phone, c_gender)
        store.add_client(c)
        print("the client is added to the store")


def remove_product():
    product_id = int(input("insert product id:"))
    if store.remove_product(product_id):
        print(f"{product_id} deleted")
    else:
        print(f"{product_id} not exist")


def remove_client():
    client_id = int(input("insert client id:"))
    if store.remove_client(client_id):
        print(f"{client_id} deleted")
    else:
        print(f"{client_id} not exist")


def get_all_by_price_under():
    max_price = float(input("insert maximum price:"))
    print(f"---- All products under price ({max_price}):")
    for product in store.get_all_price_under(max_price):
        print(product)


def get_most_expensive_product():
    m_expensive = store.get_most_expensive_product()
    print(f"The most expensive product is: {m_expensive}")

def get_all_phones():
    phone_list= store.get_all_phones()
    print(f"the list of all phones in the store:{phone_list}")

def get_all_laptops():
    laptop_list = store.get_all_laptops()
    print(f"the list of all laptops in the store:{laptop_list}")

def phone_average_price():
    phone_avg = store.phone_average_price()
    print(f"the average price for a phone in the store is:{phone_avg}")

def get_max_screen():
    max_screen = store.get_max_screen()
    print(f"the maximum size for a screen in the store is:{max_screen}")

def get_common_cam():
    common_cam = store.get_common_cam()
    print(f"the most common camera in the store is:{common_cam}")

def list_popular():
    list_pop=store.list_popular()
    print(f"the list of all popular products in the store:{list_pop}")

def print_shirts():
    store.print_shirts()

def add_order():
    client_id = int(input("insert client id"))
    product_id = int(input("insert product id"))
    quantity = int(input("insert the quantity of the product that you want to order"))
    try:
        store.add_order(client_id,product_id,quantity)
    except ClientNotFoundError as e:
        print(e)
        print("please try again")
        add_order()
    except ShirtNotFoundError as e:
        print(e)
        print("please try again")
        add_order()
    except ValueError as e:
        print(e)
        print("please try again")
        add_order()



def print_orders():
    store.print_orders()


def main():
    print("--- MENU ---")
    print("1. Print all products")
    print("2. Print all clients")
    print("3. Add new product to the store")
    print("4. Add new client to the store")
    print("5. Remove product")
    print("6. Remove client")
    print("7. Print all products under price")
    print("8. Print the most expensive product")
    print("9.print smartphone list")
    print("10.print laptop list")
    print("11.print average phone price")
    print("12.print largest laptop screen ")
    print("13.print common camera resolution")
    print("14.print popular products")
    print("15. print all shirts")
    print("16. add new order")
    print("17. print all orders")
    print("18.Exit")
    num= int(input("What is your choice?"))

    while 0<num<18:
        if num == 1:
            print_products()
        elif num == 2:
            print_clients()
        elif num == 3:
            add_product(store)
        elif num == 4:
            add_client(store)
        elif num == 5:
            remove_product()
        elif num == 6:
            remove_client()
        elif num == 7:
            get_all_by_price_under()
        elif num == 8:
            get_most_expensive_product()
        elif num == 9:
            get_all_phones()
        elif num == 10:
            get_all_laptops()
        elif num==11:
            phone_average_price()
        elif num == 12:
            get_max_screen()
        elif num == 13:
            get_common_cam()
        elif num == 14:
            list_popular()
        elif num==15:
            print_shirts()
        elif num==16:
            add_order()
        elif num==17:
            print_orders()

        print()
        print("--- MENU ---")
        print("1. Print all products")
        print("2. Print all clients")
        print("3. Add new product to the store")
        print("4. Add new client to the store")
        print("5. Remove product")
        print("6. Remove client")
        print("7. Print all products under price")
        print("8. Print the most expensive product")
        print("9.print smartphone list")
        print("10.print laptop list")
        print("11.print average phone price")
        print("12.print largest laptop screen ")
        print("13.print common camera resolution")
        print("14.print popular products")
        print("15. print all shirts")
        print("16. add new order")
        print("17. print all orders")
        print("18.Exit")
        num = int(input("What is your choice?"))



if __name__ == "__main__":
    main()
