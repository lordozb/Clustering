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

mean_area = 0
count = 0
for i, c in enumerate(contours):
	mean_area += cv2.contourArea(c)
	count += 1
mean_area /= count

#print mean_area
#print cv2.contourArea(cnt)


#area_threshold = cv2.contourArea(cnt) / 2	
Clusters = 0
for i, c in enumerate(contours):
        area = cv2.contourArea(c)
        # area can be configured
        if area > mean_area:
            Clusters += 1
            cv2.drawContours(img_threshold, contours, i, (255, 0, 0), -1)

cv2.imshow('threhsold',img_threshold)
print "Clusters = "+str(Clusters)


cv2.waitKey(0)
cv2.destroyAllWindows()

