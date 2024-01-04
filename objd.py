import cv2
import numpy as np
from picamera.array import PiRGBArray
from picamera import PiCamera
import time

# Load the pre-trained MobileNet SSD model and its configuration
net = cv2.dnn.readNet('MobileNetSSD_deploy.caffemodel', 'MobileNetSSD_deploy.prototxt')

# Set the list of classes that the model can detect
classes = ["background", "aeroplane", "bicycle", "bird", "boat",
               "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
               "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
               "sofa", "train", "tvmonitor"]

# Initialize the PiCamera
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

# Allow the camera to warm up
time.sleep(0.1)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # Extract the NumPy array from the frame
    image = frame.array

    # Resize the frame to have a maximum width of 500 pixels (for faster processing)
    image = cv2.resize(image, (500, 375))

    # Extract the height and width of the frame
    (h, w) = image.shape[:2]

    # Preprocess the image for object detection
    blob = cv2.dnn.blobFromImage(image, 0.007843, (300, 300), 127.5)

    # Pass the blob through the network and obtain the detections
    net.setInput(blob)
    detections = net.forward()

    # Loop over the detections
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        # Filter out weak detections by confidence
        if confidence > 0.2:
            class_id = int(detections[0, 0, i, 1])
            label = f"{classes[class_id]}: {confidence:.2f}%"

            # Draw the bounding box and label on the frame
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
            cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)
            y = startY - 15 if startY - 15 > 15 else startY + 15
            cv2.putText(image, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the frame
    cv2.imshow("Object Detection", image)

    # Clear the stream for the next frame
    rawCapture.truncate(0)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cv2.destroyAllWindows()
