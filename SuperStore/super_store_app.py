import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv

from SuperStore.Laptop import Laptop
from SuperStore.superstore import SuperStore
from SuperStore.Shirts import Shirts
from SuperStore.Smartphone import Smartphone
from SuperStore.clients import Client
from SuperStore.product import Product
store=SuperStore("products_supply.csv", "Shirts.csv" , "clients.csv" , "orders.csv")

super_app=tk.Tk()
super_app.title('super store')
super_app.geometry("1000x800")
lbl = Label(super_app,text="Super Store",font=("Verdana",30),fg="royal blue")
lbl.grid(column=0,row=0)
products=tk.Label(super_app,text="Products", font=("Arial",15),fg="Purple")
products.grid(column=0,row=1)
products.place(x=20,y=50,height=50)
var = tk.StringVar()
products_box=ttk.Combobox(super_app , textvariable=var)
products_box["values"]=("all products","Laptop","Smartphone","Shirts")
products_box.config(font=("Arial",12))
products_box.place(x=20,y=100,width=180,height=30)
products_lst=tk.Listbox(super_app)
products_lst.config(width=60,height=10,font=("Arial",10))
products_lst.place(x=420,y=100)


def Display_buttom():
    selected_item = products_box.get()
    if selected_item== "all products":
        products_lst.delete(0, "end")
        for product in store.products:
            products_lst.insert(tk.END,product)
    elif selected_item == "Laptop":
        products_lst.delete(0,"end")
        for laptop in store.products:
            if type(laptop) is Laptop:
                products_lst.insert(tk.END,laptop)
    elif selected_item == "Smartphone":
        products_lst.delete(0,"end")
        for phone in store.products:
            if type(phone) is Smartphone:
                products_lst.insert(tk.END,phone)
    elif selected_item == "Shirts":
        products_lst.delete(0,"end")
        for shirt in store.products:
            if type(shirt) is Shirts:
                products_lst.insert(tk.END,shirt)


display_button=tk.Button(super_app,text="Display products",padx="20", pady="5",command=Display_buttom)
display_button.config(fg="purple",font=("Arial",12),relief="solid",highlightcolor="purple",highlightbackground="purple",highlightthickness=3)
display_button.place(x=220,y=100)

lbl2=Label(text="create new product",font=("Arial",15),fg="Purple")
lbl2.place(x=20,y=250,height=50)
id_lbl=Label(super_app,text="id",font="Arial")
id_lbl.place(x=20,y=300)
id_text=Entry(super_app)
id_text.place(x=20,y=325,height=30,width=150)
price_lbl=Label(super_app,text="price",font="Arial")
price_lbl.place(x=230,y=300)
price_txt=Entry(super_app)
price_txt.place(x=230,y=325,height=30,width=150)
brand_lbl=Label(super_app,text="Brand",font="Arial")
brand_lbl.place(x=440,y=300)
brand_txt=Entry(super_app)
brand_txt.place(x=440,y=325,height=30,width=150)
model_lbl=Label(super_app,text="Model",font="Arial")
model_lbl.place(x=660,y=300)
model_txt=Entry(super_app)
model_txt.place(x=660,y=325,height=30,width=150)
year_lbl=Label(super_app,text="Year",font="Arial")
year_lbl.place(x=20,y=370)
years=list(range(1970,2024))
year_var=StringVar()
year_txt=ttk.Combobox(super_app , textvariable=year_var,values=years)
year_txt.place(x=20,y=395,height=30,width=150)
CPU_lbl=Label(super_app,text="CPU",font="Arial")
CPU_lbl.place(x=230,y=430)
CPU_txt=Entry(super_app)
CPU_txt.place(x=230,y=455,height=30,width=150)
hardisk_lbl=Label(super_app,text="Hard disk",font="Arial")
hardisk_lbl.place(x=440,y=430)
hardisk_txt=Entry(super_app)
hardisk_txt.place(x=440,y=455,height=30,width=150)
screen_lbl=Label(super_app,text="Screen",font="Arial")
screen_lbl.place(x=660,y=430)
screen_txt=Entry(super_app)
screen_txt.place(x=660,y=455,height=30,width=150)
cell_lbl=Label(super_app,text="Cellular Network",font="Arial")
cell_lbl.place(x=230,y=500)
cell_txt=Entry(super_app)
cell_txt.place(x=230,y=525,height=30,width=150)
cores_lbl=Label(super_app,text="Number of cores",font="Arial")
cores_lbl.place(x=440,y=500)
cores_txt=Entry(super_app)
cores_txt.place(x=440,y=525,height=30,width=150)
cam_lbl=Label(super_app,text="Camera resolution",font="Arial")
cam_lbl.place(x=660,y=500)
cam_txt=Entry(super_app)
cam_txt.place(x=660,y=525,height=30,width=150)
var1=tk.StringVar()
var1.set(None)
def select_laptop():
    var1.set("Laptop")
    cell_txt["state"] = "disabled"
    cores_txt["state"] = "disabled"
    cam_txt["state"] = "disabled"
    CPU_txt["state"] = "normal"
    hardisk_txt["state"] = "normal"
    screen_txt["state"] = "normal"
    smartphone_button.deselect()
    global  original_color
    original_color=laptop_button.cget("foreground")
    laptop_button.config(foreground="red")
    smartphone_button.config(foreground=original_color)


def select_smartphone():
    var1.set("Smartphone")
    cell_txt["state"] = "normal"
    cores_txt["state"] = "normal"
    cam_txt["state"] = "normal"
    CPU_txt["state"] = "disabled"
    hardisk_txt["state"] = "disabled"
    screen_txt["state"] = "disabled"
    laptop_button.deselect()
    original_color=smartphone_button.cget("foreground")
    smartphone_button.config(foreground="blue")
    laptop_button.config(foreground=original_color)

