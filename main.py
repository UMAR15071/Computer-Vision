import tkinter as tk
from moreOptions import moreOptions,close_screens
from StreamScreen import stream_screen
from db_operations import connected, connectionClose


window = tk.Tk()
window.geometry('1000x600')
window.title('Screen')
window.configure(bg='#848884') 
#======================================================================================================================
def main_menu():
    close_screens(window)
    if connected():
        connectionClose()
    
    first_frame = tk.Frame(window, bg='#c3c3c3')
    first_frame.pack(pady=150)
    first_frame.pack_propagate(False)
    first_frame.configure(width=500, height=300, relief="solid", border="2")

    start_btn = tk.Button(first_frame, text='Start Attendance', font=('bold', 15))
    start_btn.configure(width=25, height=2, bg="#008000", fg='white',
                        command=lambda: stream_screen(window, main_menu))
    start_btn.pack(padx=100, pady=52)

    options_btn = tk.Button(first_frame, text='More Options', font=('bold', 15))
    options_btn.configure(width=25, height=2, bg="#1f618d", fg="white",
                        command=lambda: moreOptions(window, main_menu))
    options_btn.pack(padx=100, pady=5)

main_menu()
window.mainloop()