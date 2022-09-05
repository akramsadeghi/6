from ast import Delete, Not
from cgi import print_environ
from itertools import product
from os import remove
from queue import Empty
from pyfiglet import Figlet


myfile = open('database.txt','r+')
data = myfile.read()
prouduct_list = data.split('\n')
PRODUCTS=[]


def show_list():
    for i in range(len(PRODUCTS)):
        print(PRODUCTS[i])
        

def tekrar():
    z= input("aya mikhahid be kar edameh dahid?(y or n)....")
    while z=="y" :
        show_menu()
        choice = int(input('please choose a number :  ')) 
    

def add_product():
    
    n = int(input('How many goods do you add?  '))
    for i in range(n):
       
        code = i+1+a  
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
    for i in range(len(PRODUCTS)):
        print(PRODUCTS[i])
    

def edit_product():
    a=input('Which product are you editing?')
    mydictn2 = {}
    if a in data:
        for i in range(len(PRODUCTS)):
            mydictn2 = PRODUCTS[i]
            if a==mydictn2['id'] or a==mydictn2['name']:
                print(PRODUCTS[i])
                n1= input("aya name kala ra taghir midahid? y or no")
                if n1=="y":
                    mydictn2['name'] = input("new name")
                n2= input("aya ghemat kala ra taghir midahid? y or no")
                if n2=="y": 
                    mydictn2['price'] = input("new price") 
                n3= input("aya tedad kdadala ra taghir midahid? y or no")
                if n3=="y":
                    mydictn2['count'] = input("new count")       
                PRODUCTS[i] = mydictn2 
                print(PRODUCTS[i])
            else:
                print("no")
    # b=int(a)
     #if a in data:
      #  print("ok")
     #else:
      #  print("no")    
     #mydict2 = {}
     #mydict2 = PRODUCTS[b-1]
     #print('*********'+mydict2+'**********')          

    

                                    

def search():
     myfile2 = open('database.txt','r+')
     data = myfile2.read()
     a=input('aya az tarigh kode kala jostoju mikonid?(y or n')

     if a=="y" :
        c=input("kode ra vared konid? ")
        b=int(c)
        if c in data:
            print("ok")
            print(PRODUCTS[b-1])      

        else:
            print("no")
     else:# اینجا مشکل دارد.
        c=input("name kala ra vard konid?  ")
        #n=str(c)
        mydictn = {}
        if c in data:
            for i in range(len(PRODUCTS)):
                mydictn = PRODUCTS[i]
                if c==mydictn['name']:
                    print(PRODUCTS[i])
        else:
            print("no")    
    
def buy():
    v='y'
    while v =='y':        
        x=input('what do you buy?  ')
        if x in data:
            print("ok,in kala dar froshgah hast. ")
            mydictn = {}
            for i in range(len(PRODUCTS)):
                mydictn = PRODUCTS[i]
                if x==mydictn['name']:
                    print(PRODUCTS[i])
                    a = mydictn['id']
                    b = mydictn['name'] 
                    c = mydictn['price']
                    d = mydictn['count']
                    cc = int(c)
                    dd = int(d)
                    number = int(input('chand adad az in kala ra kharid mikonid?...'))
                    q = dd-number
                    while q<0 :
                        print("mojoodi kala kafi nist, lotfan tedad kamtaari entekhab konid.")
                        number = int(input('chand adad az in kala ra kharid mikonid?...'))
                        q = dd-number
                    else:
                        total_price = number*cc
                        mydictn['count'] = dd - number
                        print("esme kala: ",x,
                              "tedad kala: ",number,
                              "ghemat vahed: ",c,
                              "total_price: ",total_price,)
                        PRODUCTS[i] = mydictn
                        print(PRODUCTS[i])                                                
        else:
            print("in kala dar froshgah nist. ")
        v = input('aya kalay digar entekhab mikonid? y or n...')    
    else:
        print("tankyou ")


def save_exit ():
    f = open("database.txt", "w") 
    for i in range(len(PRODUCTS)):
        ss = list(PRODUCTS[i].values())
        print(PRODUCTS[i])
        f.write('\n'+ str(ss[0])+','+str(ss[1])+','+str(ss[2])+','+str(ss[3]))


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
        buy()
    elif choice == 7:
        save_exit ()
        

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
    print('7-Exit & save')
    
def tekrar():
    repeat="y"
    while repeat == "y":
        repeat=input("aya edameh midahid?  (y or n)")
        if repeat=="y":
            show_menu()
            main()
                

    

#def load():
print("loading...")
myfile = open('database.txt','r+')
data = myfile.read()
prouduct_list = data.split('\n')
a = len(prouduct_list)
PRODUCTS = []   
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


#load()
f = Figlet(font='standard')
print (f.renderText('hajji  market'))
show_menu()
main()
tekrar()
