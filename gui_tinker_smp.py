import cv2
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class VideoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Object Detection App")

        # Create left and right frames
        self.left_frame = ttk.Frame(root, padding=10)
        self.left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.right_frame = ttk.Frame(root, padding=10)
        self.right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # Create a label to display the video in the left frame
        self.video_label = ttk.Label(self.left_frame)
        self.video_label.pack()

        # Open a video file or use a camera stream
        self.cap = cv2.VideoCapture('path_to_your_video.mp4')  # Replace 'path_to_your_video.mp4' with the actual path

        # Get the initial frame for setting up the label
        ret, frame = self.cap.read()
        if ret:
            self.show_frame(frame)

        # Create a button to start object detection (you can replace this with your detection logic)
        self.start_button = ttk.Button(self.right_frame, text="Start Object Detection", command=self.start_detection)
        self.start_button.pack()

        # Configure row and column weights for resizing
        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=1)
        root.rowconfigure(0, weight=1)

    def show_frame(self, frame):
        # Convert the OpenCV BGR image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Convert the image to PhotoImage format
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)

        # Update the label with the new image
        self.video_label.config(image=image)
        self.video_label.image = image  # Keep a reference to prevent garbage collection

    def start_detection(self):
        # Implement your object detection logic here
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            # Perform object detection on the frame (replace this with your detection code)
            # For example, you can use a pre-trained model or your custom detection code
            # detected_frame = perform_object_detection(frame)

            # Show the frame with detections in the left frame
            self.show_frame(frame)

            # You may need to add a delay to control the frame rate
            # You can also use a separate thread for video processing to avoid GUI freezing

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoApp(root)
    root.mainloop()
