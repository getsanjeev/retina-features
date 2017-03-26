import numpy as np
import cv2

channel = list()
image = cv2.imread("fundus.png")
#cv2.imshow("Fundus Image",image)
b,green_fundus,r = cv2.split(image)
sigma = 0.33

#print(green_fundus)
inverted_green_fundus = 255 - green_fundus
cv2.imshow("green",green_fundus)
cv2.imshow("inverted green",inverted_green_fundus)
#edge_fundus_green = cv2.Canny(green_fundus, 10, 100)
#cv2.imshow("edge green",edge_fundus_green)
gray_fundus = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow("gray_fundus",gray_fundus)
#cv2.imshow("green_fundus",green_fundus)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
contrast_enhanced_green_fundus = clahe.apply(green_fundus)
cv2.imshow("contrast enhanced",contrast_enhanced_green_fundus)
structuring_element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
fundus_dilated = cv2.dilate(contrast_enhanced_green_fundus, structuring_element, iterations=1)
#cv2.imshow("dilate fundus",fundus_dilated)
fundus_eroded = cv2.erode(fundus_dilated, structuring_element, iterations=1)
#cv2.imshow("eroded fundus",fundus_eroded)
non_smooth_fundus = fundus_eroded;
smooth_fundus = cv2.bilateralFilter(fundus_eroded,9,75,75)
#cv2.imshow("smooth fundus",fundus_eroded)

#v1 = np.median(non_smooth_fundus)
#v2 = np.median(smooth_fundus)
#lower1 = int(max(0, (1.0 - sigma) * v1))
#upper1 = int(min(255, (1.0 + sigma) * v1))
#lower2 = int(max(0, (1.0 - sigma) * v2))
#upper2 = int(min(255, (1.0 + sigma) * v2))
edge_fundus = cv2.Canny(non_smooth_fundus, 5, 50)
edge_fundus2 = cv2.Canny(smooth_fundus, 5, 50)
cv2.imshow("edge smooth fundus",edge_fundus2)
cv2.imshow("edge nonsmooth fundus",edge_fundus)
cv2.waitKey(0)