import cv2
import tkinter as tk
import tkcalendar as tkcal
from db_operations import generate_id, insertData

def takePhoto():

    video_capture = cv2.VideoCapture(0)
    name = input('Enter you name: ')

    while True:
        ret, frame = video_capture.read()

        cv2.imshow('frame', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('c'):
            cv2.imwrite("RegisteredFaces/"+str(name) + ".jpg", frame)
            cv2.waitKey(2000)
            break

        

    video_capture.release() 

    cv2.destroyAllWindows() 


def close_screens(window):
    for frame in window.winfo_children():
        frame.destroy()

def pick_date(dob_entry):
    global cal, date_window

    date_window = tk.Toplevel()
    date_window.grab_set()
    date_window.title('Choose Date of Birth')
    date_window.geometry('250x220+590+370')
    
    cal = tkcal.Calendar(date_window, selectmode='day', date_pattern='mm/dd/yyyy', 
                         background='black', foreground='white', headersbackground='sky blue', 
                         normalbackground='lightblue', weekendbackground='lightblue', 
                         othermonthforeground='grey', othermonthbackground='lightgrey', 
                         othermonthweforeground='grey', othermonthwebackground='lightgrey', 
                         selectbackground='blue', selectforeground='white')
    cal.place(x=0, y=0)

    submit_btn = tk.Button(date_window, text='Submit', command=lambda: grab_date(dob_entry), bg='#0055fe', fg='white', font=('yu gothic ui', 12))
    submit_btn.place(x=80, y=190)

def grab_date(dob_entry):
    dob_entry.delete(0, tk.END)
    dob_entry.insert(0, cal.get_date())
    date_window.destroy()

def get_data(first_name_TextField, last_name_TextField, dob_entry, dept_combobox): #from fields
    id = generate_id()
    print(id)
    firstname = first_name_TextField.get()
    lastname = last_name_TextField.get()
    dob = dob_entry.get()
    dept = dept_combobox.get()
    insertData(id, firstname, lastname, dob, dept)
    
