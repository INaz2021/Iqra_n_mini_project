from functions import *

while True:

#MAIN MENU
    def main_function():    
        print( '''
                          
                                 )  (
                                (  ) )
                                 ) ( (
                                _________
                             .-'---------|  
                            ( C|/\/\/\/\/|     WELCOME TO CITY CAFFE
                             '-./\/\/\/\/|
                               '_________'
                                '-------'
    MAIN MENU                                    
    Enter 0 to Save & exit
    Enter 1 to see Product Menu
    Enter 2 to see Courier Menu
    Enter 3 to see Orders
    ''')
    main_function()

    value = int(input("Enter number from Main Menu:    "))

#EXIT
    if value == 0:
        print('Application Close Successfully')
        sys.exit(0)

#PRODUCT MENU
    elif value == 1:
        clear()
        def product_menu():
            print('''Product Menu
            Enter 0 to return to Main Menu
            Enter 1 to print Products
            Enter 2 to add new Product
            Enter 3 to update Products
            Enter 4 to delete Products  ''')
        product_menu()    


#PRODUCT
    
        while True:
            value = int(input("Enter number for Product Menu:    "))

#RETURN TO MAIN MENU
            if value == 0:
                main_function()
                clear()
                break

#PRODUCT PRINT
            elif value == 1:
                clear()
                read_product()
                product_menu()


#PRODUCT ADD
            elif value == 2:
                clear()
                product_menu()
                mycursor = mydb.cursor()
                sql = "INSERT INTO product (product_name, product_price) VALUES (%s, %s)"
                val = (str(input('Enter Product Name:    ')), int(input('Enter Product Price:    ')))
                mycursor.execute(sql, val)
                print('Row added successfully')


#PRODUCT UPDATE
            elif value == 3:
                clear()
                product_menu()
                mycursor = mydb.cursor()
                prod_id=int(input('Enter Product ID to Update or 0 to Cancel:    '))
                if prod_id == 0:
                    product_menu()
                    break

                else:
                    print(f'Here is the row number to update {prod_id}')    

                    value= str(input("Press Enter to SKIP or Enter 1 to Update Product Name:    "))

                    if (len(value)) == 0:
                        print('Product name not changed')

                    elif (len(value)) != 0:
                        sql = "UPDATE product SET product_name = %s where product_id = %s";
                        val = (str(input("Enter New Product Name:    ")),prod_id)
                        mycursor.execute(sql, val)  
                        print('Product name updated')

                    value= str(input("Press Enter to SKIP and 1 to Update Product Price:    "))    
                    if(len(value)) == 0:
                        print('Product price not changed')

                            
                    elif (len(value)) != 0:
                        sql = "UPDATE product SET product_price = %s WHERE product_id = %s"
                        val = (str(input("Enter new price:    ")), prod_id)
                        mycursor.execute(sql, val)  
                        print('Product price updated')    
                    else:
                        break


#PRODUCT DELETE
            elif value == 4:
                clear()
                product_menu()
                del_value = int(input('Enter 0 to Exit Or 1 to Delete Product :     '))
                if del_value == 0:
                    exit

                elif del_value == 1:
                    mycursor = mydb.cursor()
                    val = (str(input('Enter Product_Id to delete Product row:    ')))
                    sql = "DELETE FROM product WHERE product_id = %s"  %val
                    mycursor.execute(sql,val)
                    print('Row deleted successfully')
            else:
                print('You Enter Invalid Number')   


#COURIER  
    
    elif value == 2:
        clear()

#COURIER MENU        
        def courier_menu():
            print('''Courier Menu
            Enter 0 to return to Main Menu
            Enter 1 to print Courier
            Enter 2 to add new Courier
            Enter 3 to update Courier
            Enter 4 to delete Courier  ''') 
        courier_menu()    

        while True:

            value = int(input("Enter number From Courier Menu:    "))

#RETURN TO MAIN MENU
            if value == 0:
                main_function()
                break


#COURIER PRINT
            elif value == 1:
                clear()
                read_courier()
                courier_menu()


#COURIER ADD
            elif value == 2:
                clear()
                courier_menu()
                mycursor = mydb.cursor()
                sql = "INSERT INTO courier (courier_name, courier_contact) VALUES (%s, %s)"
                val = (str(input('Enter Courier Name:    ')), int(input('Enter Courier Contact:    ')))
                mycursor.execute(sql, val)
                print('Row added successfully')  



#COURIER UPDATE
            elif value == 3:
                clear()
                courier_menu()
                mycursor = mydb.cursor()
                cour_id=int(input('Enter Courier Id to Update or 0 to Cancel:    '))
                if cour_id == 0:
                    courier_menu()
                    break

                else:
                    print(f'Here is the row number to update {cour_id}')    

                    value= str(input("Press Enter to SKIP or Enter 1 to Update Courier Name:    "))

                    if (len(value)) == 0:
                        print('Courier name not changed')

                    elif (len(value)) != 0:
                        sql = "UPDATE courier SET courier_name = %s where courier_id = %s";
                        val = (str(input("Enter New Courier Name:    ")),cour_id)
                        mycursor.execute(sql, val)  
                        print('Courier name updated')

                    value= str(input("Press Enter to SKIP and 1 to Update Courier Contact:    "))    
                    if(len(value)) == 0:
                        print('Courier Contact details not changed')

                            
                    elif (len(value)) != 0:
                        sql = "UPDATE courier SET courier_contact = %s WHERE courier_id = %s"
                        val = (str(input("Enter New Contact Details:    ")), cour_id)
                        mycursor.execute(sql,val)  
                        print('Contact details updated')    
                    else:
                        break


