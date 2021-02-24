from functions_tab import *
from tabulate import tabulate
clear()
#MAIN MENU
while True:
    main_menu()
    value = int(input("Enter number from Main Menu  0 | 1 | 2 | 3     "))
    


#EXIT
    if value == 0:
        print('Application Close Successfully')
        sys.exit(0)

#PRODUCT
    elif value == 1:
        clear()
        product_menu()
    
        while True:
            value = int(input("Enter number for Product Menu  0:Exit  1:Print  2:Add  3:Update  4:Delete   "))

    #RETURN TO MAIN MENU
            if value == 0:
                clear()
                break

    #PRODUCT PRINT
            elif value == 1:
                read_product()




    #PRODUCT ADD
            elif value == 2:
                clear()
                product_menu()
                mycursor = mydb.cursor()
                sql = "INSERT INTO product (product_name, product_price) VALUES (%s, %s)"
                val = (str(input('Enter Product Name:    ')), float(input('Enter Product Price:    ')))
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
                    print(f'Here is the row number to update    {prod_id}')    

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
                        val = (float(input("Enter new price:    ")), prod_id)
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
                    sql = "DELETE FROM product WHERE product_id = %s" %val
                    mycursor.execute(sql,val)
                    print('Row deleted successfully')
            else:
                print('You Enter Invalid Number')   


