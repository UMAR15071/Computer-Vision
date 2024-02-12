import tkinter as tk
import tkcalendar as tkcal
from tkinter import ttk

window = tk.Tk()
window.geometry('1000x600')
window.title('Screen')
window.configure(bg='#848884')  

first_frame = tk.Frame(window, bg='#c3c3c3')

def close_screens():
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

#==============================================================================================================
def moreOptions():
    close_screens()

    def home_page():
        home_frame = tk.Frame(main_frame, highlightbackground='#FAF9F6', bg='#FAF9F6',
                        highlightthickness=2)

        home_frame.pack(side=tk.LEFT)
        home_frame.pack_propagate(False)
        home_frame.configure(height=600, width=700)

        home_label = tk.Label(home_frame, text = "Welcome [User]", font=('bold', 15),
                                fg='black', bd=0, bg='#FAF9F6')
        home_label.pack(pady=10)
#=================================================================================================================
        
    def register_page():
        register_frame = tk.Frame(main_frame, highlightbackground='#FAF9F6', bg='#FAF9F6',
                                    highlightthickness=2)
        register_frame.pack(side=tk.LEFT)
        register_frame.pack_propagate(False)
        register_frame.configure(height=600, width=700)

        register_label = tk.Label(register_frame, text = "Register New User", font=('bold', 15),
                                    fg='black', bg='#FAF9F6')
        register_label.pack(pady=10)

        first_name_label = tk.Label(register_frame, text="First Name", font=('bold', 15), fg='black', bg='#FAF9F6' )
        first_name_label.place(x=100, y=100)
        first_name_TextField = tk.Entry(register_frame, width=15, font=2)
        first_name_TextField.place(x=400, y=100)

        last_name_label = tk.Label(register_frame, text="Last Name", font=('bold', 15), fg='black', bg='#FAF9F6' )
        last_name_label.place(x=100, y=150)
        last_name_TextField = tk.Entry(register_frame, width=15, font=2)
        last_name_TextField.place(x=400, y=150)

        dob_label = tk.Label(register_frame, text='Date of Birth', font=('bold', 15), fg='black', bg='#FAF9F6')
        dob_label.place(x=100, y=200)

        dob_entry = tk.Entry(register_frame, width=15, font=2)
        dob_entry.place(x=400, y=200)
        dob_entry.insert(0, 'mm/dd/yyyy')
        dob_entry.bind('<Button-1>',lambda event: pick_date(dob_entry))

        dept_label = tk.Label(register_frame, text='Department', font=('bold', 15), fg='black', bg='#FAF9F6')
        dept_label.place(x=100, y=250)

        dept_combobox = ttk.Combobox(register_frame, values=["--select Dept--", "HR", "Computing", "Marketing", "Managing", "Engineering"],width=14, font=2, state='readonly')
        dept_combobox.place(x=400, y=250)

        photos_btn = tk.Button(register_frame, text="Take Photo", font=('bold', 15), width=55, fg='#FAF9F6', bg='black')
        photos_btn.place(x=50, y=350)

        submit_btn = tk.Button(register_frame, text="Submit", font=('bold', 15), width=55, fg='#FAF9F6', bg='#008000')
        dob_label.place(x=100, y=200)
        submit_btn.place(x=50, y=400)

#==================================================================================================================

#==================================================================================================================

    def update_page():
        pass

#===================================================================================================================
    
    def delete_pages():
        for frame in main_frame.winfo_children():
            frame.destroy()

    def hide_indicate():
        home_indicate.config(bg='black')
        create_indicate.config(bg='black')
        update_indicate.config(bg='black')
        view_indicate.config(bg='black')
        report_indicate.config(bg='black')

    def indicate(lb, page):
        delete_pages()
        hide_indicate()
        lb.config(bg='#FAF9F6')
        page()
   #===================================== New Frame=================================================== 
    options_frame = tk.Frame(window, bg='black')
    options_frame.pack(side = tk.LEFT)
    options_frame.pack_propagate(False)
    options_frame.configure(width=300, height=600)

    options_label = tk.Label(options_frame, text='Options', fg='#FAF9F6', bg='black', font=('bold', 20))
    options_label.pack( pady=10)
    #======================= Home Button ===============================================
    home_btn = tk.Button(options_frame, text='Home', font=('bold', 15),
                     fg='#FAF9F6', bd=0, bg='black',
                     command = lambda: indicate(home_indicate, home_page))
    
    home_btn.place(x=20, y=50)

    home_indicate = tk.Label(options_frame, text='', bg='black')
    home_indicate.place(x=1, y=50, width=5, height=40)

    #======================== Create BUtton ==============================================
    create_btn = tk.Button(options_frame, text='Add a new Record', font=('bold', 15),
                     fg='#FAF9F6', bd=0, bg='black',
                     command = lambda: indicate(create_indicate, register_page))
    
    create_btn.place(x=20, y=100)

    create_indicate = tk.Label(options_frame, text='', bg='black')
    create_indicate.place(x=1, y=100, width=5, height=40)

    #========================= Update Button ===================================================
    update_btn = tk.Button(options_frame, text='Update Record', font=('bold', 15),
                     fg='#FAF9F6', bd=0, bg='black',
                     command = lambda: indicate(update_indicate))
    
    update_btn.place(x=20, y=150)

    update_indicate = tk.Label(options_frame, text='', bg='black')
    update_indicate.place(x=1, y=150, width=5, height=40)

    #==================================View / Delete Button===============================================
    view_btn = tk.Button(options_frame, text='View/Delete Record', font=('bold', 15),
                     fg='#FAF9F6', bd=0, bg='black',
                     command = lambda: indicate(view_indicate))
    
    view_btn.place(x=20, y=200)

    view_indicate = tk.Label(options_frame, text='', bg='black')
    view_indicate.place(x=1, y=200, width=5, height=40)
    #======================================= Report Button =========================================
    report_btn = tk.Button(options_frame, text='Generate Report', font=('bold', 15),
                     fg='#FAF9F6', bd=0, bg='black',
                     command = lambda: indicate(report_indicate))
    
    report_btn.place(x=20, y=250)

    report_indicate = tk.Label(options_frame, text='', bg='black')
    report_indicate.place(x=1, y=250, width=5, height=40)
    #===================================== Back Button =============================================
    back_btn = tk.Button(options_frame, text='Back to Main Menu', font=('bold', 15))
    back_btn.configure(width=17, height=1, bg='#1f618d', fg='white')
    back_btn.place(x=50, y=500)

    #==================================== Main Frame =============================================
    main_frame = tk.Frame(window)
    main_frame = tk.Frame(window, highlightbackground='#FAF9F6', bg='#FAF9F6',
                        highlightthickness=2)


    main_frame.pack(side=tk.LEFT)
    main_frame.pack_propagate(False)
    main_frame.configure(height=600, width=700)

#======================================================================================================================
def main_menu():
    first_frame.pack(pady=150)
    first_frame.pack_propagate(False)
    first_frame.configure(width=500, height=300, relief="solid", border="2")

    start_btn = tk.Button(first_frame, text='Start Attendance', font=('bold', 15))
    start_btn.configure(width=25, height=2, bg="#008000", fg='white')
    start_btn.pack(padx=100, pady=52)

    options_btn = tk.Button(first_frame, text='More Options', font=('bold', 15))
    options_btn.configure(width=25, height=2, bg="#1f618d", fg="white",
                        command=lambda: moreOptions())
    options_btn.pack(padx=100, pady=5)

main_menu()

window.mainloop()