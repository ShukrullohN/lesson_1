import psycopg2 as db
from dotenv import load_dotenv
import os
load_dotenv()


class Database:
    @staticmethod
    def connect(query, query_type):
        database = db.connect(
            database=os.getenv("database"),
            host=os.getenv("host"),
            user=os.getenv("user"),
            password=os.getenv("password")
        )

        cursor = database.cursor()

        cursor.execute(query)
        data = ["insert", "delete", "update", "create"]
        if query_type in data:
            database.commit()
            if query_type == "insert":
                return "INSERTED"

            elif query_type == "delete":
                return "DELETE"

            elif query_type == "update":
                return "UPDATED"

            elif query_type == "create":
                return "CREATED"

               

        else:
            return cursor.fetchall()