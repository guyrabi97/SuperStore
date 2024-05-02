import numpy as np
from SuperStore.ClientNotFoundError import ClientNotFoundError
from SuperStore.Laptop import Laptop
from SuperStore.ShirtNotFoundError import ShirtNotFoundError
from SuperStore.Shirts import Shirts
from SuperStore.Smartphone import Smartphone
from SuperStore.clients import Client
from SuperStore.product import Product
from SuperStore.superstore import SuperStore
import matplotlib.pyplot as plt
store=SuperStore("products_supply.csv", "Shirts.csv" , "clients.csv" , "orders.csv")

from numpy import genfromtxt
orders_array = genfromtxt('orders.csv', delimiter=',', dtype=np.int32, skip_header=1)


orders_sID=[]
orders_quantity = []
shirt_prices = []
orders_prices =[]
for order in store.Orders:
    orders_sID.append(order.product_id)
    orders_quantity.append(order.quantity)
for id in orders_sID:
    shirt1=store.get_shirt(id)
    shirt_prices.append(shirt1.price)
for x,y in zip(shirt_prices,orders_quantity):
    orders_prices.append(int(x*y))
orders_array = np.column_stack((orders_array, orders_prices))

def biggest_order(orders_array):
    biggest=0
    for row in orders_array:
        if row[4]>biggest:
            biggest=row[4]
    big_row = orders_array[orders_array[:,4] == biggest]
    big_orderID=big_row[0,0]
    big_clientID=big_row[0,1]
    big_productID=big_row[0,2]
    print(big_row)
    for client in store.clients:
        if client.client_id==big_clientID:
            big_clientName=client.name
    for product in store.shirts:
        if product.product_id==big_productID:
            big_productName= product.product_name
    return f"the most expensive order is order number:{big_orderID}, client name:{big_clientName},product name:{big_productName} and the price is:{biggest}"


def client_order(orders_array):
    clientID = int(input("insert client id"))
    if store.is_client_id_exist(clientID)==False:
        raise ClientNotFoundError("the client not exist")
    for client in store.clients:
        if clientID == client.client_id:
            clientName=client.name
    orders_num=0
    orders_total=0
    for row in orders_array:
        if row[1]==clientID:
            orders_num+=1
            orders_total+=row[4]
    return f"the client name is:{clientName}\nthe number of orders:{orders_num}\nthe total payment is:{orders_total}"

def above_avg(orders_array):
    avg_price= sum(orders_prices)/len(orders_prices)
    for row in orders_array:
        if row[4]>avg_price:
            print(row)

def orders_dic(orders_array):
    orders_dic={}
    for client in store.clients:
        count=0
        for row in orders_array:
            if client.client_id==row[1]:
                count+=1
                orders_dic[client.name]=count
    return orders_dic


def orders_chart(orders_array):
    client_dic=orders_dic(orders_array)
    keys=list(client_dic.keys())
    values=list(client_dic.values())
    colors = ['r', 'g', 'b','orange','yellow','pink']
    plt.bar(keys, values, color=colors)
    plt.title('client name vs number of orders')
    plt.xlabel('client name')
    plt.ylabel('number of orders')
    plt.show()

# #tests
# #to add the price of evry order in to the array as a new column
# print(orders_array)
# #to find the biggest order made
# print(biggest_order(orders_array))
# #to show for every client the number of orders and the total payment
# print(client_order(orders_array))
# #shows all the orders that costs above average
# above_avg(orders_array)
# #shows dictionery of all clients and number of orders they made
# print(orders_dic(orders_array))
#shows chart bar of every client and the number of orders he made
orders_chart(orders_array)




