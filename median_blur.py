# importing the libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline # for Jupyter Notebook
# read the Image file
img2 = cv2.imread('Taj_Mahal.jpg')
# convert the image into RGB since OpenCv reads image into BGR Colors (3- channels) by default.
img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
plt.imshow(img2)
# applying the Median Blur
median = cv2.medianBlur(img2,(3,3)) # (3,3) is the kernel size
plt.imshow(median)
