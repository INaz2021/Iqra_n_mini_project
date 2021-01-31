import sys

print('Welcome to the app!')
print('Enter 0 to exit: ')
print ('Enter 1 to see Menu: ')

products = ['Coke','Salad', 'Burger','Chocolate','Crisps','Water']

while True:
  value = int(input("Select a menu option:"))
  if value == 0:
   sys.exit(0)

  elif value == 1:
    print('Press 0 to go to Main menu')
    print('Press 1 to see Products')
    print('Press 2 to add a Product')
    print('Press 3 to Update a Product')
    print('Press 4 to delete a Product')

  while True:
    value = int(input("Select a menu option:"))
    if value == 0:
     break

    elif value == 1:
      print(products)

    elif value == 2:
      add = str(input("Please enter product name to add: "))
      products.append(add)
      print(products)

    elif value == 3:
      x = str(input("Enter name of product for update: "))
      y = str(input("Enter name of new product: "))
      products=[p.replace ( x, y) for p in products]
      print(products)

    elif value == 4:
      print('Enter Index of product you want to delete: ')
      products.remove (products[int(input())])
      print(products)