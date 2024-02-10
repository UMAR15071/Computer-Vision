import tkinter as tk

window = tk.Tk()
window.geometry('1000x600')
window.title('Screen')
window.configure(bg='#848884')  

first_frame = tk.Frame(window, bg='#c3c3c3')

def close_screens():
    for frame in window.winfo_children():
        frame.destroy()




#==============================================================================================================
def moreOptions():
    close_screens()

    def hide_indicate():
        home_indicate.config(bg='black')
        create_indicate.config(bg='black')
        update_indicate.config(bg='black')
        view_indicate.config(bg='black')
        report_indicate.config(bg='black')

    def indicate(lb):
        hide_indicate()
        lb.config(bg='#FAF9F6')
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
                     command = lambda: indicate(home_indicate))
    
    home_btn.place(x=20, y=50)

    home_indicate = tk.Label(options_frame, text='', bg='black')
    home_indicate.place(x=1, y=50, width=5, height=40)

    #======================== Create BUtton ==============================================
    create_btn = tk.Button(options_frame, text='Add a new Record', font=('bold', 15),
                     fg='#FAF9F6', bd=0, bg='black',
                     command = lambda: indicate(create_indicate))
    
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
