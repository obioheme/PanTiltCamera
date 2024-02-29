import cv2
import tkinter as tk
from PIL import Image, ImageTk
from picamera2 import Picamera2
from ultralytics import YOLO
import cvzone
import numpy as np
import threading
import motor

class ObjectDetectionGUI:
    
    # Flag to track the scan state
    scan_running = False
    def toggle_scan(self):
        if self.scan_running:
            # Stop motor if scan is running
            motor.stop_motor()
            self.scan_running = False
        else:
            # Start scan if not running
            threading.Thread(target=motor.start_scan).start()
            self.scan_running = True
    
    scan_left = False
    def turn_left(self):
        if self.scan_left:
            # Stop motor if scan is running
            motor.stop_motor()
            self.scan_left = False
        else:
            # Move left if not running
            threading.Thread(target=motor.pan_turn_clockwise).start()
            self.scan_left = True
            
    scan_right = False
    def turn_right(self):
        if self.scan_right:
            # Stop motor if scan is running
            motor.stop_motor()
            self.scan_right = False
        else:
            # Move right if not running
            threading.Thread(target=motor.pan_turn_anticlockwise).start()
            self.scan_right = True
    
    scan_up = False
    def move_up(self):
        if self.scan_up:
            # Stop motor if scan is running
            motor.stop_motor()
            self.scan_up = False
        else:
            # Move up if not running
            threading.Thread(target=motor.tilt_turn_anticlockwise).start()
            self.scan_up = True

    scan_down = False
    def move_down(self):
        if self.scan_down:
            # Stop motor if scan is running
            motor.stop_motor()
            self.scan_down = False
        else:
            # Move right if not running
            threading.Thread(target=motor.tilt_turn_clockwise).start()
            self.scan_down = True

    def __init__(self, root):
        self.root = root
        self.root.title("Pan Tilt Controller")
        self.root.config(background="#ADD8E6")

        # Left Frame for Video Display
        self.left_frame = tk.Frame(root, bg="#ADD8E6")
        self.left_frame.pack(side=tk.LEFT)

        # Right Frame for Control Buttons
        self.right_frame = tk.Frame(root, bg="#ADD8E6")
        self.right_frame.pack(side=tk.RIGHT)
        
        #BUTTON FRAME
        self.btn_Frame = tk.Frame(self.right_frame,bg="#ADD8E6")
        self.btn_Frame.grid(row=1, column=0, rowspan=4, sticky="nsew")

        # Initialize Picamera2 and YOLO model
        self.picam2 = Picamera2()
        self.picam2.preview_configuration.main.format = "RGB888"
        self.picam2.preview_configuration.align()
        self.picam2.configure("preview")
        self.picam2.start()

        self.model = YOLO('yolov8n.pt')

        # Load class list from 'coco.txt'
        with open("coco.txt", "r") as my_file:
            data = my_file.read()
            self.class_list = data.split("\n")

        # Left Frame components
        self.cam = tk.Label(self.left_frame)
        self.cam.pack()

        #Button Frame Components        
        pic_width = round(480*0.2)
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
        self.new_up = ImageTk.PhotoImage(resized_up)
        resized_down = dn_arrow.resize((pic_width, pic_height))
        self.new_down = ImageTk.PhotoImage(resized_down)
        resized_left = lt_arrow.resize((pic_width, pic_height))
        self.new_left = ImageTk.PhotoImage(resized_left)
        resized_right = rt_arrow.resize((pic_width, pic_height))
        self.new_right = ImageTk.PhotoImage(resized_right)
        resized_stop = stop_button.resize((pic_width, pic_height))
        self.new_stop = ImageTk.PhotoImage(resized_stop)
        resized_reset = reset_button.resize((pic_width, pic_height))
        self.new_reset = ImageTk.PhotoImage(resized_reset)
        resized_power = power_button.resize((pic_width, pic_height))
        self.new_power = ImageTk.PhotoImage(resized_power)

        label_height = round(pic_height/5)
        space_width = round(pic_width/120)

        self.up_btn = tk.Button(self.btn_Frame, bg="#ADD8E6", width=0, height=0, image=self.new_up, command=self.move_up)
        self.up_btn.grid(row=2, column=2)

        self.space1 = tk.Label(self.btn_Frame, bg="#ADD8E6", font=("Times New Roman", label_height))
        self.space1.grid(row=3, columnspan=4)

        self.left_btn = tk.Button(self.btn_Frame, bg="#ADD8E6", width=0, height=0, image=self.new_left, command=self.turn_left)
        self.left_btn.grid(row=4, column=0)

        self.space2 = tk.Label(self.btn_Frame, bg="#ADD8E6", font=("Times New Roman", label_height), width=space_width)
        self.space2.grid(row=4, column=1)

        self.stop_btn = tk.Button(self.btn_Frame, bg="#ADD8E6", width=0, height=0, image=self.new_stop, command=lambda: motor.stop_motor())
        self.stop_btn.grid(row=4, column=2)

        self.space3 = tk.Label(self.btn_Frame, bg="#ADD8E6", font=("Times New Roman", label_height), width=space_width)
        self.space3.grid(row=4, column=3)

        self.right_btn = tk.Button(self.btn_Frame, bg="#ADD8E6", width=0, height=0, image=self.new_right, command=self.turn_right)
        self.right_btn.grid(row=4, column=4)

        self.space4 = tk.Label(self.btn_Frame, bg="#ADD8E6", font=("Times New Roman", label_height))
        self.space4.grid(row=5, columnspan=4)

        self.down_btn = tk.Button(self.btn_Frame, bg="#ADD8E6", width=0, height=0, image=self.new_down, command=self.move_down)
        self.down_btn.grid(row=6, column=2)

        self.space4 = tk.Label(self.btn_Frame, bg="#ADD8E6", font=("Times New Roman", label_height))
        self.space4.grid(row=7, columnspan=4)

        self.reset_btn = tk.Button(self.btn_Frame, bg="#ADD8E6", width=0, height=0, image=self.new_reset, command=lambda: motor.reset_motor())
        self.reset_btn.grid(row=8, column=0)

        self.power_btn = tk.Button(self.btn_Frame, bg="#ADD8E6", width=0, height=0, image=self.new_power, command=self.toggle_scan)
        self.power_btn.grid(row=8, column=4)

        # Start video update
        self.update_video()

    def update_video(self):
        # Capture frame from Picamera2
        frame = self.picam2.capture_array()
        #frame = cv2.flip(frame, -1)

        # Perform object detection
        results = self.model.predict(frame)
        boxes = results[0].boxes.data

        for row in boxes:
            x1, y1, x2, y2, _, d = map(int, row)
            c = self.class_list[d]
            confidence = row[4]
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
            cvzone.putTextRect(frame, f'{c} {confidence: .2f}', (x1, y1), 1, 1)
        
        # Convert the frame to RGB and display it on the Tkinter GUI
        image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        photo = ImageTk.PhotoImage(image=image)
        #photo.resize(width=win_width*0.65, height=win_height)
        self.cam.config(image=photo)
        self.cam.image = photo

        # Schedule the next update
        self.root.after(10, self.update_video)

if __name__ == "__main__":
    root = tk.Tk()
    app = ObjectDetectionGUI(root)
    root.after(10, motor.start_scan)
    root.mainloop()
    
