import mysql.connector

db = mysql.connector.connect(
    host='attendance-management.czg8eiywyuez.eu-west-1.rds.amazonaws.com',
    user='admin',
    passwd='B00tCamp$',
    database='attendanceManagement'
)

mycursor = db.cursor()

mycursor.execute('''
    CREATE TABLE Employees (
    Employee_ID int AUTO_INCREMENT,
    First_Name VARCHAR(15),
    Last_Name VARCHAR(15),
    Date_Of_Birth date,
    Department VARCHAR(20),
    Delete_Flag TINYINT DEFAULT 0,
    PRIMARY KEY (Employee_ID)
    )
''')

mycursor.execute('''
    CREATE TABLE Registers (
    Employee_ID int,
    Date date,
    Time_Clocked_In VARCHAR(7),
    Time_Clocked_Out VARCHAR(7) DEFAULT 'None',
    FOREIGN KEY (Employee_ID) REFERENCES Employees(Employee_ID)
    )
''')


db.close()