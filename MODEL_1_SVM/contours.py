import numpy as np
import cv2
 
im = cv2.imread('1.jpg')
# cv2.imshow("img", im)
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
# cv2.imshow("imgray", imgray)
ret,thresh = cv2.threshold(imgray,127,255,cv2.THRESH_BINARY)
cv2.imshow("thresh", thresh)

im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# cv2.imshow("im2", im2)
mask = np.ones(im.shape[:2], dtype="uint8") * 255
#cv2.drawContours(im, contours, -1, (0,255,0))
#cv2.imshow("contours", im)

for cnt in contours:
	if cv2.contourArea(cnt) <= 200:
		cv2.drawContours(mask, [cnt], -1, 0, -1)

im_invert = cv2.bitwise_not(im)

im_invert = cv2.bitwise_and(im_invert, im_invert, mask=mask)
cv2.imshow("Mask", mask)
cv2.imshow("After", cv2.bitwise_not(im_invert))
cv2.waitKey(0)