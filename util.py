import os
from tkinter import messagebox
import cv2
import tkinter as tk
import tkcalendar as tkcal
from db_operations import generate_id, insertData, getDetails

def takePhoto():

    video_capture = cv2.VideoCapture(0)
    global id
    id = generate_id()

    while True:
        ret, frame = video_capture.read()

        cv2.imshow('frame', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('c'):
            cv2.imwrite("RegisteredFaces/"+str(id) + ".jpg", frame)
            cv2.waitKey(2000)
            break

        

    video_capture.release() 

    cv2.destroyAllWindows() 

def takePhoto(idTextField):

    id = idTextField.get()
    print(id)
    if os.path.exists("RegisteredFaces/"+str(id) + ".jpg"):
        os.remove("RegisteredFaces/"+str(id) + ".jpg")
    
    video_capture = cv2.VideoCapture(0)
        
    while True:
        ret, frame = video_capture.read()

        cv2.imshow('frame', frame)
            
        if cv2.waitKey(1) & 0xFF == ord('c'):
            cv2.imwrite("RegisteredFaces/"+str(id) + ".jpg", frame)
            cv2.waitKey(2000)
            messagebox.showinfo("Success ","Recorded has been Updated")
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
                         othermonthweforeground='grey', othermonthwebackgroundd='lightgrey', 
                         selectbackground='blue', selectforeground='white')
    cal.place(x=0, y=0)

    submit_btn = tk.Button(date_window, text='Submit', command=lambda: grab_date(dob_entry), bg='#0055fe', fg='white', font=('yu gothic ui', 12))
    submit_btn.place(x=80, y=190)

from datetime import datetime

def grab_date(dob_entry):
    dob_entry.delete(0, tk.END)
    
    # Get the date string from the calendar in MM/DD/YYYY format
    date_str = cal.get_date()  
    
    # Convert the string to a datetime object
    date_obj = datetime.strptime(date_str, '%m/%d/%Y')

    # Format the date in YYYY-MM-DD format
    formatted_date = date_obj.strftime('%Y-%m-%d')

    # Insert the formatted date into the entry widget
    dob_entry.insert(0, formatted_date)

    # Close the date window
    date_window.destroy()


def get_data(first_name_TextField, last_name_TextField, dob_entry, dept_combobox): #from fields

    if first_name_TextField.get() == "" or last_name_TextField.get() == "" or dob_entry.get() == "" or dept_combobox.get() == "--select Dept--":
        messagebox.showerror("Error", "Error: Please fill all the fields")
    else:
        firstname = first_name_TextField.get()
        lastname = last_name_TextField.get()
        dob = dob_entry.get()
        dept = dept_combobox.get()
        if insertData(id, firstname, lastname, dob, dept):
            first_name_TextField.delete(0, tk.END)
            last_name_TextField.delete(0, tk.END)
            dob_entry.delete(0, tk.END)

def retrieveData(id_TextField, first_name_TextField, last_name_TextField, dob_entry, dept_combobox):
    id = id_TextField.get()
    firstname, lastname, dob, dept = getDetails(id)

    first_name_TextField.delete(0, tk.END)
    first_name_TextField.insert(0, firstname)
    
    last_name_TextField.delete(0, tk.END)
    last_name_TextField.insert(0, lastname)
    
    dob_entry.delete(0, tk.END)
    dob_entry.insert(0, dob)
    
   
    dept_combobox.set(dept)

def fillData(id_TextField, first_name_TextField, last_name_TextField, dob_entry, dept_TextField):
    id = id_TextField.get()

    
    first_name_TextField.configure(state = 'normal')
    last_name_TextField.configure(state = 'normal')
    dob_entry.configure(state = 'normal')
    dept_TextField.configure(state = 'normal')

    firstname, lastname, dob, dept = getDetails(id)

    first_name_TextField.delete(0, tk.END)
    first_name_TextField.insert(0, firstname)
    
    last_name_TextField.delete(0, tk.END)
    last_name_TextField.insert(0, lastname)
    
    dob_entry.delete(0, tk.END)
    dob_entry.insert(0, dob)

    dept_TextField.delete(0,tk.END)
    dept_TextField.insert(0, dept)

    
    first_name_TextField.configure(state = 'disabled')
    last_name_TextField.configure(state = 'disabled')
    dob_entry.configure(state = 'disabled')
    dept_TextField.configure(state = 'disabled')

