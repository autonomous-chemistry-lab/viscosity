import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('160.jpg')

crop_img = img[450:550, 900:950]
cv2.imshow("crop", crop_img)
cv2.waitKey()