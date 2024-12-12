# Importing database connection
from connect_mysql import connection, Error

# Main function that runs user interface

def main():
    while True:
        print(f'''
        Welcome to the Gym Database management system
        *********************************************
            1. Members Table
            2. Sessions Table
            3. Exit
        ''')

        ans = int(input("Which table would you like to view?: "))

        if ans == 1:
            print(f'''
            Members Operations:
            *******************
                1. View existing members
                2. Add a new member
                3. Update member info
                4. Exit
            ''')

            operation = int(input("What would you like to do?: "))

            if operation == 1:
                get_members()
            elif operation == 2:
                add_member()
            elif operation == 3:
                update_member()
            elif operation == 4:
                break
        
        elif ans == 2:
            print(f'''
            Sessions Operations:
            *******************
                1. View existing workout sessions
                2. Add a new workout session
                3. Delete a workout session
                4. Exit
            ''')

            operation = int(input("What would you like to do?: "))

            if operation == 1:
                get_sessions()
            elif operation == 2:
                add_session()
            elif operation == 3:
                delete_session()
            elif operation == 4:
                break
        
        elif ans == 3:
            break



# Members Functions

def get_members():
    conn = connection()
    # Testing connection
    if conn is not None:
        try:
            # Creating "libarian" who will grab information from the database (library)
            cursor = conn.cursor()

            # Creating sql command to grab all data in the members table
            query = "SELECT * FROM members"

            # Libarian is attempting to follow command
            cursor.execute(query)

            # For each member the libarian finds from previous command - print their id, name & age
            for id,name, age in cursor.fetchall():
                print(f"id#: {id} - name: {name} - age: {age}")
        
        except Error as e:
            print(f"Error: {e}")

        finally:
            # ALWAYS CLOSE CONNECTION
            cursor.close()
            conn.close()


def add_member(): 
    conn = connection()
    # Testing connection
    if conn is not None:

        try: 
            cursor = conn.cursor()
            
            # Creating variables to hold user input for member name & age
            member_name = input("Insert member name: ").title()
            member_age = int(input("Insert member age: "))
    
             # Creating sql command to Add a new member with the values of (member_name & member_age)
            query = "INSERT INTO members (name,age) VALUES (%s,%s)"
            cursor.execute(query,(member_name,member_age))
            conn.commit()

            print(f"New member {member_name} added successfully!")
        
        except Error as e:
            print(f"Error: {e}")
        
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

            conn.close()
            conn.close()


def update_member():
    conn = connection()
    if conn is not None:

        try:
            cursor = conn.cursor()

            # Creating variable to hold user input for member id & age
            member_id = input("Please provide the id for the member you would like to update: ")
            member_age = int(input("What is their age?: "))

            # Creating sql command to update the age column in the members table where the member's id is equal to member_id  
            query = "UPDATE members SET age = %s WHERE id = %s"

            cursor.execute(query,(member_age,member_id))
            conn.commit()

            print(f"Updated the age for member at id {member_id} to {member_age}")

        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close()


# Session Functions

def get_sessions():
    conn = connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            
            # Creating sql command to grab all data in the workout_sessions table
            query = "SELECT * FROM workout_sessions"
            cursor.execute(query,)

            for id,session_date,member_id,duration,calories_burned in cursor.fetchall():
                print(f'''
                    session#: {id} 
                    XXXXXXXXXXXXXX
                        - member id: {member_id}
                        - date: {session_date}
                        - duration : {duration}
                        - calories burned : {calories_burned}
                ''')
            
        except Error as e:
            print(f"Error : {e}")
        
        finally:
            cursor.close()
            conn.close()


def add_session():
    conn = connection()
    if conn is not None:

        try:
            cursor = conn.cursor()

            # Creating variables to hold information for the workout session user wants to add to the workout_sessions table
            date = input("Enter date of session (YYYY-MM-DD): ")
            id = int(input("Enter member id for this session: "))
            session_duration = input("Enter duration of workout session: ")
            calories = input("Enter number of calories burned: ")

            # Creating sql command to take the user input above to create a new session and add it to the workout_sessions table
            query = "INSERT INTO workout_sessions (session_date,member_id,duration,calories_burned) VALUES (%s,%s,%s,%s)"
            cursor.execute(query,(date,id,session_duration,calories))
            conn.commit()

            print(f"New workout session submitted for member at id: {id}")

        except Error as e:
            print(f"Error as {e}")
        
        finally:
            cursor.close()
            conn.close()


def delete_session ():
    conn = connection()
    if conn is not None:
        try:
            cursor = conn.cursor()

            # creating variables to hold the id for the session user wishes to delete and the id of the member related to that session
            session_id = int(input("Which workout session would you like to delete?: "))
            member_id = int(input("What is the id of the member for the session you wish to delete?: "))

            # Creating sql command to delete the workout session with the id of session_id for the member at member_id
            query = "DELETE FROM workout_sessions WHERE id = %s AND member_id = %s"

            cursor.execute(query, (session_id,member_id))
            conn.commit()

            print("Session deleted successfully")


        except Error as e:
            print(f"Error : {e}")

        finally:
            cursor.close()
            conn.close()


main()