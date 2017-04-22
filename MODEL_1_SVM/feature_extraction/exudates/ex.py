import numpy as np
import cv2
import scipy.misc
import glob
import os
import operator


name = ''
counter = 1;
founter = 501;
no_of_images = 0


#def get_structure_index(subimage):



def remove_optical_disk(image,counter):	
	coloumn = 0
	time = 0
	row = 0	
	get_coloumn = 0
	get_row = 0
	gotit = 1
	mean_intensity_of_image = np.mean(image)	
	size_array = image.shape
	no_of_rows = size_array[0]
	no_of_coloumns = size_array[1]	
	mask_statistic_list = []
	mean_table = []	
	index_table_row = []
	index_table_coloumn = []
	regions_with_greater_intensity = []
	while row < no_of_rows:
		while coloumn < no_of_coloumns:			
			subarray = image[row:row+159,coloumn:coloumn+119]			
			mean_table.append(np.mean(subarray))			
			index_table_row.append(row)
			index_table_coloumn.append(coloumn)					
			coloumn = coloumn+30			
		coloumn = 0
		row = row+40	
	sorted_table = sorted(mean_table,reverse = True)	
	print(sorted_table[0:10])
	index = 0
	newindex = 0
	while gotit == 1 :	
		newindex = mean_table.index(sorted_table[index])
		print(mean_table[newindex])
		get_row = index_table_row[newindex]
		print(get_row)
		get_coloumn = index_table_coloumn[newindex]
		if get_row > 190 and get_row < 420 :
			print("selected")
			gotit = 0		
		else :
			index = index + 1
			
		
	image[get_row:get_row+159,get_coloumn:get_coloumn+119]	= mean_intensity_of_image
	#blur = cv2.GaussianBlur(image,(5,5),0)	
	#im_at_mean = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 0)
	name2 = str(counter) + '.jpg'
	scipy.misc.imsave(name2,image)	
	return ;


images = [cv2.imread(file) for file in glob.glob('/home/sherlock/DR/MODEL_1_SVM/data/*png')]
print(len(images))

while no_of_images < 130:

	fundus = images[no_of_images]	
	dim = (800,600)
	I1 = cv2.resize(fundus, dim, interpolation = cv2.INTER_AREA)	
	b,green_fundus,r = cv2.split(I1)		
	kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(25,25))
	th_fundus = cv2.morphologyEx(green_fundus, cv2.MORPH_TOPHAT, kernel)
	mf_fundus = cv2.medianBlur(th_fundus,3)
	name = str(founter) + '.jpg'
	scipy.misc.imsave(name,mf_fundus)
	remove_optical_disk(mf_fundus,counter)

	# xmask = np.ones(fundus.shape[:2], dtype="uint8") * 255
	# x1, xcontours, xhierarchy = cv2.findContours(mf_fundus.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)	
	# for cnt in xcontours:		
	# 	peri = cv2.arcLength(cnt, True)		   			
	# 	if cv2.contourArea(cnt) >= 200:
	# 		shape = "circle"	
	# 	else:
	# 		shape = "veins"
	# 	if(shape=="circle"):
	# 		cv2.drawContours(xmask, [cnt], -1, 0, -1)	
	# circles = cv2.HoughCircles(inv_fundus,cv2.HOUGH_GRADIENT,1,20,
    # param1=100,param2=30,minRadius=0,maxRadius=0)	
	# if circles is not None:
	# 	circles = np.round(circles[0, :]).astype("int")	

	# for (x, y, r) in circles:
	# 	cv2.circle(inv_fundus, (x, y), r, (0, 255, 0), 2)			
	#cv2.imshow("output", np.hstack([gc, output]))	
	
	
	counter = counter + 1
	founter = founter + 1
	no_of_images = no_of_images+ 1
	print()
	print("NEXT IMAGE : ", no_of_images)


print("fcuk")
cv2.waitKey(0)