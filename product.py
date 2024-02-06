import os 
import mysql.connector 
mydb= mysql.connector.connect(host="localhost",user="root",password="mysql",database="stock") 
mycursor=mydb.cursor() 
                                                                                     
def project_mnmg(): 
                    print("1. ADD NEW PRODUCT") 
                    print("2. LIST PRODUCT") 
                    print("3. UPDATE PRODUCT")  
                    print("4. END") 
                    p=int(input("ENTER YOUR CHOICE=")) 
                    if p==1: 
                        mydb= mysql.connector.connect(host="localhost",user="root",password="mysql", database="stocks") 
                        mycursor=mydb.cursor() 
                        code=int(input("\t\t Enter product code:")) 
                        name=input("\t\t Enter product name:") 
                        qty=int(input("\t\t Enter product quantity:")) 
                        price=float(input("\t\t Enter price of product:")) 
                        cat=input("\t\t Enter product category:") 
                        sql="INSERT INTO PRODUCTS(pcode,pname,pprice,pqty,pcat) values(%s,%s,%s,%s,%s);" 
                        val=(code,name,price,qty,cat) 
                        mycursor.execute(sql,val) 
                        mydb.commit() 
                        project_mnmg() 
                    elif p==2: 
                        print("\t\t\t List of all products") 
                        mydb=mysql.connector.connect(host="localhost", user="root", password="mysql",database="stocks") 
                        mycursor=mydb.cursor() 
                        z="SELECT* from PRODUCTS;" 
                        mycursor.execute(z) 
                        print("\t\t\t PRODUCT DETAILS") 
                        print("\t\t code     name   price   quantity   category") 
                        for i in mycursor: 
                                           print("\t\t",i[0],"\t", i[1], "\t", i[2], "\t", i[3], "\t", i[4]) 
                        project_mnmg() 
                    elif p==3: 
                            mydb=mysql.connector.connect(host="localhost", user="root", password="mysql",database="stocks") 
                            mycursor=mydb.cursor() 
                            code=int(input("Enter the product code")) 
                            qty=int(input("Enter the new quantity:")) 
                            price=int(input("Enter INCREASED price of product")) 
                            y="UPDATE PRODUCTS SET pqty=%s,pprice=pprice+%s WHERE pcode=%s;" 
                            value=(qty,price,code) 
                            mycursor.execute(y,value) 
                            mydb.commit() 
                            print("\t\t Products detail updated") 
                            project_mnmg() 
                    else: 
                        print("THANKS FOR USING THIS PROGRAM") 
                        print("CREDITS FOR THIS PROGRAM") 
                        print("\t\t\t TANUJ MEHTA") 
                        print("\t\t\t VIVEK CHADGAL") 
                        print("SPECIAL CREDITS TO: MRS. SEEMA") 
                         
 
 
print("PRODUCT MANAGEMENT SYSTEM") 
star="show tables;" 
mycursor.execute(star) 
for j in mycursor: 
        print(j) 
project_mnmg()                                 
 
