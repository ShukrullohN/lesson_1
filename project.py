from classes import Base
from db_connect import Database
def enter():
    se = input("""
        1. Login
        2. Register
    """)
    
    if se == "1":
        return login()

    elif se =="2":
        return register()
    
    else:
        print("Error!")
        return enter()

def login():
    sr = input("""
        1. Customer
        2. Seller
    """)
    if sr == "1":
        email = input("Enter email:")
        password = input("Enter password: ")
        data = Base.select("customer")
        for i in data:
            if i[3] == email and i[4] == password:
                return customer.customer(email, password)
            else:
                print("Error")
                return enter()

    elif sr == "2":
        email = input("Enter email:")
        password = input("Enter password: ")
        data = Base.select("seller")
        for i in data:
            if i[3] == email and i[4] == password:
                return seller.seller(email, password)
            else:
                print("Error")
                return enter()        
    
def register():
    ser = input("""
    1. Customer
    2. Seller
    """)
    if ser == "1":
        first_name = input("First name :")
        last_name = input("Last name :")
        email = input("email:")
        password = input("password :")
        query = f"insert into customer(first_name, last_name, email, password) values('{first_name}', '{last_name}', '{email}', '{password}');"
        print(Database.connect(query, "insert"))
        return customer.customer(email, password)

    if ser == "2":
        first_name = input("First name :")
        last_name = input("Last name :")
        email = input("email:")
        password = input("password :")
        query = f"insert into seller(first_name, last_name, email, password) values('{first_name}', '{last_name}', '{email}', '{password}');"
        print(Database.connect(query, "insert"))
        return seller.seller(email, password)


if __name__ == "__main__":
    enter()