#COURIER DELETE
            elif value == 4:
                clear()
                courier_menu()
                del_value = int(input('Enter 0 to Exit Or 1 to Delete  Courier :     '))
                if del_value == 0:
                    exit

                elif del_value == 1:
                    mycursor = mydb.cursor()
                    val = (str(input('Enter Courier to delete row:    ')))
                    sql = "DELETE FROM courier WHERE courier_id = %s"  %val
                    mycursor.execute(sql,val)
                    print('Row deleted successfully')
            else:
                print('You Enter Invalid Number')



#ORDER
    elif value == 3:
        clear()

#ORDER MENU        
        def order_menu():
            print('''Order Menu
            Enter 0 to return to Main Menu
            Enter 1 to print Orders
            Enter 2 to add new Order
            Enter 3 to update Order
            Enter 4 to delete Order  ''') 
        order_menu()    

        while True:

            value = int(input("Enter number from Orders Menu:     "))

#RETURN TO MAIN MENU            
            if value == 0:
                main_function()
                break


#ORDER PRINT
            elif value == 1:
                clear()
                read_orders()
                order_menu()


#ORDER ADD
            elif value == 2:
                clear()
                order_menu()
                mycursor = mydb.cursor()
                name = str(input("Enter Name of Customer:     "))
                address = str(input("Enter Address of Customer:     "))
                phone = int(input("Enter Contact Detail of Customer:     "))

                value= str(input("Press Enter 0 to cancel and 1 to Add Courier:    "))    
                if(len(value)) == 0:
                    exit

                elif (len(value)) == 1:
                    cour_list()
                    cou_id = int(input("Enter Courier Id:     "))

                while True:
                    value= str(input("Enter Product ID to Add or 0 to Cancel:    "))
                    if(len(value)) == 0:
                        exit

                    elif (len(value)) == 1:
                        sql = "INSERT into orders (items) values %s "
                        #pro_id = int(input("Enter Product Id:     "))
                        mycursor.execute(sql, value)



                    sql =  "INSERT into orders (customer_name, customer_address, customer_contact, courier) values (%s,%s,%s,%s)"
                    val = (name, address, phone, cou_id)
                    mycursor.execute(sql, val)


#ORDER UPDATE STATUS
            elif value == 3:
                clear()
                order_menu()
                mycursor = mydb.cursor()
                Status_list =['Order Accepted','On the way','Delivered']
                ord_id=int(input('Enter Order ID to Update Order Status or 0 to Cancel :    '))
                if ord_id == 0:
                    order_menu()
                    break

                else:
                    print(f'Here is the row number to update {ord_id}')    

                    value= str(input("Press Enter to SKIP or Enter 1 to Update Order Status:    "))

                    if (len(value)) == 0:
                        print('Order Status not changed')

                    elif (len(value)) != 0:
                        sql = "UPDATE orders SET order_status = %s where order_id = %s";
                        ord_status = Status_list[int(input('Enter number to Update Order Status  0: Order Accepted   1: On the way  2: Delivered'))]
                        val = (ord_status,ord_id)
                        mycursor.execute(sql, val)  
                        print('Order Status updated')


#ORDER DELETE
            elif value == 4:
                clear()
                order_menu()
                del_value = int(input('Enter 0 to Exit Or 1 to Delete Order :     '))
                if del_value == 0:
                    exit

                elif del_value == 1:
                    mycursor = mydb.cursor()
                    val = (str(input('Enter Order ID to delete row:    ')))
                    sql = "DELETE FROM orders WHERE order_id = %s"  %val
                    mycursor.execute(sql,val)
                    print('Row Deleted Successfully')



#ORDER UPDATE EACH PROPERTY
            elif value == 5:
                clear()
                order_menu()
                mycursor = mydb.cursor()
                ord_id=int(input('Enter Order ID to Update or 0 to Cancel :    '))
                if ord_id == 0:
                    order_menu()
                    break

                else:
                    print(f'Here is the row number for update {ord_id}')   
                    
                sql = "UPDATE orders set customer_name = CASE when  NOT NULL then customer_name =  %s"  
                name = str(input('Enter new customer Name'))
                val = (sql, ord_id, name)
                mycursor.execute(sql, val)  


                    # for i in ord_id:
                    #     if i == ord_id[0]:

                    #value= str(input("Press Enter to SKIP or Enter 1 to Update Order:    "))

                    
                    # for i in ord_id:
                    #     if i == ord_id[0]:
                            
                    # value= str(input("Press Enter to SKIP or Enter 1 to Update Order:    "))        
                    
                    # if (len(value)) == 0:
                    #     print('Customer Name not changed')
                    # if (len(value)) != 0:
                    #     name = str(input('Enter new Name of Customer'))
                    #     elif 


