import numpy as np
import cv2
import scipy.misc

def remove_white_spots(image,founter):	
	clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
	my_image = clahe.apply(image)
	ret,image2 = cv2.threshold(my_image,15,255,cv2.THRESH_BINARY)
	cv2.imshow("bhehe",image2)
	dim = (800,700)
	fundus = cv2.resize(image2, dim, interpolation = cv2.INTER_AREA)
	xcount = founter;
	xname = str(founter) + '.jpg'
	xmask = np.ones(fundus.shape[:2], dtype="uint8") * 255
	x1, xcontours, xhierarchy = cv2.findContours(fundus,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)	
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

images = ['11.jpg', '12.jpg',  '13.jpg','14.jpg','15.jpg','16.jpg','17.jpg','18.jpg','19.jpg','20.jpg']
name = ''
founter = 11;
for image in images:
	fundus = cv2.imread(image)	
	clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
	my_image = clahe.apply(fundus)
	ret,image2 = cv2.threshold(my_image,15,255,cv2.THRESH_BINARY)
	cv2.imshow("bhehe",image2)
	dim = (800,700)
	fundus = cv2.resize(image2, dim, interpolation = cv2.INTER_AREA)
	xcount = founter;
	xname = str(founter) + '.jpg'
	xmask = np.ones(fundus.shape[:2], dtype="uint8") * 255
	x1, xcontours, xhierarchy = cv2.findContours(fundus,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)	
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
#	remove_white_spots(image1,founter)
	founter = founter +1;
print("fcuk2")
cv2.waitKey(0)


