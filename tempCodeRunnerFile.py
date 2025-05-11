# import cv2
# import torch
# print("Open CV: ",cv2.__version__)
# print("PyTorch: ",torch.__version__)
from ultralytics import YOLO  

# Initialize the model
model = YOLO("yolov8n.pt")  

# Train the model
model.train(data="F:/The Ultimate project/datasets/car_dataset.yaml", epochs=50)




