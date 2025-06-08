import psycopg2
from psycopg2 import OperationalError
import json

# function to create connection to grad_db server created using postgresql
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

# function that will execute a query given a connection and a query
def execute_query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()

    try:
        cursor.execute(query)
        print("successful query execution")
    except OperationalError as e:
        print(f"the error '{e}' occurred")
    
# function to parse through a str and return float value of gpa/gre/gre_v
def str_to_float(str_value):
    int_array = ['0', '1', '2', '3', '4', '5', '6', '7', '8','9']
    index = 0
    for chr in str_value:
        if chr not in int_array:
            index+=1
        else:
            index-=1 
            break
    int_string = str_value[index:]
    final = float(int_string)
    return final

# function to convert date_added to acceptable date format YYYY-MM-DD
def str_to_date(date_added):
    # initialize variables and define arrays 
    MM = ""
    index = 0
    int_array = ['0', '1', '2', '3', '4', '5', '6', '7', '8','9']
    month_array = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September','October', 'November', 'December']

    # find where the input phrase may include "Added on" and remove it from the string if it exists to get a string suchas "August 08, 2025"
    if date_added[0] == 'A':
        for chr in date_added:
            if chr == 'n':
                break
            else:
                index+=1
        date_added = date_added[index+2:]
        #print(date_added)
        index = 0
    
    # processs the date string until you hit an integer character, this is the starting integer of the day, use this to index the month, day, and year
    for chr in date_added:
        if chr not in int_array:
            index+=1
        else:
            break
    
    str_month = date_added[:index-1]

    for month in month_array:
        if month == str_month:
            temp_index = month_array.index(month)
            month_index = str(temp_index)
            if index < 10:
                MM = '0'+ month_index
            else:
                MM = month_index

    DD = date_added[index:index+2]
    YYYY = date_added[index+4:]

    # put as a string reflecting YYYY-MM-DD
    output_date = YYYY + '-' + MM + '-'+ DD

    return output_date

# main function
def main():

# connect to the grad_db database that was created
    connection = create_connection("grad_db", "postgres", "jan123","localhost", "5432")

# create table
# note that serial is used to create a column that increments automatically
    create_applicants_query = """
    CREATE TABLE IF NOT EXISTS applicants (
        p_id SERIAL PRIMARY KEY,
        program TEXT,
        comments TEXT,
        date_added DATE,
        url TEXT,
        status TEXT,
        term TEXT,
        us_or_international TEXT,
        gpa FLOAT,
        gre FLOAT,
        gre_v FLOAT,
        gre_aw FLOAT,
        degree TEXT    
    )
"""
    execute_query(connection, create_applicants_query)

    # insert entries into table
    # open the json file, load it in as a list of dict (exaclty how it's stored)
    file = open("jhu_software_concepts\module_3\cleaned_applicant_data_10000 1.json")
    data = json.load(file)

    # from the data file, retrieve the values of the respective keys and store each entry as a tuple
    program = "None"
    comments = "None"
    date_added = "0000-00-00"
    url = "None"
    status = "None"
    term = "None"
    us_or_international = "None"
    gpa = 0.0
    gre = 0.0
    gre_v = 0.0
    gre_aw = 0.0
    degree = "None"
    date_punctuation = [' ', '.', '-', '--', 'None']

    for item in data:
        if item.get("program") is not None:
            program = item.get("program")
        if item.get("comments") is not None:
            comments = item.get("comments")
        if item.get("date_added") is not None:
            if item.get("date_added") not in date_punctuation:
                temp_date_added = item.get("date_added")
                date_added = str_to_date(temp_date_added)
        if item.get("url") is not None:
            url = item.get("url")
        if item.get("status") is not None:
            status = item.get("status")
        if item.get("term") is not None:
            term = item.get("term")
        if item.get("US/International") is not None:
            us_or_international = item.get("US/International")
        if item.get("GPA") is not None:
            temp_gpa = item.get("GPA")
            gpa = str_to_float(temp_gpa)
        if item.get("GRE") is not None:
            temp_gre = item.get("GRE")
            gre = str_to_float(temp_gre)
        if item.get("GRE V") is not None:
            temp_gre_v = item.get("GRE V")
            gre_v = str_to_float(temp_gre_v)
        if item.get("GRE AW") is not None:
            temp_gre_aw = item.get("GRE AW")
            gre_aw = str_to_float(temp_gre_aw)
        if item.get("Degree") is not None:
            degree = item.get("Degree")
        
       
        # insert created values to table
        insert_query = "INSERT INTO applicants (program, comments, date_added, url, status, term, us_or_international, gpa, gre, gre_v, gre_aw, degree) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
        
        connection.autocommit = True
        cursor = connection.cursor()
        cursor.execute(insert_query, (program, comments, date_added, url, status, term, us_or_international, gpa, gre, gre_v, gre_aw, degree))

    #query = """DROP TABLE applicants"""
    #execute_query(connection,query)

main()