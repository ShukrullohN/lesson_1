from classes import Base
from db_connect import Database


def profile(email, password):
    services = input("""
        1. Edit
        2. Log out
        0. Back

    """)
    if services == "1":
        ser = input("""
        1. First_name
        2. Last_name
        3. email
        4. Password
        0. Back
              """)
        if ser == "1":
            old_data = input("Enter old data")
            new_data = input("Enter new data")

            data = Base.update("seller", "first_name", old_data, new_data)
            return profile(email, password)

        elif ser == "2":
            old_data = input("Enter old data")
            new_data = input("Enter new data")
            
            data = Base.update("seller", "last_name", old_data, new_data)
            return profile(email, password)

        elif ser == "3":
            old_data = input("Enter old data")
            new_data = input("Enter new data")
            data = Base.update("seller", "email", old_data, new_data)
            return profile(email, password)

        elif ser == "4":
            old_data = input("Enter old data")
            new_data = input("Enter new data")
            data = Base.update("seller", "password", old_data, new_data)
            return profile(email, password)

                    
        
        elif ser == "0":
            return seller(email, password)

        else:
            print("Error")
            return seller(email, password)    
       
    elif services == "0":
        return seller(email, password)

    elif services == "2":
        return log_out(email, password)

    else:
        print("Error")
        return profile(email, password)

def log_out(email, password):
    ser = input("""
        Are you sure to log out
        1. Yes
        2. Back
    """)      
    if ser == "1":
        Base.delete("seller", "email", email)

def my_products(email, password):
    data = Base.select("seller")
    for i in data:
        print(f"""
            Product_id : {i[5]}
        """)
    
    ser = input("""
        1. Add product
        0. Back
    """)

    if ser == "1":
        id = input("Enter product id")
        query = f"insert into seller(product_id) values({id});"
        print(Database.connect(query,"insert" ))
        return seller(email, password)
        
    elif ser == "0":
        return seller(email, password)

    else:
        print("Error")    
        return seller(email, password)



def log_out(email, password):
    ser = input("""
        Are you sure to log out
        1. Yes
        2. Back
    """)      
    if ser == "1":
        Base.delete("seller", "email", email)


def orders(email, password):
    data = Base.select("seller")
    for i in data:
        print(f"""
        ID : {i[0]}
        Product_ID : {i[1]}
        Customer_ID : {i[2]}
        status: {i[3]}

        """)
    
    b = input("""
        0. Back
        """)

    if b== "0":
        return seller(email, password)    

def seller(email, password):
    services = input("""
        1.my products
        2.orders
        3.profile
        4.log out
    """)
    if services =="1":
        return my_products(email, password)

    elif services =="2":
        return orders(email, password)

    elif services =="3":
        return profile(email, password)

    elif services =="4":
        return log_out(email, password)
