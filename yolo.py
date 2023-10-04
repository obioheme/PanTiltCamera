from ultralytics import YOLO
model = YOLO("yolov8.pt")
model.predict(source=0, show=True)