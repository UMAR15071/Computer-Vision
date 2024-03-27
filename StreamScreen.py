import datetime
import tkinter as tk
from util import close_screens
from PIL import Image, ImageTk
import numpy as np
import cv2
import os
import face_recognition
from db_operations import getDetails, clockIn, clockOut, checkMarked, establish_Connection

def stream_screen(window, main_menu):
    global process_this_frame
    process_this_frame = 0
    close_screens(window)
    establish_Connection()

    FOLDER = "RegisteredFaces"
    files = os.listdir(FOLDER)

    # ... [Your existing code for setting up the options frame and buttons]
    options_frame = tk.Frame(window, bg='black')
    options_frame.pack(side = tk.RIGHT)
    options_frame.pack_propagate(False)
    options_frame.configure(width=300, height=600)

    id_label = tk.Label(options_frame, text="ID", font=('bold', 15), fg='#FAF9F6', bg='black' )
    id_label.place(x=50, y=100)

    first_name_label = tk.Label(options_frame, text="Name", font=('bold', 15), fg='#FAF9F6', bg='black' )
    first_name_label.place(x=50, y=130)

    dept_label = tk.Label(options_frame, text="Dept", font=('bold', 15), fg='#FAF9F6', bg='black' )
    dept_label.place(x=50, y=160)

    def change(id, firstname, lastname, dept):
        id_label.configure(text="ID: "+id)
        first_name_label.configure(text="Name: "+firstname+ " " + lastname)
        dept_label.configure(text="Department: "+dept)
        

    def changeState(id):
        date = datetime.date.today().strftime("%Y-%m-%d")
        marked = checkMarked(id,date)
        if marked:
            clockout_btn.configure(state='normal')
            clockin_btn.configure(state='disable')
        else:
            clockin_btn.configure(state='normal')
            clockout_btn.configure(state='disable')
        

    clockin_btn = tk.Button(options_frame, width=17, height=1, text='Clock In', font=('bold', 15),
                            bg="#008000", fg='#FAF9F6', state='disabled',
                            command=lambda: clockIn(id))
    
    clockin_btn.place(x=50, y=400)

    clockout_btn = tk.Button(options_frame, width=17, height=1, text='Clock Out', font=('bold', 15),
                            fg='#FAF9F6', bg='#D2042D',state='disabled', command=lambda: clockOut(id))
    
    clockout_btn.place(x=50, y=450)

    stop_btn = tk.Button(options_frame, width=17, height=1, text='Stop Streaming', font=('bold', 15),
                            bg="#1f618d", fg="#FAF9F6", command=lambda: close_cam(main_menu))
    
    stop_btn.place(x=50, y=500)

    known_face_ids = []
    known_face_encodings = []
    for file in files:
        image = face_recognition.load_image_file(f"{FOLDER}/{file}")
        face_encoding = face_recognition.face_encodings(image)
        if face_encoding:
            known_face_encodings.append(face_encoding[0])
            id = file.removesuffix('.jpg')
            known_face_ids.append(id)

    cam_frame = tk.Frame(window, highlightbackground='#FAF9F6', bg='#FAF9F6', highlightthickness=2)
    cam_frame.pack(side=tk.LEFT)
    cam_frame.pack_propagate(False)
    cam_frame.configure(height=600, width=700, bg='white')
    video_canvas = tk.Canvas(cam_frame, height=600, width=700, bg='white')
    video_canvas.pack()
    cap = cv2.VideoCapture(0)

    def open_cam():
        global process_this_frame
        ret, frame = cap.read()

        if ret:
            cv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_image = Image.fromarray(cv_image)
            imgtk = ImageTk.PhotoImage(image=pil_image)
            video_canvas.create_image(25, 50, anchor=tk.NW, image=imgtk)
            video_canvas.image = imgtk
            
            if process_this_frame % 50 == 0:
                face_locations = face_recognition.face_locations(cv_image)
                face_encodings = face_recognition.face_encodings(cv_image, face_locations)

                face_ids = []
                for face_encoding in face_encodings:
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                    global id 
                    id = "unknown"
                    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        id = known_face_ids[best_match_index]
                    face_ids.append(id)
                    firstname, lastname, dept = getDetails(id)
                    change(id,firstname,lastname,dept)
                    changeState(id)
                    
                
            process_this_frame += 1



            video_canvas.after(20, open_cam)

    open_cam()

    def close_cam(main_menu):
        cap.release()
        video_canvas.delete("all")
        main_menu()

