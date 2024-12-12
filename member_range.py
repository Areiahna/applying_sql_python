# Importing database connection
from connect_mysql import connection, Error

def get_members_in_age_range(start_age, end_age):
    conn = connection()
    # Testing connection
    if conn is not None:
        try:
            # Creating "libarian" who will grab information from the database (library)
            cursor = conn.cursor()
            # Creating sql command to grab all members between ages x & x
            query = "SELECT name, age FROM members WHERE age BETWEEN %s AND %s"

            # Libarian is attempting to follow command
            cursor.execute(query,(start_age,end_age))

            # For each member the libarian finds from previous command - provide their name & age
            for name, age in cursor.fetchall():
                print(f"name: {name} - age: {age}")

        except Error as e:
            print(f"Error : {e}") 

        finally:
            # ALWAYS CLOSE CONNECTIONS
            cursor.close()
            conn.close()   

get_members_in_age_range(25,30)