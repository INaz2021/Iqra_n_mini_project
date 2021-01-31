import sys
import os

print('Welcome to the app!')
print('Enter 0 to exit: ')
print ('Enter 1 to see Product Menu:    ')
print('Enter 2 to see Courier Menu:     ')
prod = []
cour = []
item = ''


def product():
  prod.clear()
  with open('product.txt', 'r') as file:
    for line in file:
      prod.append(line.rstrip())


def courier():      
   with open('courier.txt', 'r') as file:
    for line in file:
      cour.append(line.rstrip())    




while True:
  value = int(input("Enter number:    "))

  if value == 0:
    sys.exit(0)

  elif value == 1:
    print('Product Menu   0 | 1 | 2 | 3 | 4')

############
    
    while True:
      value = int(input("Enter number for Product Menu:     "))
      if value == 0:
        break

      elif value == 1:
        product()
        print(prod)

      elif value == 2:
        add = str(input("Please enter product name to add: "))
        with open ('product.txt','a+') as file:
          file.write(add + '\n')

      elif value == 3:
        x = str(input("Enter name of product for update: "))
        y = str(input("Enter name of new product: "))
        prod=[p.replace ( x, y) for p in prod]
        print(prod)
        with open ('product.txt','w+') as file:
          for item in prod:
            file.write(item + '\n')

      elif value == 4:
        print('Enter product you want to delete: ')
        del prod[int(input())]
        print(prod)
        with open ('product.txt','w+') as file:
          for item in prod:
            file.write(item + '\n')
      else:
        print('you enter wrong number')

##########
  elif value == 2:
    print('Courier menu  0 | 1 | 2 | 3 | 4')  

    while True:
          
      value = int(input("Enter number Courier:     "))
      if value == 0:
        break
    
      elif value == 1:
        courier()
        print(cour)

      elif value == 2:
        add = str(input("Please enter courier name to add: "))
        with open ('courier.txt','a+') as file:
          file.write(add + '\n')

      elif value == 3:
        x = str(input("Enter name of courier for update: "))
        y = str(input("Enter name of new courier: "))
        cour=[p.replace ( x, y) for p in cour]
        print(cour)
        with open ('courier.txt','w+') as file:
          for item in cour:
            file.write(item + '\n')

      elif value == 4:
        print('Enter courier you want to delete: ')
        del cour[int(input())]
        print(cour)
        with open ('courier.txt','w+') as file:
          for item in cour:
            file.write(item + '\n')
      else:
        print('you enter wrong number')
