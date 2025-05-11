from ultralytics import yolo
import cv2

#Loading the Yolo version 8 model
model = yolo('yolov8n.pt')
#also using the nano version of the model for faster proceesing

#Initialising the camera for capturing the video
#Using the (0) for the default camera
cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    #Detecting the objects in the frame
    if not ret:
        break
    results = model(frame)

    #visualizing the frames
    annotated_frame = results[0].plot()
    cv2.imshow('Car Detection', annotated_frame)

    #Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#Releasing the camera and closing the window
cap.release()
cv2.destroyAllWindows()