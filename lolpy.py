import cv2
cap = cv2.VideoCapture('http://192.168.0.50:8080/?action=stream')

while True:
  ret, frame = cap.read()
  cv2.imshow('Video', frame)

  if cv2.waitKey(1) == 27:
    exit(0)