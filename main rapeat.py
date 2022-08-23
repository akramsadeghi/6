from ast import Delete
from cgi import print_environ
from itertools import product
from os import remove
from queue import Empty
from pyfiglet import Figlet

def show_list():
    for i in range(len(PRODUCTS)):
        print(PRODUCTS[i])

def tekrar():
    z= input("aya mikhahid be kar edameh dahid?(y or n)....")
    while z=="y" :
        show_menu()
        choice = int(input('please choose a number :  '))        

def add_product():
    
    myfile1 = open('database.txt','r+')
    data = myfile1.read()
    prouduct_list = data.split('\n')
    a = len(prouduct_list)
    n = int(input('How many goods do you add?  '))
    for i in range(n):
       
        code = i+1+a #input(' kala code : ') 
        name = input(' kala name :  ')
        while name in data:
            print("kala tekrari hast")
            print("be edit bravid")
            name = input(' kala name :  ')
        price = input(' kala price :  ')
        number = input(' kala number :  ') 
        mydict1 = {}
        mydict1['id'] = code
        mydict1['name'] = name
        mydict1['price'] = price
        mydict1['count'] = number
        PRODUCTS.append(mydict1)
        ss=[]
        ss.append(code)
        ss.append(name)
        ss.append(price)
        ss.append(number)
        print(ss)
        myfile1.write('\n'+str(ss[0])+','+str(ss[1])+','+str(ss[2])+','+str(ss[3]))
        
    for i in range(len(PRODUCTS)):
        print(PRODUCTS[i])
    

def edit_product():
     myfile2 = open('database.txt','r+')
     data = myfile2.read()
     a=input('Which product are you editing?')
     b=int(a)
     if a in data:
        print("ok")
        prouduct_list = data.split('\n')
        
         
        print(prouduct_list[b-1])      

     else:
        print("no")    
                
     prouduct_info = prouduct_list[b-1].split(',')
     mydict2 = {}
     mydict2['id'] = prouduct_info[0]
     mydict2['name'] = prouduct_info[1]
     mydict2['price'] = prouduct_info[2]
     mydict2['count'] = prouduct_info[3]

     n1= input("aya name kala ra taghir midahid? y or no")
     if n1=="y":
        mydict2['name'] = input("new name")
     n2= input("aya ghemat kala ra taghir midahid? y or no")
     if n2=="y":   
       mydict2['price'] = input("new price")
     n3= input("aya tedad kdadala ra taghir midahid? y or no")
     if n3=="y":    
        mydict2['count'] = input("new count")
     print(mydict2)
     print(prouduct_info)
     

     PRODUCTS.append(prouduct_info)

     prouduct_list[b-1] = [mydict2['id'] ,  mydict2['name'],mydict2['price'],mydict2['count']]  
     print(prouduct_list[b-1]) 
     prouduct_list[b-1] == data[b-1]
     myfile2.write (data[b-1])
     for i in range(len(PRODUCTS)):
        print(PRODUCTS[i])
                                    

def search():
# این قسمت به دلیل اینکه توانایی چاپ یک ردیف کالا را در جستجوی عبارت ندارد ناقص است.
     myfile2 = open('database.txt','r+')
     data = myfile2.read()
     a=input('aya az tarigh kode kala jostoju mikonid?(y or n')

     if a=="y" :
        c=input("kode ra vared konid? ")
        b=int(c)
        if c in data:
            print("ok")
            prouduct_list = data.split('\n')
            print(prouduct_list[b-1])      

        else:
            print("no") 
     else:
        c=input("ebart jostoju ra vard konid?  ")
        if c in data:
            print("ok")
            prouduct_list = data.split('\n')
            print(prouduct_list[c])      

        else:
            print("no")          

def main():
    choice = int(input('please choose a number :  '))
            

    if choice ==1:
        add_product()
    elif choice == 2:
        edit_product()
    elif choice == 3:
        delete_product()
    elif choice == 4:
        search()    
    elif choice == 5:
        show_list()
    elif choice == 6:
        pass
    elif choice == 7:
        pass

def delete_product():   #حذف نمی شود.
    myfile2 = open('database.txt','r+')
    data = myfile2.read()
    a=input('Which product are you deleting?')
    b=int(a)
    if a in data:
        print("ok")
        prouduct_list = data.split('\n')
        print(prouduct_list[b-1]) 
        del prouduct_list[b-1]
        print(data)
    else:
        print("no")

    #print(mydict2)
     

    #PRODUCTS.append(mydict2)

    #prouduct_list[b-1] = [mydict2['id'] ,  mydict2['name'],mydict2['price'],mydict2['count']]  
    #print(prouduct_list[b-1]) 
    #myfile2.write (data[b-1])         

    for i in range(len(PRODUCTS)):
        print(PRODUCTS[i]) 

 

def show_menu():
    print('1-Add Product')
    print('2-Edit Product')
    print('3-Delete Product')
    print('4-Search')
    print('5-Show List')
    print('6-Buy')
    print('7-Exit')
    
def tekrar():
    repeat="y"
    while repeat == "y":
        repeat=input("aya edameh midahid?  (y or n)")
        if repeat=="y":
            show_menu()
            main()
                


def load():    
    print("loading...")
    myfile = open('database.txt','r+')
    data = myfile.read()
    prouduct_list = data.split('\n')
    a = len(prouduct_list)
    
    for i in range(len(prouduct_list)):
        prouduct_info = prouduct_list[i].split(',')
        mydict = {}
        mydict['id'] = prouduct_info[0]
        mydict['name'] = prouduct_info[1]
        mydict['price'] = prouduct_info[2]
        mydict['count'] = prouduct_info[3]
        PRODUCTS.append(mydict)
    print("welcome")
    print(len(prouduct_list))
PRODUCTS = []

load()
f = Figlet(font='standard')
print (f.renderText('hajji  market'))
show_menu()
main()
tekrar()













