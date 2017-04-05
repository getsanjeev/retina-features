# Import the necessary packages
import numpy as np
import cv2

for x in xrange(1,11):
	print "Input: Image %s ."%(x)
	
	s = '%s.png'%(x)
	ss = '%s_resized.png'%(x)
	t = "%s_grayscale.png"%(x)
	abc = "%s_clahe.png"%(x)
	
	# Load the image
	img_original = cv2.imread(s)

	# Extract the green filter
	resized_image = cv2.resize(img_original, (576, 720)) 
	#cv2.imshow("Original",resized_image)
	a = '%s_resized.png'%(x)
	cv2.imwrite(a,resized_image)
	b,g,r = cv2.split(resized_image)
	#cv2.imshow("Green Channel",g)

	# Intensity Reverse
	img_step2 = cv2.subtract(255,g) 
	k = '%s_resized.png'%(x)
	srs = cv2.imread(k,0)

	#GreyScale
	img_original = cv2.imread(ss)
	gray_image = cv2.cvtColor(img_original, cv2.COLOR_RGB2GRAY)
	cv2.imwrite(t,gray_image)
	m = cv2.imread(t,0)

	# Adaptive Histogram equalization(For Veins)
	clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(5,5))
	img_step3 = clahe.apply(srs)
	#cv2.imshow('CLAHE output', img_step3)
	# Morphological Opening
	#img_step4 = cv2.morphologyEx(img_step3, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5)), iterations = 2)
	img_step4 = cv2.erode(img_step3, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5)),iterations = 3)
	#cv2.imshow('Morph Opening',img_step4)s
	
	# Adaptive Histogram equalization
	clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(5,5))
	img_clahe = clahe.apply(m)

	# Subtract Adaptive Histogram Equalization - Morphological Opening
	img_step5 = cv2.subtract(img_step3 ,img_step4)

	#Opening for Mneurism
	opening = cv2.morphologyEx(img_clahe, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5)), iterations = 2)
	
	#Canny for Mneurism
	edges = cv2.Canny(img_clahe,0,50)

	#Subtraction canny - clahe
	cancla = cv2.subtract(edges,img_clahe)
	# ret,th4 = cv2.threshold(cancla,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	# cv2.imshow("haha",th4)
	# cv2.waitKey(0)

	#Binarization
	ret,th3 = cv2.threshold(img_step5,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	#th3 = cv2.adaptiveThreshold(img_step5,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,25,2)
	cv2.imshow("Binary",th3)
	#th3 = cv2.subtract(255,th3)
	b = '%s_binary.png'%(x)
	cancla = cv2.subtract(cancla,th3)
	cv2.imshow("haha",cancla)
	cv2.waitKey(0)
	cv2.imwrite(b,th3)

	print "Image %s Processed."%(x)