laptop_button=tk.Radiobutton(super_app,text="Laptop",font="Arial",variable=var1,value="Laptop",command=select_laptop)
laptop_button.place(x=20,y=460)
smartphone_button=tk.Radiobutton(super_app,text="Smartphone",font="Arial",variable=var1,value="Smartphone",command=select_smartphone)
smartphone_button.place(x=20,y=510)
def add_new_product():
    if var1.get()=="Laptop":
        new_prod1=Laptop(id_text.get(),brand_txt.get(),model_txt.get,year_txt.get()
                         ,price_txt.get(),CPU_txt.get(),hardisk_txt.get(),screen_txt.get())
        if id_text.get()=="":
          id_text.config(bg="red")
        elif brand_txt.get()=="":
            brand_txt.config(bg="red")
        elif model_txt.get()=="":
            model_txt.config(bg="red")
        elif year_txt.get()=="":
            year_txt.config(bg="red")
        elif price_txt.get()=="":
            price_txt.config(bg="red")
        elif CPU_txt.get()=="":
            CPU_txt.config(bg="red")
        elif hardisk_txt.get()=="":
            hardisk_txt.config(bg="red")
        elif screen_txt.get()=="":
            screen_txt.config(bg="red")
        elif store.get_product(int(id_text.get())) is not None:
            messagebox.showerror('ERROR', "ID already exist")
        elif id_text.get().isalpha():
            messagebox.showerror('ERROR',"ID must be in numbers")
        elif price_txt.get().isalpha():
            messagebox.showerror('ERROR',"price must be in numbers")
        elif hardisk_txt.get().isalpha():
            messagebox.showerror('ERROR',"hard disk must be in numbers")
        elif screen_txt.get().isalpha():
            messagebox.showerror('ERROR',"screen size must be in numbers")
        else:
            store.add_product(new_prod1)
            messagebox.showinfo(message=f"product id:{id_text.get()}\nbrand:{brand_txt.get()}\nmodel:{model_txt.get()}"
                                        f"\nyear:{year_txt.get()}\nprice:{price_txt.get()}\nCPU:{CPU_txt.get()}\n"
                                        f"hard disk:{hardisk_txt.get()}\nscreen:{screen_txt.get()} \nis added to the store")
            id_text.config(background="white")
            brand_txt.config(background="white")
            model_txt.config(background="white")
            year_txt.config(background="white")
            price_txt.config(background="white")
            CPU_txt.config(background="white")
            hardisk_txt.config(background="white")
            screen_txt.config(background="white")
            id_text.delete(0,END),brand_txt.delete(0,END),model_txt.delete(0,END),year_txt.delete(0,END),
            price_txt.delete(0,END),CPU_txt.delete(0,END),hardisk_txt.delete(0,END),screen_txt.delete(0,END)
    if var1.get()=="Smartphone":
        new_prod2=Smartphone(id_text.get(),brand_txt.get(),model_txt.get(),year_txt.get()
                         ,price_txt.get(),cell_txt.get(),cores_txt.get(),cam_txt.get())
        if id_text.get()=="":
          id_text.config(bg="red")
        elif brand_txt.get()=="":
            brand_txt.config(bg="red")
        elif model_txt.get()=="":
            model_txt.config(bg="red")
        elif year_txt.get() == "":
            year_txt.config(background='red')
        elif price_txt.get()=="":
            price_txt.config(bg="red")
        elif cell_txt.get()=="":
            cell_txt.config(bg="red")
        elif cores_txt.get()=="":
            cores_txt.config(bg="red")
        elif cam_txt.get()=="":
            cam_txt.config(bg="red")
        elif store.get_product(int(id_text.get())) is not None:
            messagebox.showerror('ERROR', "ID already exist")
        elif id_text.get().isalpha():
            messagebox.showerror('ERROR',"ID must be in numbers")
        elif price_txt.get().isalpha():
            messagebox.showerror('ERROR',"price must be in numbers")
        elif cores_txt.get().isalpha():
            messagebox.showerror('ERROR',"number of cores must be in numbers")
        elif cam_txt.get().isalpha():
            messagebox.showerror('ERROR',"camera resolution  must be in numbers")
        else:
            store.add_product(new_prod2)
            messagebox.showinfo(message=f"product id:{id_text.get()}\nbrand:{brand_txt.get()}\nmodel:{model_txt.get()}"
                                        f"\nyear:{year_txt.get()}\nprice:{price_txt.get()}\ncell net:{cell_txt.get()}\n"
                                        f"number of cores{cores_txt.get()}\ncamera resolution:{cam_txt.get()} \nis added to the store")
            id_text.config(background="white")
            brand_txt.config(background="white")
            model_txt.config(background="white")
            year_txt.config(background="white")
            price_txt.config(background="white")
            cell_txt.config(background="white")
            cores_txt.config(background="white")
            cam_txt.config(background="white")
            id_text.delete(0,END),brand_txt.delete(0,END),model_txt.delete(0,END),year_txt.delete(0,END),
            price_txt.delete(0,END),cell_txt.delete(0,END),cores_txt.delete(0,END),cam_txt.delete(0,END)

create_button=tk.Button(super_app,text="create",padx="20", pady="5",command=add_new_product)
create_button.config(fg="purple",font=("Arial",12),relief="solid",highlightcolor="purple",highlightbackground="purple",highlightthickness=3)
create_button.place(x=660,y=575)






super_app.mainloop()