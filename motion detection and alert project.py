import cv2
import numpy as np
import pygame

cam = cv2.VideoCapture(0)
pygame.mixer.init()

ret,first_frame = cam.read()
first_frame = cv2.cvtColor(first_frame,cv2.COLOR_BGR2GRAY)
first_frame = cv2.GaussianBlur(first_frame, (21,21),0)

while True:
    ret, frame = cam.read()
    if not ret:
        break

    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.GaussianBlur(gray_frame,(21,21),0)

    delta_frame = cv2.absdiff(first_frame,(21,21),0)

    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]

    

    white_pixel_count =np.sum(thresh_frame == 255)

    if white_pixel_count > 1000:
        pygame.mixer.Sound('alert.wav').play()

    cv2.imshow('Moition Detection', frame)
    
    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()
