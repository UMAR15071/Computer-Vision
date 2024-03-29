from tkinter import messagebox,Button
import datetime
import mysql.connector
import tkinter as tk

db = None
cursor = None

def establish_Connection():
    global db, cursor
    try:
        db = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='attendance_management'
        )
        cursor = db.cursor()
    except mysql.connector.Error as err:
        messagebox.showerror("Database Connection Error", f"Error: {err}")
        return False
    return True

def insertData(id, firstname, lastname, dob, dept):
    global cursor
    if cursor is None:
        if not establish_Connection():
            return False

    try:
        cursor.execute("""
                    INSERT INTO employees (Employee_ID, First_Name, Last_Name, Date_of_Birth, Department)
                    VALUES (%s,%s,%s,%s,%s)       
                        """, (id, firstname, lastname, dob, dept))
        db.commit()
        return True
    except mysql.connector.Error as err:
        messagebox.showerror("Database Insert Error", f"Error: {err}")
        return False
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")
        return False


def connected():
    if db is not None:
        return True
    else: 
        return False
    
def connectionClose():
    cursor.close()
    db.close()

def generate_id():
    # Assuming 'cursor' is already defined and connected to your database
    query = "SELECT MAX(Employee_ID) FROM employees"
    cursor.execute(query)
    result = cursor.fetchone()[0]  # Get the first (and only) item from the tuple

    if result is None:
        # Table is empty, start IDs from 1
        return 1
    else:
        # Increment the last ID by 1
        return result + 1


def getDetails(id):
    try:
        query = """SELECT First_name, Last_name,Date_Of_Birth, Department FROM employees WHERE Employee_ID = %s"""
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        if result:
            return result
        else:
            return "Unknown", "Unknown", "Unknown"  
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None  

def checkMarked(id, date):
    if id == "Unknown":
        print("Invalid credentials")
        return False
    else:
        try:
            query = """SELECT Time_Clocked_Out
                    FROM registers
                    WHERE Employee_ID = %s AND Date = %s
                    ORDER BY Time_Clocked_In DESC LIMIT 1"""
            cursor.execute(query, (id, date))
            result = cursor.fetchone()
            if result:
                if result[0] is None:
                    return True
                else:
                    return False
        except mysql.connector.Error as err:
            print(f"Database error: {err}")
            return False
    
def clockIn(id):
    print(id)
    if id == "Unknown":
        print("Can't run")
    try:
        date = datetime.date.today().strftime("%Y-%m-%d")  # Adjust the format if needed
        time = datetime.datetime.now().strftime("%H:%M")  # Adjust the format if needed
        query = """INSERT INTO registers (Employee_ID, Date, Time_Clocked_In)
                   VALUES (%s, %s, %s)"""
        cursor.execute(query, (id, date, time))
        db.commit()
        print("Attendance marked")
    except mysql.connector.Error as err:
        print(f"Database error: {err}")


def clockOut(id):
    if id == "Unknown":
        print("invalid credentials")
    else:
        time = datetime.datetime.now().time().strftime("%H:%M")
        query = """UPDATE registers
                    SET Time_Clocked_Out = %s WHERE 
                    Employee_ID = %s"""
        cursor.execute(query, (time, id))
        db.commit()
        print("Employee clocked out")

def updateRecord(id_TextField, first_name_TextField, last_name_TextField, dob_entry, dept_combobox):
    if first_name_TextField.get() == "" or last_name_TextField.get() == "" or dob_entry.get() == "" or dept_combobox.get() == "--select Dept--":
        messagebox.showerror("Error", "Error: Please fill all the fields")
    else:
        query = """UPDATE employees 
                SET First_Name = %s,
                    Last_Name = %s,
                    Date_of_Birth = %s,
                    Department = %s
                WHERE Employee_ID = %s"""
        
        id = id_TextField.get()
        firstname = first_name_TextField.get() 
        lastname = last_name_TextField.get()
        dob = dob_entry.get()
        dept = dept_combobox.get()
        try:
            cursor.execute(query, (firstname, lastname, dob, dept, id))
            db.commit()

            id_TextField.delete(0,tk.END)
            first_name_TextField.delete(0, tk.END)
            last_name_TextField.delete(0, tk.END)
            dob_entry.delete(0, tk.END)
            dept_combobox.set("--select Dept--")
            messagebox.showinfo("Success ","Recorded has been Updated")
        except mysql.connector.Error as err:
            print(f"Database error: {err}")

def deleteRecord(id):
    try:
        query = """DELETE from employees 
                WHERE Employee_ID = %s"""
        cursor.execute(query, (id,))
        db.commit()
        messagebox.showinfo("Success ","Recorded has been deleted Successfully")
    except mysql.connector.Error as err:
            print(f"Database error: {err}")
