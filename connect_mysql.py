import mysql.connector
from mysql.connector import Error

db_name = "gym_management_db"
user = "root"
# Your password goes here
password = "*******"
host = "localhost"

# Creating function to connect to mysql database
def connection():

    try:
        conn = mysql.connector.connect(
            username = user,
            database = db_name,
            password = password,
            host = host
        )

        if conn.is_connected:
            # print("Connected to gym_management db")
            return conn

    except Error as e:
        print(f"Error : {e}")
        return None

    # finally:
    #     if conn and conn.is_connected:
    #         conn.close()
    #         print("MySql Connection is closed")