import numpy as np
import cv2
import scipy.misc

images = ['1.png', '2.png',  '3.png','4.png','5.png','6.png','7.png','8.png','9.png','10.png']
name = ''
counter = 11;
for image in images:
	fundus = cv2.imread(image)
	dim = (800,700)
	fundus = cv2.resize(fundus, dim, interpolation = cv2.INTER_AREA)
	cv2.imshow("Fundus Image",fundus)
	b,green_fundus,r = cv2.split(fundus)
	sigma = 0.33

	#print(green_fundus)
	inverted_green_fundus = 255 - green_fundus
	#cv2.imshow("green",green_fundus)
	#cv2.imshow("inverted green",inverted_green_fundus)
	#edge_fundus_green = cv2.Canny(green_fundus, 10, 100)
	#cv2.imshow("edge green",edge_fundus_green)
	gray_fundus = cv2.cvtColor(fundus, cv2.COLOR_BGR2GRAY)
	impo = cv2.Canny(gray_fundus, 5, 50)
	cv2.imshow("IMPORTANt",impo)
	#cv2.imshow("gray_fundus",gray_fundus)
	#cv2.imshow("green_fundus",green_fundus)
	clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
	contrast_enhanced_green_fundus = clahe.apply(green_fundus)
	contrast_enhanced_inverted_green_fundus = clahe.apply(inverted_green_fundus)
	#cv2.imshow("contrast enhanced",contrast_enhanced_green_fundus)
	structuring_element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
	fundus_dilated = cv2.dilate(contrast_enhanced_green_fundus, structuring_element, iterations=1)
	#cv2.imshow("dilate fundus",fundus_dilated)
	fundus_eroded = cv2.erode(fundus_dilated, structuring_element, iterations=1)
	cv2.imshow("eroded fundus",fundus_eroded)
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

	blood_vessels = cv2.addWeighted(edge_fundus2,0.6,contrast_enhanced_inverted_green_fundus,0.4,0)
	#dst = cv2.addWeighted(img1,0.7,img2,0.3,0)

	#cv2.imshow("blood vessels", blood_vessels)
	#binary_blood_vessel1 = cv2.adaptiveThreshold(non_smooth_fundus,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,21,2)
	binary_blood_vessel2 = cv2.adaptiveThreshold(smooth_fundus,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,21,2)
	im2, contours, hierarchy = cv2.findContours(binary_blood_vessel2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	cv2.imshow("most imp",binary_blood_vessel2)
	#cv2.imshow("blood vessels adaptive smooth", binary_blood_vessel2)
	name = str(counter) + '.jpg'
	scipy.misc.imsave(name, binary_blood_vessel2)
	counter = counter +1;
print("fcuk")
cv2.waitKey(0)