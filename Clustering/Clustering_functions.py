import cv2
import matplotlib.pyplot as plt
import numpy as np
#Reading the Image using opencv
img_1 = cv2.imread('visual.jpg',1)
img = cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY)
#cv2.imshow('gray',img)

# Making the kernal
kernal = np.ones((11,11), np.float32)/121

# Blurring the points
smoothed = cv2.filter2D(img,-1,kernal)
#cv2.imshow('smooth',smoothed)


#cv2.imshow('gaussian',blur)
# Applying Threshold
ret, img_threshold = cv2.threshold(smoothed, 240, 255, cv2.THRESH_BINARY_INV)



# Displaying Smoothed and image treated with threshold
#cv2.imshow('threhsold',img_threshold)


kernal_dilate = np.ones((2,2), np.uint8)
kernal_opening = np.ones((10,10), np.uint8)

#dilate = cv2.dilate(img_threshold, kernal_dilate, iterations = 1)
#cv2.imshow('dilate', dilate)

#opening = cv2.morphologyEx(dilate, cv2.MORPH_OPEN, kernal_opening)
#cv2.imshow('closing',opening)



contours,hierarchy = cv2.findContours(img_threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]

mean_area = 0
count = 0
for i, c in enumerate(contours):
	mean_area += cv2.contourArea(c)
	count += 1
mean_area /= count


Clusters = 0
for i, c in enumerate(contours):
        area = cv2.contourArea(c)
        # area can be configured
        if area > mean_area *.1:
            Clusters += 1
            cv2.drawContours(img_threshold, contours, i, (255, 0, 0), -1)

cv2.imshow('threhsold',img_threshold)
print "Clusters = "+str(Clusters)

dilate = cv2.dilate(img_threshold, kernal_dilate, iterations = 1)
cv2.imshow('dilate', dilate)

cv2.waitKey(0)
cv2.destroyAllWindows()

