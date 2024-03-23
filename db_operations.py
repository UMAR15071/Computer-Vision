import sqlite3
from tkinter import messagebox,Button
import datetime

def insertData(id, firstname, lastname, dob, dept):
    con = sqlite3.connect('Attendance.db')
    cursor = con.cursor()
    try:
        query = """INSERT INTO employees
                   VALUES(?,?,?,?,?)"""
        cursor.execute(query, (id, firstname, lastname, dob, dept))
        con.commit()
        print("A record has been added")
        cursor.close()
        con.close()
        return True
    except:
        messagebox.showerror("Error", "Picture Missing: Please save the person's picture before submitting")
        return False


def generate_id():
    con = sqlite3.connect('Attendance.db')
    cursor = con.cursor()

    cursor.execute("""SELECT COUNT(*) FROM employees""")
    count = cursor.fetchone()[0]
    if count == 0:
        count += 1
    else:
        query = """SELECT Employee_ID FROM employees
                ORDER BY Employee_ID DESC LIMIT 1"""
        cursor.execute(query)
        last_record_id = cursor.fetchone()[0]
        count = last_record_id + 1
    cursor.close()
    con.close()
    return count

def getDetails(id):
    con = sqlite3.connect('Attendance.db')
    cursor = con.cursor()
    query = """ SELECT First_name, Last_name, Department FROM employees WHERE Employee_ID = ?"""

    cursor.execute(query, (id,))
    result = cursor.fetchall()
    cursor.close()
    con.close()
    if result:
        return result[0]
    else:
        return "Unknown", "Unknown", "Unknown"

def checkMarked(id, date):
    if id == "Unknown":
        print("invalid credentials")
    else:
        con = sqlite3.connect('Attendance.db')
        cursor = con.cursor()
        query = """SELECT Time_Clock_out
                    FROM registers
                    WHERE Employee_ID = ? AND Date = ? 
                    ORDER BY Time_Clock_In DESC LIMIT 1"""
        cursor.execute(query, (id, date))
        result = cursor.fetchone()
        cursor.close()
        con.close()
        if result:
            if result[0] == "N/A":
                return True
            else: 
                return False
        else: 
            return False
        


    
def clockIn(id):
    if id == "Unknown":
        print("can't run")
    else:
        date = datetime.date.today().strftime("%d-%m-%Y")
        time = datetime.datetime.now().time().strftime("%H:%M")
        con = sqlite3.connect('Attendance.db')
        cursor = con.cursor()
        query = """INSERT INTO registers
                    values(?,?,?,?)"""
        cursor.execute(query, (id,date,time,"N/A"))
        con.commit()
        cursor.close()
        con.close()
        print("Attendance marked")


def clockOut(id):
    if id == "Unknown":
        print("invalid credentials")
    else:
        time = datetime.datetime.now().time().strftime("%H:%M")
        con = sqlite3.connect('Attendance.db')
        cursor = con.cursor()
        query = """UPDATE registers
                    SET Time_Clock_out = ? WHERE 
                    Employee_ID = ?"""
        cursor.execute(query, (time, id))
        con.commit()
        cursor.close()
        con.close()
        print("Employee timed out")