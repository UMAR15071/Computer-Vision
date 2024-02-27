import tkinter as tk
from util import close_screens

def stream_screen(window, main_menu):
    close_screens(window)

    options_frame = tk.Frame(window, bg='black')
    options_frame.pack(side = tk.RIGHT)
    options_frame.pack_propagate(False)
    options_frame.configure(width=300, height=600)

    clockin_btn = tk.Button(options_frame, width=17, height=1, text='Clock In', font=('bold', 15),
                            bg="#008000", fg='#FAF9F6')
    
    clockin_btn.place(x=50, y=400)

    clockout_btn = tk.Button(options_frame, width=17, height=1, text='Clock Out', font=('bold', 15),
                            fg='#FAF9F6', bg='#D2042D')
    
    clockout_btn.place(x=50, y=450)

    stop_btn = tk.Button(options_frame, width=17, height=1, text='Stop Streaming', font=('bold', 15),
                            bg="#1f618d", fg="#FAF9F6", command=lambda: main_menu())
    
    stop_btn.place(x=50, y=500)



    cam_frame = tk.Frame(window)
    cam_frame = tk.Frame(window, highlightbackground='#FAF9F6', bg='#FAF9F6',
                        highlightthickness=2)


    cam_frame.pack(side=tk.LEFT)
    cam_frame.pack_propagate(False)
    cam_frame.configure(height=600, width=700)