import numpy as np
import cv2

image = cv2.imread("fundus.png")
gray_fundus = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray_fundus)
g_kernel = cv2.getGaborKernel((51,51), 1.0, 150,20.0, 0.5, 0, ktype=cv2.CV_32F)
filtered_img1 = cv2.filter2D(gray_fundus, cv2.CV_8UC3, g_kernel)
cv2.imshow("blood vessels", filtered_img1)
cv2.waitKey(0)
