import cv2
import numpy as np




# Import the image
img = cv2.imread('img.jpg',)
size = img.shape 
print(size)





#gray
gray=np.array(img)


gray=gray[:,:,0]
img_gray=np.array([gray,gray,gray])
img_gray=np.transpose(img_gray,(1,2,0))#矩阵维度交换
cv2.imwrite('img_gray.jpg',img_gray,[int(cv2.IMWRITE_JPEG_QUALITY),100])

# split
ret, img_split = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
cv2.imwrite('img_split.jpg',img_split,[int(cv2.IMWRITE_JPEG_QUALITY),100])

#gray2
img_gray_COLOR_BGR2GRAY = cv2.cvtColor(img_gray, cv2.COLOR_BGR2GRAY)
cv2.imwrite('img_gray_COLOR_BGR2GRAY.jpg',img_gray_COLOR_BGR2GRAY,[int(cv2.IMWRITE_JPEG_QUALITY),100])

#adaptiveThreshold
img_split_auto = cv2.adaptiveThreshold(img_gray_COLOR_BGR2GRAY,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)

cv2.imwrite('img_split_auto.jpg',img_split_auto,[int(cv2.IMWRITE_JPEG_QUALITY),100])



# erosion 
'''
kernel = np.ones((4,4),np.uint8)
erosion = cv2.erode(img_split_auto,kernel,iterations = 1)
cv2.imwrite('erosion.jpg',erosion,[int(cv2.IMWRITE_JPEG_QUALITY),100])
'''

 

#kernel = np.ones((2,2),np.uint8)
kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(2,2))
dilation = cv2.dilate(img_split_auto,kernel,iterations = 1)
cv2.imwrite('dilation.jpg',dilation,[int(cv2.IMWRITE_JPEG_QUALITY),100])

'''

kernel = np.ones((5,5),np.uint8)
opening  = cv2.morphologyEx(img_split_auto, cv2.MORPH_OPEN, kernel)
cv2.imwrite('opening.jpg',opening ,[int(cv2.IMWRITE_JPEG_QUALITY),100])



kernel = np.ones((2,2),np.uint8)
closing   = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel)
cv2.imwrite('closing.jpg',closing ,[int(cv2.IMWRITE_JPEG_QUALITY),100])
'''

# gradient
#kernel = np.ones((2,2),np.uint8)
kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
gradient = cv2.morphologyEx(dilation, cv2.MORPH_GRADIENT, kernel)
cv2.imwrite('gradient.jpg',gradient,[int(cv2.IMWRITE_JPEG_QUALITY),100])

'''
# tophat
kernel = np.ones((2,2),np.uint8)
tophat = cv2.morphologyEx(img_split_auto, cv2.MORPH_TOPHAT, kernel)
cv2.imwrite('tophat.jpg',tophat,[int(cv2.IMWRITE_JPEG_QUALITY),100])


# tophat
kernel = np.ones((2,2),np.uint8)
blackhat = cv2.morphologyEx(img_split_auto, cv2.MORPH_BLACKHAT, kernel)
cv2.imwrite('blackhat.jpg',blackhat,[int(cv2.IMWRITE_JPEG_QUALITY),100])
'''


#cv2.imshow("Image2",gradient ) 

contours, hierarchy = cv2.findContours(gradient,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)  


newimg = np.zeros(size, np.uint8)   
#fill the image with white
newimg.fill(255)

l = len(contours)
while l>=1:
	area=cv2.contourArea(contours[l-1],True)
	if area > 200 :		
		print('contours=',l-1,' area=',area)
		cv2.drawContours(newimg,contours,l-1,(123,123,255),1) 

	l=l-1
cv2.imshow("Image3",newimg)  
cv2.waitKey(0)
#cv2.imshow("Image1",img_split_auto ) 



