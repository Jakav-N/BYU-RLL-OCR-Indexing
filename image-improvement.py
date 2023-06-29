"""File designed to improve the sample images"""

import cv2
import os
import numpy as np

with os.scandir("C:\\Users\\jenia\\Downloads\\skagit-images") as it:
    for entry in it:
        #Read the image
        img = cv2.imread(entry.path)

        #Perform operations
        #https://stackoverflow.com/questions/9480013/image-processing-to-improve-tesseract-ocr-accuracy
        #img = cv2.resize(img, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        kernel = np.ones((1, 1), np.uint8)
        img = cv2.dilate(img, kernel, iterations=1)
        img = cv2.erode(img, kernel, iterations=1)
        img = cv2.adaptiveThreshold(cv2.GaussianBlur(img,(3,3),0), 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 13, 5)
        #img = cv2.threshold(cv2.GaussianBlur(img,(3,3),0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

        #Output image
        cv2.imwrite('C:\\Users\\jenia\\Dropbox\\Jacob\\Visual studio code\\RA-python-tools\\improved_images\\' + entry.name, img)


#for image in 
#