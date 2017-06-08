import pandas as pd
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Reading csv file and considering only 2 features
fp = open('dataset.csv','r')
petal_length = [] 
petal_width = []
#petal_class = []
line = fp.readline()

while len(line) != 0:    
    data = line.split(',')
    petal_length.append(data[2])
    petal_width.append(data[3])
    #petal_class.append(data[4])
    line = fp.readline()
   
fp.close()

# Plotting and Saving the plot without the Axis
plt.scatter(petal_length, petal_width)
plt.axis('off')
plt.savefig('visual.jpg')

#Reading the Image using opencv
img_1 = cv2.imread('visual.jpg',1)
img = cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY)

# Making the kernal
kernal = np.ones((25,25), np.float32)/625

# Blurring the points
smoothed = cv2.filter2D(img,-1,kernal)

# Applying Threshold
ret, img_threshold = cv2.threshold(smoothed, 220, 255, cv2.THRESH_BINARY_INV)

# Displaying Smoothed and image treated with threshold
#--cv2.imshow('thresh',img_threshold)
#--cv2.imshow('smoothed',smoothed)


contours,hierarchy = cv2.findContours(img_threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]
#--cv2.drawContours(img_threshold, contours, -1, (255,0,0), 3)
#--cv2.imshow('contour',img_threshold)


area_threshold = cv2.contourArea(cnt) / 2

for i, c in enumerate(contours):
        area = cv2.contourArea(c)
        # area can be configured
        if area > area_threshold:
            print i
            cv2.drawContours(img_threshold, contours, i, (255, 0, 0), -1)

cv2.imshow('threhsold',img_threshold)

#--(x,y),radius = cv2.minEnclosingCircle(cnt)
#--center = (int(x),int(y))
#--radius = int(radius)
#--cv2.circle(img_1,center,radius,(0,0,255),3)
#--cv2.imshow('image',img_1)


cv2.waitKey(0)
cv2.destroyAllWindows()



