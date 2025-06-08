import psycopg2
from psycopg2 import OperationalError


# function to connect with database
def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database = db_name,
            user = db_user,
            password = db_password,
            host = db_host,
            port = db_port,
        )
        print("Connection successful")
    except OperationalError as e:
        print(f"the error '{e}' occurred")
    return connection
 
# function to execute SQL queries
def execute_query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()

    try:
        cursor.execute(query)
        print("successful query execution")
        print(cursor.fetchall())

    except OperationalError as e:
        print(f"the error '{e}' occurred")

# main function
def main():
# connect to the grad_db database
    connection = create_connection("grad_db", "postgres", "jan123","localhost", "5432")

    connection.autocommit = True
    cursor = connection.cursor()

    # How many entries applied for Fall 2024?
    query = """
        SELECT COUNT (a.term)
            FROM applicants a
            WHERE a.term = 'Fall 2024'
    """
    cursor.execute(query)
    print(cursor.fetchall())

    # What percentage of entries are from international students?
    query = """
        SELECT COUNT (a.us_or_international)
            FROM applicants a
            WHERE a.us_or_international = 'International'
    """
    cursor.execute(query)
    temparray = cursor.fetchall()
    temptuple = temparray[0]
    num_international = temptuple[0]
    print(num_international)

    query = """
        SELECT COUNT (a.us_or_international)
            FROM applicants a
    """
    cursor.execute(query)
    temparray = cursor.fetchall()
    temptuple = temparray[0]
    total = temptuple[0]
    print(total)

    percent_international = (num_international / total ) * 100
    print(percent_international)

    


main()