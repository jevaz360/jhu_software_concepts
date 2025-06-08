Name: Janice Vaz JHED ID: jvaz3

Module 3: SQL Data Analysis

Approach: In this assignment, we were tasked with loading the webscraped data we stored in a JSON file into a SQL table.

In order to do this first a database called grad_db was created in which an applicants SQL table was created. Accordingly the JSON file that had the stored data was opened and each dictionary representing an applicants entry was parsed to get the respective column information in the SQL table. After retrieving the available information an insert statement was made to insert the applicant's entry into the applicants SQL table. It is noted that when parsing to get respective column information, some entries scraped from the web had improper styling such as for the date SQL column requring a YYYY-MM-DD format. Hence, conversions were made with the str_to_date function. Similarly, some entries had improper or empty dates such as "--", in order to avoid this, the data needed to be collected was initialized such that 0000-00-00 would be the default date, and would only change if an actual string date was passed through. A similar problem was encountered with GPA and GRE scores needing to convert the string received from the scraped data which would often be in the string format of "GPA 3.5", hence a str_to_float function was used to turn a string like this into a float of 3.5. The default floats for GPA and GRE scores were set to 0.0. This is noted because when selecting entries to determine
average GPAs/GRE scores for example, when querying the table, GPAs/GRE scores with a value of 0 (default indicating the entry didn't actually have a GPA/GRE score) were selectively ignored.

After loading the data into the table, SQL queries were processed in the query_data.py file.

Lastly, using Flask, a webpage where the results of the queries are uploaded was developed in the app.py file.

Known Bugs:
