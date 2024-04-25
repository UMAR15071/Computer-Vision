import tkinter as tk
from tkinter import ttk
from util import takePhoto, close_screens, pick_date,get_data, retrieveData, fillData, updatePhoto
from db_operations import establish_Connection, updateRecord, deleteRecord, getReport


#==============================================================================================================
def moreOptions(window, main_menu):
    close_screens(window)
    establish_Connection()

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
        dob_entry.insert(0, 'yyyy-mm-dd')
        dob_entry.bind('<Button-1>',lambda event: pick_date(dob_entry))

        dept_label = tk.Label(register_frame, text='Department', font=('bold', 15), fg='black', bg='#FAF9F6')
        dept_label.place(x=100, y=250)

        dept_combobox = ttk.Combobox(register_frame, values=["--select Dept--", "HR", "Computing", "Marketing", "Managing", "Engineering"],width=14, font=2, state='readonly')
        dept_combobox.place(x=400, y=250)

        photos_btn = tk.Button(register_frame, text="Take Photo", font=('bold', 15), width=55, fg='#FAF9F6', bg='black',
                               command = lambda: takePhoto())
        photos_btn.place(x=50, y=350)

        submit_btn = tk.Button(register_frame, text="Submit", font=('bold', 15), width=55, fg='#FAF9F6', bg='#008000',
                               command=lambda: get_data(first_name_TextField, last_name_TextField, dob_entry, dept_combobox))
        dob_label.place(x=100, y=200)
        submit_btn.place(x=50, y=400)

#==================================================================================================================

#==================================================================================================================

    def update_page():
        update_frame = tk.Frame(main_frame, highlightbackground='#FAF9F6', bg='#FAF9F6',
                                    highlightthickness=2)
        update_frame.pack(side=tk.LEFT)
        update_frame.pack_propagate(False)
        update_frame.configure(height=600, width=700)

        update_label = tk.Label(update_frame, text = "Update User", font=('bold', 15),
                                    fg='black', bg='#FAF9F6')
        update_label.pack(pady=10)

        id_label = tk.Label(update_frame, text="Emplyee ID", font=('bold', 15), fg='black', bg='#FAF9F6' )
        id_label.place(x=100, y=100)
        id_TextField = tk.Entry(update_frame, width=15, font=2)
        id_TextField.place(x=400, y=100)

        submit_btn = tk.Button(update_frame, text="Search", font=('bold', 15), width=55, fg='#FAF9F6', bg='#1f618d',
                               command=lambda: retrieveData(id_TextField, first_name_TextField, last_name_TextField, dob_entry, dept_combobox))
        submit_btn.place(x=50, y=150)

        first_name_label = tk.Label(update_frame, text="First Name", font=('bold', 15), fg='black', bg='#FAF9F6' )
        first_name_label.place(x=100, y=200)
        first_name_TextField = tk.Entry(update_frame, width=15, font=2)
        first_name_TextField.place(x=400, y=200)

        last_name_label = tk.Label(update_frame, text="Last Name", font=('bold', 15), fg='black', bg='#FAF9F6' )
        last_name_label.place(x=100, y=250)
        last_name_TextField = tk.Entry(update_frame, width=15, font=2)
        last_name_TextField.place(x=400, y=250)

        dob_label = tk.Label(update_frame, text='Date of Birth', font=('bold', 15), fg='black', bg='#FAF9F6')
        dob_label.place(x=100, y=300)
        dob_entry = tk.Entry(update_frame, width=15, font=2)
        dob_entry.place(x=400, y=300)
        dob_entry.insert(0, 'yyyy-mm-dd')
        dob_entry.bind('<Button-1>',lambda event: pick_date(dob_entry))

        dept_label = tk.Label(update_frame, text='Department', font=('bold', 15), fg='black', bg='#FAF9F6')
        dept_label.place(x=100, y=350)
        dept_combobox = ttk.Combobox(update_frame, values=["--select Dept--", "HR", "Computing", "Marketing", "Managing", "Engineering"],width=14, font=2, state='readonly')
        dept_combobox.place(x=400, y=350)

        photos_btn = tk.Button(update_frame, text="Update Photo", font=('bold', 15), width=55, fg='#FAF9F6', bg='black',
                               command= lambda: updatePhoto(id_TextField))
        photos_btn.place(x=50, y=400)

        submit_btn = tk.Button(update_frame, text="Update", font=('bold', 15), width=55, fg='#FAF9F6', bg='#D2042D',
                               command= lambda: updateRecord(id_TextField, first_name_TextField, last_name_TextField, dob_entry, dept_combobox))
        submit_btn.place(x=50, y=450)
#=====================================================================================================================================
    def view_page():
        view_frame = tk.Frame(main_frame, highlightbackground='#FAF9F6', bg='#FAF9F6',
                                    highlightthickness=2)
        view_frame.pack(side=tk.LEFT)
        view_frame.pack_propagate(False)
        view_frame.configure(height=600, width=700)

        update_label = tk.Label(view_frame, text = "View/Delete User Record", font=('bold', 15),
                                    fg='black', bg='#FAF9F6')
        update_label.pack(pady=10)

        id_label = tk.Label(view_frame, text="Employee ID", font=('bold', 15), fg='black', bg='#FAF9F6' )
        id_label.place(x=100, y=100)
        id_TextField = tk.Entry(view_frame, width=15, font=2)
        id_TextField.place(x=400, y=100)    

        submit_btn = tk.Button(view_frame, text="Search", font=('bold', 15), width=55, fg='#FAF9F6', bg='#1f618d',
                               command=lambda: fillData(id_TextField, first_name_TextField, last_name_TextField, dob_entry, dept_textField))
        submit_btn.place(x=50, y=150)

        first_name_label = tk.Label(view_frame, text="First Name", font=('bold', 15), fg='black', bg='#FAF9F6' )
        first_name_label.place(x=100, y=200)
        first_name_TextField = tk.Entry(view_frame, width=15, font=2, state='disabled')
        first_name_TextField.place(x=400, y=200)

        last_name_label = tk.Label(view_frame, text="Last Name", font=('bold', 15), fg='black', bg='#FAF9F6' )
        last_name_label.place(x=100, y=250)
        last_name_TextField = tk.Entry(view_frame, width=15, font=2, state='disabled')
        last_name_TextField.place(x=400, y=250)

        dob_label = tk.Label(view_frame, text='Date of Birth', font=('bold', 15), fg='black', bg='#FAF9F6')
        dob_label.place(x=100, y=300)
        dob_entry = tk.Entry(view_frame, width=15, font=2, state='disabled')
        dob_entry.place(x=400, y=300)

        dept_label = tk.Label(view_frame, text='Department', font=('bold', 15), fg='black', bg='#FAF9F6')
        dept_label.place(x=100, y=350)
        dept_textField = tk.Entry(view_frame, width=15, font=2, state='disabled')
        dept_textField.place(x=400, y=350)

        delete_btn = tk.Button(view_frame, text="Delete", font=('bold', 15), width=55, fg='#FAF9F6', bg='#D2042D',
                               command= lambda: deleteRecord(id_TextField.get(), first_name_TextField, last_name_TextField, dob_entry, dept_textField))
        delete_btn.place(x=50, y=400)

#===================================================================================================================
    def report_page():
        report_frame = tk.Frame(main_frame, highlightbackground='#FAF9F6', bg='#FAF9F6',
                                    highlightthickness=2)
        report_frame.pack(side=tk.LEFT)
        report_frame.pack_propagate(False)
        report_frame.configure(height=600, width=700)

        home_label = tk.Label(report_frame, text = "Generate Report", font=('bold', 15),
                                fg='black', bd=0, bg='#FAF9F6')
        home_label.pack(pady=10)

        date_label = tk.Label(report_frame, text='Date', font=('bold', 15), fg='black', bg='#FAF9F6')
        date_label.place(x=100, y=100)

        date_entry = tk.Entry(report_frame, width=15, font=2)
        date_entry.place(x=400, y=100)
        date_entry.insert(0, 'yyyy-mm-dd')
        date_entry.bind('<Button-1>',lambda event: pick_date(date_entry))

        submit_btn = tk.Button(report_frame, text="Submit", font=('bold', 15), width=55, fg='#FAF9F6', bg='#008000',
                               command=lambda: getReport(date_entry.get(), trv))
        submit_btn.place(x=50, y=150)

        trv = ttk.Treeview(report_frame)
        trv.configure(height=15) 
        trv.place(x=55, y=200)
        trv["columns"] = ['1', '2', '3', '4']
        trv['show'] = 'headings'

        trv.column("1", width = 150, anchor ='c')
        trv.column("2", width = 150, anchor ='c')
        trv.column("3", width = 150, anchor ='c')
        trv.column("4", width = 150, anchor ='c')

        trv.heading("1", text ="First Name")
        trv.heading("2", text ="Last Name")
        trv.heading("3", text ="Clock In")
        trv.heading("4", text ="Clock Out")  
        
#====================================================================================================================    
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
   #===================================== New Frame =================================================== 
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
                     command = lambda: indicate(update_indicate, update_page))
    
    update_btn.place(x=20, y=150)

    update_indicate = tk.Label(options_frame, text='', bg='black')
    update_indicate.place(x=1, y=150, width=5, height=40)

    #==================================View / Delete Button===============================================
    view_btn = tk.Button(options_frame, text='View/Delete Record', font=('bold', 15),
                     fg='#FAF9F6', bd=0, bg='black',
                     command = lambda: indicate(view_indicate, view_page))
    
    view_btn.place(x=20, y=200)

    view_indicate = tk.Label(options_frame, text='', bg='black')
    view_indicate.place(x=1, y=200, width=5, height=40)
    #======================================= Report Button =========================================
    report_btn = tk.Button(options_frame, text='Generate Report', font=('bold', 15),
                     fg='#FAF9F6', bd=0, bg='black',
                     command = lambda: indicate(report_indicate, report_page))
    
    report_btn.place(x=20, y=250)

    report_indicate = tk.Label(options_frame, text='', bg='black')
    report_indicate.place(x=1, y=250, width=5, height=40)
    #===================================== Back Button =============================================
    back_btn = tk.Button(options_frame, text='Back to Main Menu', font=('bold', 15))
    back_btn.configure(width=17, height=1, bg='#1f618d', fg='white', command=lambda: main_menu())
    back_btn.place(x=50, y=500)

    #==================================== Main Frame =============================================
    main_frame = tk.Frame(window)
    main_frame = tk.Frame(window, highlightbackground='#FAF9F6', bg='#FAF9F6',
                        highlightthickness=2)


    main_frame.pack(side=tk.LEFT)
    main_frame.pack_propagate(False)
    main_frame.configure(height=600, width=700)
    home_page()