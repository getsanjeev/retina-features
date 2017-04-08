import numpy as np
import cv2
import scipy.misc

images = ['1.jpeg', '2.jpeg',  '3.jpeg','4.jpeg','5.jpeg','6.jpeg','7.jpeg','8.jpeg','9.jpeg','10.jpeg']
name = ''
counter = 1;
founter = 11;
for image in images:
	fundus = cv2.imread(image)	
	dim = (800,700)
	fundus = cv2.resize(fundus, dim, interpolation = cv2.INTER_AREA)
	b,green_fundus,r = cv2.split(fundus)
	#yname = str(founter) + '.jpg'
	#scipy.misc.imsave(yname,green_fundus)
	clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
	contrast_enhanced_green_fundus = clahe.apply(green_fundus)
	r1 = cv2.morphologyEx(contrast_enhanced_green_fundus, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5)), iterations = 1)
	R1 = cv2.morphologyEx(r1, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5)), iterations = 1)
	r2 = cv2.morphologyEx(R1, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(11,11)), iterations = 1)
	R2 = cv2.morphologyEx(r2, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(11,11)), iterations = 1)
	r3 = cv2.morphologyEx(R2, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(23,23)), iterations = 1)
	R3 = cv2.morphologyEx(r3, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(23,23)), iterations = 1)	
	f4 = cv2.subtract(R3,contrast_enhanced_green_fundus)
	f5 = clahe.apply(f4)
	median = cv2.medianBlur(f5,5)
	#smooth_fundus = cv2.bilateralFilter(f5,9,75,75)
	#binary_blood_vessel = cv2.adaptiveThreshold(smooth_fundus,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,20)
	ret,thresh2 = cv2.threshold(median,5,255,cv2.THRESH_BINARY_INV)
	r1 = cv2.morphologyEx(thresh2, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5)), iterations = 1)
	R1 = cv2.morphologyEx(r1, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5)), iterations = 1)
	r2 = cv2.morphologyEx(R1, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(11,11)), iterations = 1)
	R2 = cv2.morphologyEx(r2, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(11,11)), iterations = 1)	
	f4 = cv2.subtract(R3,f5)
	f5 = clahe.apply(f4)
	ret,thresh2 = cv2.threshold(median,5,255,cv2.THRESH_BINARY_INV)
	name = str(counter) + '.jpg'
	scipy.misc.imsave(name,thresh2)
	counter = counter +1;
	founter = founter +1;
print("fcuk")
cv2.waitKey(0)
