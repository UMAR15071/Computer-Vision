from tkinter import messagebox,Button
import datetime
import mysql.connector
import tkinter as tk
import os,sys

db = None
cursor = None

def get_resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def establish_Connection():
    global db, cursor
    try:
        db = mysql.connector.connect(
            host='attendancemanagement.czg8eiywyuez.eu-west-1.rds.amazonaws.com',
            user='admin',
            passwd='B00tCamp$',
            database='attendanceManagement'
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
                    INSERT INTO Employees (Employee_ID, First_Name, Last_Name, Date_of_Birth, Department)
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
    query = "SELECT MAX(Employee_ID) FROM Employees"
    cursor.execute(query)
    result = cursor.fetchone()[0]  

    if result is None:
        return 1
    else:
        return result + 1


def getDetails(id):
    try:
        query = """SELECT First_name, Last_name, Date_Of_Birth, Department FROM Employees WHERE Employee_ID = %s AND Delete_Flag = 0"""
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        if result:
            return result
        else:
            return "Unknown", "Unknown", "Unknown", "Unknown"

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    except TypeError as te:
        print(f"TypeError: {te}")
        return None

def checkMarked(id, date):
    if id == "Unknown":
        print("Invalid credentials")
        return False
    else:
        try:
            query = """SELECT Time_Clocked_Out
                    FROM Registers
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
        date = datetime.date.today().strftime("%Y-%m-%d")  
        time = datetime.datetime.now().strftime("%H:%M")  
        query = """INSERT INTO Registers (Employee_ID, Date, Time_Clocked_In)
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
        try:
            time = datetime.datetime.now().time().strftime("%H:%M")
            query = """UPDATE Registers
                        SET Time_Clocked_Out = %s
                        WHERE Employee_ID = %s
                        ORDER BY Time_Clocked_In DESC
                        LIMIT 1"""
            print(time)
            cursor.execute(query, (time, id))
            db.commit()
            print("Employee clocked out")
        except mysql.connector.Error as err:
            print(f"Database error: {err}")

def updateRecord(id_TextField, first_name_TextField, last_name_TextField, dob_entry, dept_combobox):
    if first_name_TextField.get() == "" or last_name_TextField.get() == "" or dob_entry.get() == "" or dept_combobox.get() == "--select Dept--":
        messagebox.showerror("Error", "Error: Please fill all the fields")
    else:
        query = """UPDATE Employees 
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
        query = """UPDATE Employees
                    SET Delete_Flag = 1 
                    WHERE Employee_ID = %s"""
        cursor.execute(query, (id,))
        db.commit()

        photo_path = get_resource_path(f"RegisteredFaces/{id}.jpg")

        # Check if the photo exists and remove it
        if os.path.exists(photo_path):
            os.remove(photo_path)
        
        messagebox.showinfo("Success", "Record has been deleted successfully")

    except mysql.connector.Error as err:
        print(f"Database error: {err}")
def getReport(date, table):
    try:
        query = """SELECT Employee_ID, Time_Clocked_In, Time_Clocked_Out FROM Registers
                    WHERE Date = %s"""
        cursor.execute(query, (date,))
        results = cursor.fetchall()
        if results:
            for item in table.get_children():
                table.delete(item)
            for result in results:
                id = result[0]
                firstname, lastname = getName(id)
                table.insert("",'end',values=(firstname, lastname,result[1],result[2]))
        else:
            for item in table.get_children():
                table.delete(item)
            messagebox.showerror("Error", f"No record found")
    except Exception as e:
        messagebox.showerror("Error", f"No record found {e}")
        


def getName(id):
    try:
        query = """SELECT First_Name, Last_Name 
                    FROM Employees
                    WHERE Employee_ID = %s"""
        cursor.execute(query,(id,))
        results = cursor.fetchone()
        return results[0], results[1]
    except Exception as e:
        messagebox.showerror("Error", f"unexpected error {e}")