#COURIER  
    
    elif value == 2:
        clear()
        courier_menu()

        while True:

            value = int(input("Enter number From Courier Menu   0:Exit  1:Print  2:Add  3:Update  4:Delete    "))

    #RETURN TO MAIN MENU
            if value == 0:
                clear()
                break


    #COURIER PRINT
            elif value == 1:
                clear()
                read_courier()



    #COURIER ADD
            elif value == 2:
                clear()
                courier_menu()
                mycursor = mydb.cursor()
                sql = "INSERT INTO courier (courier_name, courier_contact) VALUES (%s, %s)"
                val = (str(input('Enter Courier Name:    ')), str(input('Enter Courier Contact:    ')))
                mycursor.execute(sql, val)
                print('Row added successfully')  



    #COURIER UPDATE
            elif value == 3:
                clear()
                mycursor = mydb.cursor()
                cour_id=int(input('Enter Courier Id to Update or 0 to Cancel:    '))
                if cour_id == 0:
                    break

                else:
                    print(f'Here is the row number to update    {cour_id}')    

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
                del_value = int(input('Enter 0 to Exit Or 1 to Delete Courier :     '))
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
        order_menu()

        while True:

            value = int(input("Enter number from Orders Menu: 0:Exit  1:Print  2:Add   3:Update Order_Status  4:Delete  5:Update Order      "))

    #RETURN TO MAIN MENU            
            if value == 0:
                clear()
                break


    #ORDER PRINT
            elif value == 1:
                read_orders()



    #ORDER ADD
            elif value == 2:
                clear()
                order_menu()
                mycursor = mydb.cursor()
                
                name = str(input("Enter Name of Customer:     "))
                address = str(input("Enter Address of Customer:     "))
                phone = str(input("Enter Contact Detail of Customer:     "))

                value= str(input("Press Enter to cancel and 1 to Add Courier:    "))    
                if(len(value)) == 0:
                    exit
                elif (len(value)) == 1:
                    read_courier()
                    cou_id = int(input("Enter Courier Id:     "))
                    # if cou_id >=10:
                    #     print('You Entered Invalid Id')
                    #     break
                    sql =  "INSERT into orders (customer_name, customer_address, customer_contact, courier) values (%s,%s,%s,%s)"
                    val = (name, address, phone, cou_id)
                    mycursor.execute(sql, val)

                #product id
                read_product()
                sql1 = "SELECT max(order_id) from orders"
                mycursor.execute(sql1)
                last_orderid = mycursor.fetchall()
                for i in last_orderid:
                    a = int(i[0])
                print("Enter Product Id   ")
                items = [int(x) for x in input().split()]
                for i in range(len(items)):
                    val2= [a, items[i]]
                    sql2 = "INSERT into order_product (order_id,product_id) values (%s,%s)"
                    mycursor.execute(sql2,val2)


                #print as table 
                sql1 = """SELECT o.order_id, o.courier, o.order_status, o.customer_name, o.customer_address, o.customer_contact,
                        GROUP_CONCAT(p.product_id SEPARATOR ' , ') FROM orders o        
                        Left JOIN order_product op on op.order_id = o.order_id
                        JOIN product p on p.product_id = op.product_id
                        GROUP BY op.order_id"""
                mycursor.execute(sql1)
                result= mycursor.fetchall()
                print(tabulate(result, headers=["Order_ID","Courier_ID", "Order_status","Customer_Name","Customer_Address","Customer_Number","Items" ],   tablefmt='pretty'))


        #ORDER UPDATE STATUS
            elif value == 3:
                clear()
                order_menu()
                mycursor = mydb.cursor()
                Status_list =['Ready to Pick','On the way','Delivered']
                ord_id=int(input('Enter Order ID to Update Order Status or 0 to Cancel :    '))
                if ord_id == 0:
                    break

                else:
                    print(f'Here is the row number to update {ord_id}')    

                    value= str(input("Press Enter to SKIP or Enter 1 to Update Order Status:    "))

                    if (len(value)) == 0:
                        print('Order Status not changed')

                    elif (len(value)) != 0:
                        sql = "UPDATE orders SET order_status = %s where order_id = %s"
                        ord_status = Status_list[int(input('Enter number to Update Order Status  0:Ready to Pick   1:On the way  2:Delivered'        ))]
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
                ord_id=int(input('Enter Order Id to Update or 0 to Cancel:    '))
                if ord_id == 0:
                    break

                else:
                    print(f'Here is the row number to update   {ord_id}')    

                #name
                value = str(input("Press Enter to SKIP or Enter 1 to Update Customer Name:    "))
                if (len(value)) == 0:
                    print('Customer name not changed')
                elif (len(value)) != 0:
                    sql = "UPDATE orders SET customer_name = %s where order_id = %s";
                    val = (str(input("Enter New Customer Name:    ")),ord_id)
                    mycursor.execute(sql, val)  
                    print('Customer Name updated')
                
                #address
                value = str(input("Press Enter to SKIP or Enter 1 to Update Customer Address:    "))
                if (len(value)) == 0:
                    print('Customer address not changed')
                elif (len(value)) != 0:
                    sql = "UPDATE orders SET customer_address = %s where order_id = %s";
                    val = (str(input("Enter New Customer Address:    ")),ord_id)
                    mycursor.execute(sql, val)  
                    print('Customer Address updated')

                #contact
                value = str(input("Press Enter to SKIP or Enter 1 to Update Customer Number:    "))
                if (len(value)) == 0:
                    print('Customer Number not changed')
                elif (len(value)) != 0:
                    sql = "UPDATE orders SET customer_contact = %s where order_id = %s";
                    val = (str(input("Enter New Customer Number:    ")),ord_id)
                    mycursor.execute(sql, val)  
                    print('Customer Contact Number updated')    

                #order status
                Status_list =['Ready to Pick','On the way','Delivered']
                value = str(input("Press Enter to SKIP or Enter 1 to Update Order Status:    "))
                if (len(value)) == 0:
                    print('Order Status not changed')
                elif (len(value)) != 0:
                    sql = "UPDATE orders SET order_status = %s where order_id = %s"
                    ord_status = Status_list[int(input('Enter number to Update Order Status  0:Ready to Pick   1:On the way  2:Delivered'       ))]
                    val = (ord_status,ord_id)
                    mycursor.execute(sql, val)  
                    print('Order Status updated')

                #items
                value = str(input("Press Enter to SKIP or Enter 1 to Update Items:    "))
                if (len(value)) == 0:
                    print('Items')
                elif (len(value)) != 0:
                    print("Press Enter Product Id")
                    items = [int(x) for x in input().split()]
                    sql = "DELETE from order_product where order_id = %s"
                    mycursor.execute(sql, (ord_id,))
                    for i in range(len(items)):
                        val= [ord_id,items[i]]
                        sql3 = "INSERT into order_product (order_id,product_id) values (%s,%s)"
                        mycursor.execute(sql3,val)
                        print('Items updated')


                #courier
                value = str(input("Press Enter to SKIP or Enter 1 to Update Courier:    "))
                if (len(value)) == 0:
                    print('Courier not changed')
                elif (len(value)) != 0:
                    read_courier()
                    sql = "UPDATE orders SET courier = %s where order_id = %s";
                    val = (str(input("Enter New Courier:    ")),ord_id)
                    mycursor.execute(sql, val)  
                    print('Courier updated')
            
            else:
                print('You Enter Invalid Number')

    else:
        print('You Entered Invalid Value')
        break            