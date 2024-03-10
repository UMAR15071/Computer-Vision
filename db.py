import sqlite3

#This file will run only once!!

con = sqlite3.connect("Attendance.db") #connection to db

cursor = con.cursor() #cursor to navigate inside the database

cursor.execute(""" CREATE TABLE employees(
               Employee_ID int,
               First_name text, 
               Last_name text, 
               Date_Of_Birth text,
               Department text
)
""")
cursor.execute(""" CREATE TABLE registers(
               Employee_ID int,
               Date text,
               Time_Clock_In text,
               Time_Clock_out text
)
""")

con.commit() # run for commiting any query

con.close() # closing the database connection


