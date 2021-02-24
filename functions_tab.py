import mysql.connector
from tabulate import tabulate
import sys
import os

#CLEAR FUNCTION
def clear():
    os.system('clear')

#CONNECTION
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="Project",
    auth_plugin='mysql_native_password',
    autocommit = True)



#PRODUCT FUNCTION
def read_product():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM product")
    file = mycursor.fetchall()
    print(tabulate(file, headers=["Product_ID","Product_Name", "Product_Price"],   tablefmt='pretty'))


#COURIER FUNCTION
def read_courier():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM courier")
    file = mycursor.fetchall()
    print(tabulate(file, headers=["Courier_ID","Courier_Name", "Courier_Number"],   tablefmt='pretty'))

#ORDER FUNCTION
def read_orders():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM orders")
    file = mycursor.fetchall()
    print(tabulate(file, headers=["Order_ID","Customer_Name", "Customer_Address", "Customer_Number","Order_Status","Courier"],   tablefmt='pretty'))    


#PRODUCT MENU
def product_menu():
    print('''Product Menu
    Enter 0 to return to Main Menu
    Enter 1 to print Products
    Enter 2 to add new Product
    Enter 3 to update Products
    Enter 4 to delete Products  ''')

#COURIER MENU        
def courier_menu():
    print('''Courier Menu
    Enter 0 to return to Main Menu
    Enter 1 to print Courier
    Enter 2 to add new Courier
    Enter 3 to update Courier
    Enter 4 to delete Courier  ''') 

#ORDER MENU        
def order_menu():
    print('''Order Menu
    Enter 0 to return to Main Menu
    Enter 1 to print Orders
    Enter 2 to add new Order
    Enter 3 to update Order Status
    Enter 4 to delete Order
    Enter 5 to Update Order  ''') 



#MAIN MENU
def main_menu():    
    print( '''
                                           
                               )  (
                              (  ) )
                               ) ( (
                             _________
                          .-'---------|  
                         ( C|/\/\/\/\/|      WELCOME TO CITY CAFFE
                          '-./\/\/\/\/|
                            '_________'
                             '-------'
    MAIN MENU                                    
    Enter 0 to Save & exit
    Enter 1 to see Product Menu
    Enter 2 to see Courier Menu
    Enter 3 to see Orders Menu
    ''')
