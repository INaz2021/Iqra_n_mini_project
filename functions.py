import mysql.connector
import sys
import os

#CLEAR FUNCTION
def clear():
    os.system('cls')

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
    mycursor = mydb.cursor(dictionary = True)
    mycursor.execute('SELECT * FROM product')
    file = mycursor.fetchall()
    for row in file:
        for key,value in row.items():
            print(key, ':', value) 
        print(" ")

#COURIER FUNCTION
def read_courier():
    mycursor = mydb.cursor(dictionary = True)
    mycursor.execute('SELECT * FROM courier')
    file = mycursor.fetchall()
    for row in file:
        for key,value in row.items():
            print(key, ':', value) 
        print(" ")

#ORDER FUNCTION
def read_orders():
    mycursor = mydb.cursor(dictionary = True)
    mycursor.execute('SELECT * FROM orders')
    file = mycursor.fetchall()
    for row in file:
        for key,value in row.items():
            print(key, ':', value) 
        print(" ")

#COURIER_LIST FUNCTION
def cour_list():
    mycursor.execute('SELECT * from courier')
    file = mycursor.fetchall()
    for row in file:
        print(row)        
