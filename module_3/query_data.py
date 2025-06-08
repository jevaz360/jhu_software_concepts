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
    temparray = cursor.fetchall()
    temptuple = temparray[0]
    num_fall2024_applicants = temptuple[0]
    print(num_fall2024_applicants)

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
 

    query = """
        SELECT COUNT (a.us_or_international)
            FROM applicants a
    """
    cursor.execute(query)
    temparray = cursor.fetchall()
    temptuple = temparray[0]
    total = temptuple[0]
 

    percent_international = (num_international / total ) * 100
    percent_international = round(percent_international, 2)
    print(percent_international)

    # What is the average GPA of applicants?

    query = """
        SELECT a.gpa FROM applicants a
            WHERE a.gpa != 0

    """
    cursor.execute(query)
    temparray = cursor.fetchall()
    x = []
    for tuple in temparray:
        value = tuple[0]
        x.append(value)

    sum_gpa = sum(x)
    total_applicants_with_gpa = len(x)
    average_gpa = sum_gpa / total_applicants_with_gpa
    print(average_gpa)

    # What is the average GRE of applicants?
    query = """
        SELECT a.gre FROM applicants a
            WHERE a.gre != 0

    """
    cursor.execute(query)
    temparray = cursor.fetchall()
    x = []
    for tuple in temparray:
        value = tuple[0]
        x.append(value)


    sum_gre = sum(x)
    total_applicants_with_gre = len(x)
    average_gre = sum_gre / total_applicants_with_gre

    print(average_gre)

    # What is the average GRE V of applicants?
    query = """
        SELECT a.gre_v FROM applicants a
            WHERE a.gre_v != 0

    """
    cursor.execute(query)
    temparray = cursor.fetchall()
    x = []
    for tuple in temparray:
        value = tuple[0]
        x.append(value)

    sum_gre_v = sum(x)
    total_applicants_with_gre_v = len(x)
    average_gre_v = sum_gre_v / total_applicants_with_gre_v
    print(average_gre_v)

    # What is the average GRE AW of applicants?
    query = """
        SELECT a.gre_aw FROM applicants a
            WHERE a.gre_aw != 0

    """
    cursor.execute(query)
    temparray = cursor.fetchall()
    x = []
    for tuple in temparray:
        value = tuple[0]
        x.append(value)

    sum_gre_aw = sum(x)
    total_applicants_with_gre_aw = len(x)
    average_gre_aw = sum_gre_aw / total_applicants_with_gre_aw
    print(average_gre_aw)

    # What is the average GPA of American students in Fall 2024
    query = """
        SELECT a.gpa FROM applicants a
            WHERE 
                a.us_or_international = 'American' AND
                a.term = 'Fall 2024' AND
                a.gpa != 0
    """
    cursor.execute(query)
    temparray = cursor.fetchall()

    x = []
    for tuple in temparray:
        value = tuple[0]
        x.append(value)

    sum_gpa_american_fall2024= sum(x)
    total_applicants_with_gpa_american_fall2024 = len(x)
    average_gpa_american_fall2024 = sum_gpa_american_fall2024 / total_applicants_with_gpa_american_fall2024
    print(average_gpa_american_fall2024)

    # What percent of entries for Fall 2024 are Acceptances (to two decimal places)?

    # NOTE: reference used for 'like' operator in the where statement below: 
    # https://www.postgresql.org/message-id/81Jun28.170305edt.35713@gateway.lee.k12.nc.us#:~:text=To%20find%20strings%20inside%20a%20field%20in,write%20something%20like:%20*%20**(no%20pun%20intended)**

    query = """
        SELECT * FROM applicants a
            WHERE
                a.term = 'Fall 2024' AND
                a.status LIKE '%Accepted%'
    """
    cursor.execute(query)
    temparray = cursor.fetchall()
    num_fall2024_applicants_accepted = len(temparray)
    percent_fall2024_accepted = (num_fall2024_applicants_accepted / num_fall2024_applicants) * 100
    percent_fall2024_accepted = round(percent_fall2024_accepted, 2)
    print(percent_fall2024_accepted)

    # What is the average GPA of applicants who applied for Fall 2024 who are acceptances?
    query = """
        SELECT a.gpa FROM applicants a
            WHERE
                a.term = 'Fall 2024' AND
                a.status LIKE '%Accepted%' AND
                a.gpa !=0
    """
    cursor.execute(query)
    temparray = cursor.fetchall()
    #print(temparray)
    
    x = []
    for tuple in temparray:
        value = tuple[0]
        x.append(value)

    sum_gpa_fall2024_acceptances= sum(x)
    total_fall2024_acceptances = len(x)
    average_gpa_fall2024_acceptances = sum_gpa_fall2024_acceptances / total_fall2024_acceptances
    print(average_gpa_fall2024_acceptances)

    # How many entries are from applicants who applied to JHU for a masters degree in Computer Science?
    query = """
        SELECT * FROM applicants a
            WHERE
                a.program LIKE '%Computer Science%' AND
                a.program LIKE '%Johns Hopkins%'
    """
    cursor.execute(query)
    temparray = cursor.fetchall()
    num_applicants_cs_jhu = len(temparray)
    print(num_applicants_cs_jhu)


main()