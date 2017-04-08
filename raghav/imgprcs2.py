# Import the necessary packages
import numpy as np
import cv2

print "Input: Image 1."
s = '1_resized.png'
t = "1_grayscale.png"
abc = "1_clahe.png"

# Load the image
img_original = cv2.imread(s)
gray_image = cv2.cvtColor(img_original, cv2.COLOR_RGB2GRAY)

b,g,r = cv2.split(img_original)
img_step2 = cv2.subtract(255,g) 
k = '1_resized.png'
srs = cv2.imread(k,0)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(5,5))
img_cl = clahe.apply(srs)

img_step4 = cv2.erode(img_cl, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(6,6)),iterations = 2)

img_step5 = cv2.subtract(img_cl ,img_step4)

ret,th3 = cv2.threshold(img_step5,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow(th3)
cv2.waitKey(0)

cv2.imshow("dasd",gray_image)
cv2.imwrite(t,gray_image)
m = cv2.imread(t,0)
#Adaptive Histogram equalization
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(5,5))
img_clahe = clahe.apply(m)
# cv2.imshow('CLAHE output', img_clahe)
# #cv2.imwrite(abc,img_clahe)
opening = cv2.morphologyEx(img_clahe, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(6,6)))
# cv2.imshow("asd",opening)
# cv2.waitKey(0)

# #img_step4 = cv2.morphologyEx(abc, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5)), iterations = 1)
edges = cv2.Canny(img_clahe,50,100)
cv2.imshow("Asanf",edges)
cv2.waitKey(0)


final = cv2.subtract(edges,opening)
cv2.imshow("Hey Hey",final)
cv2.waitKey(0)

