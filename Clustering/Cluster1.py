import pandas as pd
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Reading csv file and considering only 2 features
fp = open('dataset.csv','r')
petal_length = [] 
petal_width = []
petal_class = []
line = fp.readline()

while len(line) != 0:    
    data = line.split(',')
    petal_length.append(data[2])
    petal_width.append(data[3])
    petal_class.append(data[4])
    line = fp.readline()
   
fp.close()

# Plotting and Saving the plot without the Axis
plt.scatter(petal_length, petal_width)
plt.axis('off')
plt.savefig('visual.jpg')

#Reading the Image using opencv
img = cv2.imread('visual.jpg',1)

# Making the kernal
kernal = np.ones((15,15), np.float32)/225

# Blurring the points
smoothed = cv2.filter2D(img,-1,kernal)
cv2.imshow('smoothed',smoothed)

cv2.waitKey(0)
cv2.destroyAllWindows()



