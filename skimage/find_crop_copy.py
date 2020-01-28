import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('5_min20_R.jpg')

crop_img = img[50:1150,400:950]

cv2.imshow("crop", crop_img)
cv2.imwrite('5_min20_RC.jpg', crop_img, None)
cv2.waitKey()
