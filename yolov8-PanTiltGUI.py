from tkinter import *
import cv2
import numpy as np
from PIL import Image, ImageTk
from ultralytics import YOLO
#import motor

yolo = YOLO("yolov8n.pt")

window = Tk()
window.wm_title("Pan Tilt Camera Controller")
window.config(background="#ADD8E6")
win_width = window.winfo_screenwidth()
win_height = window.winfo_screenheight()
window.geometry("%dx%d" % (win_width, win_height))

#LEFT FRAME
left_Frame = Frame(window, width=win_width*0.65, height=win_height, bg="#ADD8E6")
left_Frame.pack(side=LEFT)

cam = Label(left_Frame, bg="#ADD8E6")
cam.place(x= 10, y=450)

cap = cv2.VideoCapture(0)


# Function to perform object detection
def perform_object_detection(frame):
    # Perform YOLO object detection
    results = yolo(frame)    
    
    # Extract bounding box coordinates and labels
    #boxes = results.xyxy[0].cpu().numpy()
    
    # Draw bounding boxes on the frame
    while True:
        for result in results:
            boxes = result.boxes
            probs = result.probs
    

    return frame

# Function to update the displayed video stream
def show_video():
    ret, frame = cap.read()
    if not ret:
        cam.config(text="Camera not plugged in. Please insert a camera!", font=("Arial", 30))
    else:
        frame_flip = cv2.flip(frame, 0)
        frame_resized = cv2.resize(frame_flip, (int(win_width * 0.75), win_height))
        
        # Perform object detection on the frame
        frame_with_detection = perform_object_detection(frame_resized)
        
        # Convert the frame to ImageTk format
        cv2image = cv2.cvtColor(frame_with_detection, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        
        # Update the GUI
        cam.imgtk = imgtk
        cam.config(image=imgtk)

    # Repeat after an interval to capture continuously
    cam.after(10, show_video)




#RIGHT FRAME
right_Frame = Frame(window, width=win_width*0.25, height=win_height, bg="#ADD8E6")
right_Frame.pack(side=RIGHT)

#BUTTON FRAME
btn_Frame = Frame(right_Frame, width=0, height=win_height, bg="#ADD8E6")
btn_Frame.grid(row=1, column=0, rowspan=4, sticky="nsew")

pic_width = round(win_width * 0.072)
pic_height = round(pic_width)
#Open Images to Resize
up_arrow = Image.open("up_arrow.png")
dn_arrow = Image.open("down_arrow.png")
lt_arrow = Image.open("left_arrow.png")
rt_arrow = Image.open("right_arrow.png")
stop_button = Image.open("stop.png")
reset_button = Image.open("reset.png")
power_button = Image.open("power_on.png")

#Resize Images
resized_up = up_arrow.resize((pic_width, pic_height))
new_up = ImageTk.PhotoImage(resized_up)
resized_down = dn_arrow.resize((pic_width, pic_height))
new_down = ImageTk.PhotoImage(resized_down)
resized_left = lt_arrow.resize((pic_width, pic_height))
new_left = ImageTk.PhotoImage(resized_left)
resized_right = rt_arrow.resize((pic_width, pic_height))
new_right = ImageTk.PhotoImage(resized_right)
resized_stop = stop_button.resize((pic_width, pic_height))
new_stop = ImageTk.PhotoImage(resized_stop)
resized_reset = reset_button.resize((pic_width, pic_height))
new_reset = ImageTk.PhotoImage(resized_reset)
resized_power = power_button.resize((pic_width, pic_height))
new_power = ImageTk.PhotoImage(resized_power)

label_height = round(pic_height/5)
space_width = round(pic_width/120)
up_btn = Button(btn_Frame, bg="#ADD8E6", width=0, height=0, image=new_up, command= lambda: motor.elevation_anti_clockwise())
up_btn.grid(row=2, column=2)

space1 = Label(btn_Frame, bg="#ADD8E6", font=("Times New Roman", label_height))
space1.grid(row=3, columnspan=4)

left_btn = Button(btn_Frame, bg="#ADD8E6", width=0, height=0, image=new_left, command=lambda: motor.azimuth_anti_clockwise())
left_btn.grid(row=4, column=0)

space2 = Label(btn_Frame, bg="#ADD8E6", font=("Times New Roman", label_height), width=space_width)
space2.grid(row=4, column=1)

stop_btn = Button(btn_Frame, bg="#ADD8E6", width=0, height=0, image=new_stop)
stop_btn.grid(row=4, column=2)

space3 = Label(btn_Frame, bg="#ADD8E6", font=("Times New Roman", label_height), width=space_width)
space3.grid(row=4, column=3)

right_btn = Button(btn_Frame, bg="#ADD8E6", width=0, height=0, image=new_right, command=lambda: motor.azimuth_clockwise())
right_btn.grid(row=4, column=4)

space4 = Label(btn_Frame, bg="#ADD8E6", font=("Times New Roman", label_height))
space4.grid(row=5, columnspan=4)

down_btn = Button(btn_Frame, bg="#ADD8E6", width=0, height=0, image=new_down, command=lambda: motor.elevation_clockwise())
down_btn.grid(row=6, column=2)

space4 = Label(btn_Frame, bg="#ADD8E6", font=("Times New Roman", label_height))
space4.grid(row=7, columnspan=4)

reset_btn = Button(btn_Frame, bg="#ADD8E6", width=0, height=0, image=new_reset)
reset_btn.grid(row=8, column=0)

power_btn = Button(btn_Frame, bg="#ADD8E6", width=0, height=0, image=new_power, command=lambda: toggle_scan())
power_btn.grid(row=8, column=4)

show_video()
window.mainloop()
                                                                                                                                                
