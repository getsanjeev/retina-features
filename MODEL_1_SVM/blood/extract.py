import numpy as np
import cv2
import scipy.misc

def remove_white_spots(image,founter):	
	xcount = founter;		
	xname = str(founter) + '.jpg'
	xmask = np.ones(f5.shape[:2], dtype="uint8") * 255
	x1, xcontours, xhierarchy = cv2.findContours(image,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)	
	for cnt in xcontours:
		shape = "unidentified"
		peri = cv2.arcLength(cnt, True)
		approx = cv2.approxPolyDP(cnt, 0.04 * peri, True)   				
		if len(approx) >7:
			shape = "triangle"	
		else:		
			shape = "circle"
		if(shape=="circle"):
			cv2.drawContours(xmask, [cnt], -1, 0, -1)
	scipy.misc.imsave(xname,xmask)
	return;

images = ['1.png', '2.png',  '3.png','4.png','5.png','6.png','7.png','8.png','9.png','10.png']
name = ''
counter = 1;
founter = 11;

for image in images:
	fundus = cv2.imread(image)	
	dim = (800,700)
	fundus = cv2.resize(fundus, dim, interpolation = cv2.INTER_AREA)
	b,green_fundus,r = cv2.split(fundus)
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

	ret,f6 = cv2.threshold(f5,15,255,cv2.THRESH_BINARY)
	mask = np.ones(f5.shape[:2], dtype="uint8") * 255
	im2, contours, hierarchy = cv2.findContours(f6,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
	for cnt in contours:
		if cv2.contourArea(cnt) <= 200:
			cv2.drawContours(mask, [cnt], -1, 0, -1)
			cv2.imshow("mask",mask)
	im = cv2.bitwise_and(f5, f5, mask=mask)
	ret,fin = cv2.threshold(im,15,255,cv2.THRESH_BINARY_INV)	
	fundus_eroded = cv2.erode(fin, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3)), iterations=1)
	#remove_white_spots(fundus_eroded,founter)


	xmask = np.ones(fundus.shape[:2], dtype="uint8") * 255
	x1, xcontours, xhierarchy = cv2.findContours(fin,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)	
	for cnt in xcontours:
		shape = "unidentified"
		peri = cv2.arcLength(cnt, True)
		approx = cv2.approxPolyDP(cnt, 0.04 * peri, False)   				
		if len(approx) > 5 and cv2.contourArea(cnt) <= 2000 and cv2.contourArea(cnt) >= 200:
			shape = "circle"	
		else:
			shape = "veins"
		if(shape=="circle"):
			cv2.drawContours(xmask, [cnt], -1, 0, -1)
			
	#im_fin = cv2.bitwise_and(fundus_eroded, fundus_eroded, mask=xmask)

	name = str(counter) + '.jpg'
	name2 = str(founter) + '.jpg'
	scipy.misc.imsave(name,xmask)
	scipy.misc.imsave(name2,fundus_eroded)
	counter = counter +1;
	founter = founter +1;

print("fcuk")
cv2.waitKey(0)

