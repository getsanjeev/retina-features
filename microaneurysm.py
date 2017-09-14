from SimpleCV import Image, Color
import csv

def findMA(path, file_name_without_extension):
    eye = Image(path)

    (empty, eye_green, emptier) = eye.splitChannels(False)

    eye_green = eye_green * 2.5
    eye_gray = eye_green.grayscale()

    eye_gray = eye_gray.smooth()


    #Canny edge detection algorithm. t1 specifies the threshold value to begin an edge. t2 specifies the strength required
    #build an edge off of a point found by T2.
    eye_edges = eye_gray.edges(t1 = 70, t2=35)


    edge_test = eye_gray + eye_edges


    eye_final = eye_edges

    #Perform closing to find individual objects
    eye_final = eye_final.dilate(2)
    eye_final = eye_final.erode()

    eye_final = eye_final.dilate(4)
    eye_final = eye_final.erode(3)

    big_blobs = eye_final.findBlobs(minsize=500)

     #create a blank image to mask
    masked_image = Image(eye.size())

    for b in big_blobs:

         #set mask
       b.image = masked_image

         #draw the blob on your mask
       b.draw(color = Color.WHITE)



    eye_final = eye_final - masked_image.applyLayers()
    eye_final = eye_final.erode()
    eye_final = eye_final.grayscale()
    print(eye_final[100,200][0])
    print(eye_final[200,300])
    print(eye_final[400,600])
    #eye_final.save("testthis.png")


    if eye_final.findBlobs(maxsize=10):

        small_blobs = eye_final.findBlobs(maxsize=10)

        #create a blank image to mask
        masked_small_image = Image(eye.size())
        for b in small_blobs:

            #set mask
           b.image = masked_small_image

           #draw the blob on your mask
           b.draw(color = Color.WHITE)


        eye_final = eye_final - masked_small_image.applyLayers()
        # print("secondtime")
        print(eye_final[100,200])
        print(eye_final[200,300])
        print(eye_final[400,600])


    if eye_final.findBlobs():
        final_blobs = eye_final.findBlobs()

        #Filter through objects to find only potential microaneurysms
        masked_circle_image = Image(eye.size())
        for b in final_blobs:
            blob_height = b.height()
            blob_width = b.width()
            width_height_diff = abs(blob_height-blob_width)
            if (width_height_diff > .2 * blob_height) | (width_height_diff > .2 *blob_width):
                    b.image = masked_circle_image
                    b.draw(color = Color.WHITE)


            if (b.area() < .45 *blob_height * blob_width):

                    b.image = masked_circle_image
                    b.draw(color = Color.WHITE)

            #remove large pointless blobs
            if (b.area() > 1500):
                    b.image = masked_circle_image
                    b.draw(color=Color.WHITE)


        #Save different objects
        #eye_final.save("Output1.png")
        #masked_circle_image.applyLayers().save("Output2.png")

        eye_final = eye_final - masked_circle_image.applyLayers()
    eye_example = eye_final + eye

    # print("third time")
    print(eye_final[100,200])
    print(eye_final[200,300])
    print(eye_final[400,600])

    eye_example.save(file_name_without_extension+'_MAoverlay.tif')
    print("overlay saved")
    eye_final.save(file_name_without_extension+'_MA.tif')
    print("MA saved")
    # print("fourth time")
    print(eye_final[140,140])
    print(eye_final[180,180])
    print(eye_final[350,350])
    # print('lag gye')
    return eye_final


pathFolder = "/home/utkarsh/SimpleCV/input"
filesArray = [x for x in os.listdir(pathFolder) if os.path.isfile(os.path.join(pathFolder,x))]
# MA_Folder = pathFolder+"/MA/"

# if not os.path.exists(MA_Folder):
#     os.mkdir(MA_Folder)


with open('ma.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['microaneurysmcount', 'countvalue'])
    for file_name in filesArray:
        print(pathFolder+'/'+file_name)
        print(os.path.splitext(file_name)[0])        
        final_madetected = findMA(pathFolder+'/'+file_name,os.path.splitext(file_name)[0])

        i = 0
        j = 0
        white = 0
        black = 0

        # while i < final_madetected.size()[0]:
        #     j = 0
        #     while j < final_madetected.size()[1]:                
        #         if final_madetected[i,j] == 255:
        #             white = white + 1
        #         j = j+1
        #     i = i+1
        # print('lag gye dobara')
        print(final_madetected.size())


        while i < final_madetected.size()[0]:
            j=0
            while j < final_madetected.size()[1]:
                
                if final_madetected[i,j][0] != 0:
                    white=white + 1
                    #print(final_madetected[i,j][k],i,j,k)
                else:
                    black=black+1
                    
                j=j+1
            i=i+1

        print(white)
        #print(black)
        final_white_pixels=white/3


        filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow([os.path.splitext(file_name)[0]+"_microaneurysm.jpg",white])
       # cv2.imwrite(os.path.splitext(file_name)[0]+"_microaneurysm.jpg",bloodvessel)    

        # file_name_no_extension = os.path.splitext(file_name)[0]
        # counter = maskWhiteCounter(exudate_image)
        # array_exudate_pixels.append(counter)
        # cv2.imwrite(exudateFolder+file_name_no_extension+"_exudates.jpg",exudate_image)
