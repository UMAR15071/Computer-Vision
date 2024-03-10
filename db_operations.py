import sqlite3

def insertData(id, firstname, lastname, dob, dept):
    con = sqlite3.connect('Attendance.db')
    cursor = con.cursor()

    query = """INSERT INTO employees
                   VALUES(?,?,?,?,?)"""
    cursor.execute(query, (id, firstname, lastname, dob, dept))
    con.commit()
    print("A record has been added")
    cursor.close()
    con.close()

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
    
