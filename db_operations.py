import sqlite3
from tkinter import messagebox

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
    
    print(result)
    cursor.close()
    con.close()
    if result:
        return result[0]
    else:
        return "Unknown", "Unknown", "Unknown"
