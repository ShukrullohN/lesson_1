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

            data = Base.update("customer", "first_name", old_data, new_data)
            return profile(email, password)

        elif ser == "2":
            old_data = input("Enter old data")
            new_data = input("Enter new data")
            
            data = Base.update("customer", "last_name", old_data, new_data)
            return profile(email, password)

        elif ser == "3":
            old_data = input("Enter old data")
            new_data = input("Enter new data")
            data = Base.update("customer", "email", old_data, new_data)
            return profile(email, password)

        elif ser == "4":
            old_data = input("Enter old data")
            new_data = input("Enter new data")
            data = Base.update("customer", "password", old_data, new_data)
            return profile(email, password)

                    
        
        elif ser == "0":
            return customer(email, password)

        else:
            print("Error")
            return customer(email, password)    
       
    elif services == "0":
        return customer(email, password)

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
        Base.delete("customer", "email", email)
        



def customer(email, password):
    ser = input("""
     1. Products
     2. Wants
     3. profile
    """)

    if ser == "1":
        data = Base.select("product")
        for i in Data:
            print(f"""
              ID = {i[0]}
              Name = {i[1 ]}
              price = {i[2 ]}
              made = {i[3]}
              category_id = {i[4]}
            """)

        b = input("""
            0. Back
        """)
        
        if b=="0":
            return customer(email, password)

    elif ser == "2":
        if len(data) !=0:
            data = Base.select("wants")
            for i in Data:
                print(f"""
                ID = {i[0]}
                Product_id = {i[1]}
                """)
            
            e = input("""
            1. Add prodict
            0. Back
            """)
            if e == "1":
                id == int(input("Entr ptofuct id "))
                query = f"insert into wants(product_id) values({id})"
                print(Database.connect(query, "insert"))
                return customer(email, password)

            elif e == "0":
                return customer(email, password)    
        else:
            e = input("""
            1. Add prodict
            0. Back
            """)
            if e == "1":
                id == int(input("Entr ptofuct id "))
                query = f"insert into wants(product_id) values({id});"
                print(Database.connect(query, "insert"))
                return customer(email, password)

            elif e =="0":
                return customer(email, password)  

    elif ser == "3":
        return profile(email, password) 



