import torch
from pathlib import Path
from PIL import Image
import requests
from io import BytesIO

# Load the YOLOv8-tiny model
model = torch.hub.load('ultralytics/yolov5:v6.0', 'yolov5s', pretrained=True)

# Download a sample image for testing
img_url = "https://ultralytics.com/images/zidane.jpg"
response = requests.get(img_url)
img = Image.open(BytesIO(response.content))

# Perform inference
results = model(img)

# Display results
results.show()

# Save results (optional)
results.save(Path("output"))
