import cv2
import numpy as np

img = cv2.imread("C:/Users/DELL/OneDrive/Pictures/Screenshots/Screenshot 2024-12-17 214458.png", 0)
kernel = np.ones((5,5), np.uint8)

dilation = cv2.dilate(img, kernel, iterations=1)
erosion = cv2.erode(img, kernel, iterations=1)

cv2.imshow('Dilated Image', dilation)
cv2.imshow('Eroded Image', erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()