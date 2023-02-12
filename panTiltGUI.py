from tkinter import *
import cv2
import numpy as np
from PIL import Image, ImageTk

window = Tk()
window.wm_title("Pan Tilt Camera Controller")
window.config(background="#5C6B9C")
win_width = window.winfo_screenwidth()
win_height = window.winfo_screenheight()
window.geometry("%dx%d" % (win_width, win_height))

#LEFT FRAME
left_Frame = Frame(window, width=win_width*0.75, height=win_height, bg="#5C6B9C")
left_Frame.pack(side=LEFT)

cam = Label(left_Frame)
cam.grid(row=1, column=0)
cap = cv2.VideoCapture(0)


def show_video():
    ret, frame = cap.read()
    if not ret:
        no_cam = Label(left_Frame, text="Camera not plugged in. Please insert camera!", bg="#5C6B9C", font=("Arial", 20))
        no_cam.grid(row=0, column=0, columnspan=4, rowspan=1)
        
    else:
        #get latest frame and convert to image
        cv2image = cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
        img =Image.fromarray(cv2image)
        #convert image to PhotoImage
        imgtk = ImageTk.PhotoImage(image = img)
        cam.imgtk = imgtk
        cam.configure(image=imgtk)
        #re[eat after an interval to capture continuously
        cam.after(20, show_video)


#RIGHT FRAME
right_Frame = Frame(window, width=win_width*0.25, height=win_height, bg="#5C6B9C")
right_Frame.pack(side=RIGHT)

#BUTTON FRAME
btn_Frame = Frame(right_Frame, width=0, height=win_height, bg="#ADD8E6")
btn_Frame.grid(row=1, column=0, rowspan=4, sticky="nsew")

pic_height = round(win_height * 0.25)
pic_width = round(pic_height)
#Open Images to Resize
up_arrow = Image.open("up_arrow.png")
dn_arrow = Image.open("down_arrow.png")
lt_arrow = Image.open("left_arrow.png")
rt_arrow = Image.open("right_arrow.png")

#Resize Images
resized_up = up_arrow.resize((pic_width, pic_height))
new_up = ImageTk.PhotoImage(resized_up)
resized_down = dn_arrow.resize((pic_width, pic_height))
new_down = ImageTk.PhotoImage(resized_down)
resized_left = lt_arrow.resize((pic_width, pic_height))
new_left = ImageTk.PhotoImage(resized_left)
resized_right = rt_arrow.resize((pic_width, pic_height))
new_right = ImageTk.PhotoImage(resized_right)

up_btn = Button(btn_Frame, bg="#ADD8E6", width=0, height=0, image=new_up)
up_btn.grid(row=0, column=1)

down_btn = Button(btn_Frame, bg="#ADD8E6", width=0, height=0, image=new_down)
down_btn.grid(row=2, column=1)

left_btn = Button(btn_Frame, bg="#ADD8E6", width=0, height=0, image=new_left)
left_btn.grid(row=1, column=0)

right_btn = Button(btn_Frame, bg="#ADD8E6", width=0, height=0, image=new_right)
right_btn.grid(row=1, column=2)

label_height = round(pic_height/10)
#Displaying Position in x,y,z axis
space1 = Label(btn_Frame, text="", bg="#ADD8E6", width=5)
space1.grid(row=3, column=0)

x_label = Label(btn_Frame, text="x-axis:", bg="#ADD8E6", width=5, font=("Times New Roman", label_height))
x_label.grid(row=4, column=0)

y_label = Label(btn_Frame, text="y-axis:", bg="#ADD8E6", width=5, font=("Times New Roman", label_height))
y_label.grid(row=5, column=0)

z_label = Label(btn_Frame, text="z-axis:", bg="#ADD8E6", width=5, font=("Times New Roman", label_height))
z_label.grid(row=6, column=0)

space2 = Label(btn_Frame, text="", bg="#ADD8E6", width=5)
space2.grid(row=7, column=0)

#Entry Fields to specify positions of x,y,z axis
x_entry = Entry(btn_Frame, bg="#FFFFFF", font=("Times New Roman", label_height))
x_entry.grid(row=4, column=1)
y_entry = Entry(btn_Frame, bg="#FFFFFF", font=("Times New Roman", label_height))
y_entry.grid(row=5, column=1)
z_entry = Entry(btn_Frame, bg="#FFFFFF", font=("Times New Roman", label_height))
z_entry.grid(row=6, column=1)

show_video()
window.mainloop()
