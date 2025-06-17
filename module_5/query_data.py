"""Module contains functions for connecting a to a database to retrieve 
data via SQL statmenets, retrieving data from a table in the database, 
and printing out the data """

import psycopg2
from psycopg2 import OperationalError
from psycopg2 import sql

# function to connect with database
def create_connection(db_name, db_user, db_password, db_host, db_port):
    """Method creates a connection to a given database given arguments:
    user, password, host, and port
    
    Prints whether or not connection to database was successful"""
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
    """Method that executes an SQL query given arguments:
    connection, query
    
    From the connection, a cursor is initialized
    At the cursor the SQL query is executed"""
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
    """Method that connects to a database, 
    initializes a cursor, 
    uses SQL statements to query desired data,
    and prints desired data"""
# connect to the grad_db database
    connection = create_connection("grad_db", "postgres", "jan123","localhost", "5432")

    connection.autocommit = True
    cursor = connection.cursor()

    # How many entries applied for Fall 2024?
    query = sql.SQL( """
        SELECT COUNT ({term_column})
            FROM {table_name}
            WHERE {term_column} = {column_value}
    """).format(
        term_column = sql.Identifier("term"),
        table_name = sql.Identifier("applicants"),
        column_value = sql.Literal("Fall 2024")
    )
    cursor.execute(query)
    temparray = cursor.fetchall()
    temptuple = temparray[0]
    num_fall2024_applicants = temptuple[0]
    print(num_fall2024_applicants)

    # What percentage of entries are from international students?
    query = sql.SQL("""
        SELECT COUNT ({domestic_foreign_column})
            FROM {table_name}
            WHERE {domestic_foreign_column} = {column_value}
    """).format(
        domestic_foreign_column = sql.Identifier("us_or_international"),
        table_name = sql.Identifier("applicants"),
        column_value = sql.Literal('International')

    )
    cursor.execute(query)
    temparray = cursor.fetchall()
    temptuple = temparray[0]
    num_international = temptuple[0]

    query = sql.SQL("""
        SELECT COUNT ({domestic_foreign_column})
            FROM {table_name}
    """).format(
        domestic_foreign_column = sql.Identifier("us_or_international"),
        table_name = sql.Identifier("applicants")
    )
    cursor.execute(query)
    temparray = cursor.fetchall()
    temptuple = temparray[0]
    total = temptuple[0]

    percent_international = (num_international / total ) * 100
    percent_international = round(percent_international, 2)
    print(percent_international)

    # What is the average GPA of applicants?

    query = sql.SQL("""
        SELECT {gpa_column} FROM {table_name}
            WHERE {gpa_column} != {column_value}

    """).format(
        gpa_column = sql.Identifier("gpa"),
        table_name = sql.Identifier("applicants"),
        column_value = sql.Literal("0")
    )
    cursor.execute(query)
    temparray = cursor.fetchall()
    x = []
    for my_tuple in temparray:
        value = my_tuple[0]
        x.append(value)

    sum_gpa = sum(x)
    total_applicants_with_gpa = len(x)
    average_gpa = sum_gpa / total_applicants_with_gpa
    print(average_gpa)

    # What is the average GRE of applicants?
    query = sql.SQL("""
        SELECT {gre_column} FROM {table_name}
            WHERE {gre_column} != {column_value}

    """).format(
        gre_column = sql.Identifier("gre"),
        table_name = sql.Identifier("applicants"),
        column_value = sql.Literal("0")
    )
    cursor.execute(query)
    temparray = cursor.fetchall()
    x = []
    for my_tuple in temparray:
        value = my_tuple[0]
        x.append(value)


    sum_gre = sum(x)
    total_applicants_with_gre = len(x)
    average_gre = sum_gre / total_applicants_with_gre

    print(average_gre)

    # What is the average GRE V of applicants?
    query = sql.SQL("""
        SELECT {gre_v_column} FROM {table_name}
            WHERE {gre_v_column} != {column_value}

    """).format(
        gre_v_column = sql.Identifier("gre_v"),
        table_name = sql.Identifier("applicants"),
        column_value = sql.Literal("0")
    )
    cursor.execute(query)
    temparray = cursor.fetchall()
    x = []
    for my_tuple in temparray:
        value = my_tuple[0]
        x.append(value)

    sum_gre_v = sum(x)
    total_applicants_with_gre_v = len(x)
    average_gre_v = sum_gre_v / total_applicants_with_gre_v
    print(average_gre_v)

    # What is the average GRE AW of applicants?
    query = sql.SQL("""
        SELECT {gre_aw_column} FROM {table_name}
            WHERE {gre_aw_column} != {column_value}

    """).format(
        gre_aw_column = sql.Identifier("gre_aw"),
        table_name = sql.Identifier("applicants"),
        column_value = sql.Literal("0")
    )
    cursor.execute(query)
    temparray = cursor.fetchall()
    x = []
    for my_tuple in temparray:
        value = my_tuple[0]
        x.append(value)

    sum_gre_aw = sum(x)
    total_applicants_with_gre_aw = len(x)
    average_gre_aw = sum_gre_aw / total_applicants_with_gre_aw
    print(average_gre_aw)

    # What is the average GPA of American students in Fall 2024
    query = sql.SQL("""
        SELECT {gpa_column} FROM {table_name}
            WHERE 
                {domestic_foreign_column} = {dom_for_literal} AND
                {term_column} = {term_literal} AND
                {gpa_column} != {gpa_literal}
    """).format(
        gpa_column = sql.Identifier("gpa"),
        table_name = sql.Identifier("applicants"),
        domestic_foreign_column = sql.Identifier("us_or_international"),
        dom_for_literal = sql.Literal("American"),
        term_column = sql.Identifier("term"),
        term_literal = sql.Literal("Fall 2024"),
        gpa_literal = sql.Literal("0")
    )
    cursor.execute(query)
    temparray = cursor.fetchall()

    x = []
    for my_tuple in temparray:
        value = my_tuple[0]
        x.append(value)

    sum_gpa_american_fall2024= sum(x)
    total_applicants_with_gpa_american_fall2024 = len(x)
    average_gpa_american_fall2024 = (sum_gpa_american_fall2024 /
                                     total_applicants_with_gpa_american_fall2024)
    print(average_gpa_american_fall2024)

    # What percent of entries for Fall 2024 are Acceptances (to two decimal places)?

    # NOTE: reference used for 'like' operator in the where statement below:
    # https://www.postgresql.org/message-id/81Jun28.170305edt.35713@gateway.lee.k12.nc.us#:~:text=To%20find%20strings%20inside%20a%20field%20in,write%20something%20like:%20*%20**(no%20pun%20intended)**
    query = sql.SQL("""
        SELECT * FROM {table_name}
            WHERE
                {term_column} = {term_literal} AND
                {status_column} LIKE {status_literal}
    """).format(
        table_name = sql.Identifier("applicants"),
        term_column = sql.Identifier("term"),
        term_literal = sql.Literal("Fall 2024"),
        status_column = sql.Identifier("status"),
        status_literal = sql.Literal('%Accepted%')
    )
    cursor.execute(query)
    temparray = cursor.fetchall()
    num_fall2024_applicants_accepted = len(temparray)
    percent_fall2024_accepted = ((num_fall2024_applicants_accepted /
                                  num_fall2024_applicants) * 100)
    percent_fall2024_accepted = round(percent_fall2024_accepted, 2)
    print(percent_fall2024_accepted)

    # What is the average GPA of applicants who applied for Fall 2024 who are acceptances?
    query = sql.SQL("""
        SELECT {gpa_column} FROM {table_name}
            WHERE
                {term_column} = {term_literal} AND
                {status_column} LIKE {status_literal} AND
                {gpa_column} !={gpa_literal}
    """).format(
        gpa_column = sql.Identifier("gpa"),
        table_name = sql.Identifier("applicants"),
        term_column = sql.Identifier("term"),
        term_literal = sql.Literal("Fall 2024"),
        status_column = sql.Identifier("status"),
        status_literal = sql.Literal("%Accepted%"),
        gpa_literal = sql.Literal("0")
    )
    cursor.execute(query)
    temparray = cursor.fetchall()
    #print(temparray)
    x = []
    for my_tuple in temparray:
        value = my_tuple[0]
        x.append(value)

    sum_gpa_fall2024_acceptances= sum(x)
    total_fall2024_acceptances = len(x)
    average_gpa_fall2024_acceptances = (sum_gpa_fall2024_acceptances /
                                        total_fall2024_acceptances)
    print(average_gpa_fall2024_acceptances)

    # How many entries are from applicants who applied to JHU
    # for a masters degree in Computer Science?
    query = sql.SQL("""
        SELECT * FROM {table_name}
            WHERE
                {program_column} LIKE {program_literal_1} AND
                {program_column} LIKE {program_literal_2}
    """).format(
        table_name = sql.Identifier("applicants"),
        program_column = sql.Identifier("program"),
        program_literal_1 = sql.Literal('%Computer Science%'),
        program_literal_2 = sql.Literal('%Johns Hopkins%'))
    cursor.execute(query)
    temparray = cursor.fetchall()
    num_applicants_cs_jhu = len(temparray)
    print(num_applicants_cs_jhu)


main()
