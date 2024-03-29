import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='attendance_management'
)

mycursor = db.cursor()

mycursor.execute('''
    CREATE TABLE Employees (
        Employee_ID int AUTO_INCREMENT,
        First_Name VARCHAR(15),
        Last_Name VARCHAR(15),
        DATE_Of_Birth date,
        Department VARCHAR(20),
        PRIMARY KEY (Employee_ID)
    )
''')

mycursor.execute('''
    CREATE TABLE Registers (
        Employee_ID int,
        Date date,
        Time_Clocked_In VARCHAR(7),
        Time_Clocked_Out VARCHAR(7),
        FOREIGN KEY (Employee_ID) REFERENCES Employees(Employee_ID)
    )
''')
db.close()